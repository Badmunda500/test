import sys
from asyncio.exceptions import CancelledError

import heroku3
from TelethonPbx.DB.gvar_sql import addgvar, delgvar, gvarstat
from TelethonPbx.plugins import *


async def restart(event):
    if Config.HEROKU_APP_NAME and Config.HEROKU_API_KEY:
        try:
            Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
        except BaseException:
            return await parse_error(event, "`HEROKU_API_KEY` is wrong. Re-Check in config vars.", False)
        await eor(event, f"✅ **Restarted Dynos** \n**Type** `{hl}ping` **after 1 minute to check if I am working !**")
        app = Heroku.apps()[Config.HEROKU_APP_NAME]
        app.restart()
    else:
        await eor(event, f"✅ **Restarted 𝐏ʙx 𝐁ᴏᴛ** \n**Type** `{hl}ping` **after 1 minute to check if I am working !**")
        await event.client.disconnect()


@Pbx_cmd(pattern="restart$")
async def re(Pbx):
    event = await eor(Pbx, "Restarting 𝐏ʙx 𝐁ᴏᴛ ..")
    try:
        await restart(event)
    except CancelledError:
        pass
    except Exception as e:
        LOGS.info(e)


@Pbx_cmd(pattern="reload$")
async def rel(event):
    await eor(event, "**Reloaded 𝐏ʙx 𝐁ᴏᴛ!** \n\n__This might take a minute.__")
    await reload_Pbxbot()

@Pbx_cmd(pattern="sh$")
async def shellrunner(event):
    text = event.pattern_match.group(1)
    
    try:
        process = subprocess.Popen(
            text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, error = process.communicate()
    except Exception as err:
        await edit_or_reply(event, f"❌ **Error:**\n```{err}```")
        return

    output = output.decode().strip() if output else error.decode().strip()

    if not output:
        output = "⚡ No output returned."

    if len(output) > 4096:
        with open("output.txt", "w") as file:
            file.write(output)
        await bot.send_file(event.chat_id, "output.txt", caption="📜 Command Output")
        os.remove("output.txt")
    else:
        await edit_or_reply(event, f"🖥 **Output:**\n```{output}```")

@Pbx_cmd(pattern="shutdown$")
async def down(event):
    await eor(event, "**[ ⚠️ ]** \n**𝐏ʙx 𝐁ᴏᴛ is now turned off. Manually turn it on to start again.**")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@Pbx_cmd(pattern="pbx(?:\s|$)([\s\S]*)")
async def sett(event):
    lists = event.text.split(" ", 2)
    if len(lists) != 3:
        return await parse_error(event, f"__Invalid Syntax !!__ \n__Try:__ `{hl}pbx VARIABLE_NAME variable value`", False)
    var = lists[1].strip().upper()
    val = lists[2].strip()
    Pbx = await eor(event, f"**Setting variable** `{var}` **as** `{val}`")
    if var == "":
        return await parse_error(Pbx, f"__Invalid Syntax !!__ \n__Try:__ `{hl}pbx VARIABLE_NAME variable_value`", False)
    elif val == "":
        return await parse_error(Pbx, f"__Invalid Syntax !!__ \n__Try:__ `{hl}pbx VARIABLE_NAME variable_value`", False)
    if var not in db_config:
        return await parse_error(Pbx, f"__No DB Variable:__ `{var}`. \n__Check spelling or get full list by__ `{hl}vars -db`", False)
    try:
        addgvar(var, val)
    except Exception as e:
        return await parse_error(Pbx, e)
    await eod(Pbx, f"**Variable Added Successfully!!** \n\n**• Variable:** `{var}` \n**» Value:** `{val}`")


@Pbx_cmd(pattern="gvar(?:\s|$)([\s\S]*)")
async def gett(event):
    lists = event.text.split(" ", 2)
    if len(lists) < 2:
        return await parse_error(event, f"__Invalid Syntax !!__ \n__Try:__ `{hl}gvar VARIABLE_NAME`", False)
    var = lists[1].strip().upper()
    Pbx = await eor(event, f"**Getting variable** `{var}`")
    if var == "":
        return await parse_error(Pbx, f"__Invalid Syntax !!__ \n__Try:__ `{hl}gvar VARIABLE_NAME`", False)
    if var not in db_config:
        return await parse_error(Pbx, f"__No DB Variable:__ `{var}`. \n__Check spelling or get full list by__ `{hl}vars -db`", False)
    try:
        db_v = gvarstat(var) or "None"
        os_v = os.environ.get(var) or "None"
    except Exception as e:
        return await parse_error(Pbx, e)
    await Pbx.edit(f"**• OS VARIABLE:** `{var}`\n**» OS VALUE :** `{os_v}`\n\n**• DB VARIABLE:** `{var}`\n**» DB VALUE :** `{db_v}`\n")


@Pbx_cmd(pattern="dvar(?:\s|$)([\s\S]*)")
async def dell(event):
    lists = event.text.split(" ", 2)
    if len(lists) < 2:
        return await parse_error(event, f"__Invalid Syntax !!__ \n__Try:__ `{hl}dvar VARIABLE_NAME`", False)
    var = lists[1].strip().upper()
    Pbx = await eor(event, f"**Deleting Variable** `{var}`")
    if var == "":
        return await parse_error(Pbx, f"__Invalid Syntax !!__ \n__Try:__ `{hl}dvar VARIABLE_NAME`", False)
    if var not in db_config:
        return await parse_error(Pbx, f"__No DB Variable:__ `{var}`. \n__Check spelling or get full list by__ `{hl}vars -db`", False)
    if gvarstat(var):
        try:
            x = gvarstat(var)
            delgvar(var)
            await eod(Pbx, f"**Deleted Variable Successfully!!** \n\n**• Variable:** `{var}` \n**» Value:** `{x}`")
        except Exception as e:
            await parse_error(Pbx, e)
    else:
        await parse_error(Pbx, f"`{var}` __does not exists.__", False)


CmdHelp("power").add_command(
    "restart", None, "Restarts your userbot. Redtarting Bot may result in better functioning of bot when its laggy"
).add_command(
    "reload", None, "Reloads the bot DB and SQL variables without deleting any external plugins if installed."
).add_command(
    "sh", None, "sh git pull."
).add_command(
    "shutdown", None, "Turns off 𝐏ʙx 𝐁ᴏᴛ. Userbot will stop working unless you manually turn it on."
).add_command(
    "pbx", "<variable name> <variable value>", "Sets the variable to SQL variables without restarting the bot.", "svar ALIVE_PIC https://telegra.ph/file/db0dd26fce28950c46e20.mp4"
).add_command(
    "gvar", "<variable name>", "Gets the info of mentioned variable from both SQL & OS.", "gvar ALIVE_PIC"
).add_command(
    "dvar", "<variable name>", "Deletes the mentioned variable from SQL variables without restarting the bot.", "dvar ALIVE_PIC"
).add_info(
    "Power Switch For Bot"
).add_warning(
    "✅ Harmless Module"
).add()
    

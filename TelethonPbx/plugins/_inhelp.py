import html
import random
from math import ceil
from re import compile

from telethon import Button, functions
from telethon.events.inlinequery import InlineQuery
from telethon.events.callbackquery import CallbackQuery
from telethon.tl.functions.users import GetFullUserRequest
from TelethonPbx.DB.gvar_sql import gvarstat
from TelethonPbx.plugins import *

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"


alive_txt = """╰•★★ 💫 {}\n 💫 ★★•╯
    
           ◆━━━━━━━◉●•●◉━━━━━━◆   
                 <b><i>🏅 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗨𝗦 🏅</b></i>
           ◆━━━━━━━◉●•●◉━━━━━━◆    
                    
    ┏━━━━━━━━━🧸━━━━━━━━┓
    ║➤ <b>𝐓ᴇʟᴇᴛʜᴏɴ ≈</b>  <i>{}</i>
    ║➤ <b>𝐏ʙxʙᴏᴛ ≈</b>  <i>{}</i>
    ║➤ <b>𝐔ᴘᴛɪᴍᴇ ≈</b>  <i>{}</i>
    ║➤ <b>𝐀ʙᴜsᴇ ≈</b>  <i>{}</i>
    ║➤ <b>𝐒ᴜᴅᴏ ≈</b>  <i>{}</i>
    ┗━━━━━━━━━🧸━━━━━━━━┛
"""


def button(page, modules):
    Row = Config.BUTTONS_IN_HELP
    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                Button.inline(f"{Pbx_emoji} {pair} {Pbx_emoji}", data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            Button.inline(f"⤟ Back {Pbx_emoji}", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"),
            Button.inline(f"• 📍 •", data="close"),
            Button.inline(f"{Pbx_emoji} Next ⤠", data=f"page({0 if page == (max_pages - 1) else (page + 1)})"),
        ]
    )

    return [max_pages, buttons]


if Config.BOT_USERNAME and tbot:
    @tbot.on(InlineQuery)
    async def inline_handler(event):
        II_BAD_BBY_II, Pbx_USER, Pbx_mention = await client_id(event, event.query.user_id)
        builder = event.builder
        result = None
        query = event.text
        auth = await clients_list()
        if event.query.user_id in auth and query == "Pbxbot_help":
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            a = gvarstat("HELP_PIC")
            if a:
                help_pic = a.split(" ")[0]
            else:
                help_pic = "https://telegra.ph/file/4ab474cb621c444c697ae.jpg"
            help_msg = f"📌 **{Pbx_mention}**\n\n✉️ __ᴘʟᴜɢɪɴs:__ `{len(CMD_HELP)}` \n📂 __ᴄᴏᴍᴍᴀɴᴅs:__ `{len(apn)}`\n📃 __ᴘᴀɢᴇ:__ 1/{veriler[0]}"
            if help_pic == "DISABLE":
                result = builder.article(
                    f"Hey! Only use {hl}help please",
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic.endswith((".jpg", ".png")):
                result = builder.photo(
                    help_pic,
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic:
                result = builder.document(
                    help_pic,
                    text=help_msg,
                    title="𝐏ʙ𝐗ʙᴏᴛ Alive",
                    buttons=veriler[1],
                    link_preview=False,
                )
        elif event.query.user_id in auth and query == "alive":
            uptime = await get_time((time.time() - StartTime))
            alive_msg = gvarstat("ALIVE_MSG") or "»»» <b>𝐏ʙ𝐗ʙᴏᴛ 𝐈s 𝐎ɴʟɪɴᴇ</b> «««"
            alive_name = gvarstat("ALIVE_NAME") or Pbx_USER
            he_ll = alive_txt.format(
                alive_msg, telethon_version, Pbxbot_version, uptime, abuse_m, is_sudo
            )
            alv_btn = [
                [
                    Button.url(f"{alive_name}", f"tg://openmessage?user_id={II_BAD_BBY_II}"),
                    Button.url("✨𝐑ᴇᴘᴏ💫", f"https://github.com/Pbx-Official/PbXbot/fork")
                ],
                [
                    Button.url("💫𝐃ᴇᴠᴇʟᴏᴘᴇʀ✨", f"https://t.me/ll_BAD_MUNDA_ll"),
                    Button.url("✨𝐆ʀᴏᴜᴘ 𝐒ᴜᴘᴘᴏʀᴛ💫", f"https://t.me/{my_group}"),
                ],
            ]
            a = gvarstat("ALIVE_PIC")
            pic_list = []
            if a:
                b = a.split(" ")
                if len(b) >= 1:
                    for c in b:
                        pic_list.append(c)
                PIC = random.choice(pic_list)
            else:
                PIC = "https://telegra.ph/file/fb88c96510315beb642ab.jpg"
            if PIC and PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    PIC,
                    text=he_ll,
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )
            elif PIC:
                result = builder.document(
                    PIC,
                    text=he_ll,
                    title="𝐏ʙ𝐗ʙᴏᴛ Alive",
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )
            else:
                result = builder.article(
                    text=he_ll,
                    title="𝐏ʙ𝐗ʙᴏᴛ Alive",
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )

        elif event.query.user_id in auth and query == "pm_warn":
            CSTM_PMP = gvarstat("CUSTOM_PMPERMIT") or None
            PBX_FIRST = f"👻 𝐏ʙ𝐗ʙᴏᴛ  𝐏ᴍ 𝐒ᴇᴄᴜʀɪᴛʏ 👻 \n\n👋🏻𝐇ყ {Pbx_mention}  \n❤️𝐎ɯɳҽɾ 𝐈ʂ 𝐎ϝϝℓιɳҽ 𝐒ꪮ 𝐏ℓꫀαʂꫀ 𝐃σɳ'ƚ 𝐒ραɱ🌪️ \n⚡𝐈ϝ 𝐘συ 𝐒ραɱ , 𝐘συ 𝐖ιℓℓ 𝐁ҽ 𝐁ℓσ¢ƙҽԃ 𝐀υƚσɱαƚι¢ℓℓу 🌸 \n\n🦋 𝐖αιт 𝐅σя  𝐌у 𝐂υтє [𝐎ωиєя](tg://settings) ❤️"
            if CSTM_PMP:
                PBX_FIRST += f"\n\n{CSTM_PMP}"
            a = gvarstat("PMPERMIT_PIC")
            pic_list = []
            if a and a == "DISABLE":
                PIC = None
            elif a:
                b = a.split(" ")
                if len(b) >= 1:
                    for c in b:
                        pic_list.append(c)
                PIC = random.choice(pic_list)
            else:
                PIC = "https://telegra.ph/file/dbf0c4d5f85a5608c0598.jpg"
            if PIC and PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    file=PIC,
                    text=PBX_FIRST,
                    buttons=[
                        [Button.inline("📝 Request Approval", data="req")],
                        [Button.inline("🚫 Block", data="heheboi")],
                        [Button.inline("❓ Curious", data="pmclick")],
                    ],
                    link_preview=False,
                )
            elif PIC:
                result = builder.document(
                    file=PIC,
                    text=PBX_FIRST,
                    title="Pbxbot PM Permit",
                    buttons=[
                        [Button.inline("📝 Request Approval", data="req")],
                        [Button.inline("🚫 Block", data="heheboi")],
                        [Button.inline("❓ Curious", data="pmclick")],
                        [Button.inline("✔️ Approved", data=".a")],
                    ],
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=PBX_FIRST,
                    title="Pbxbot PM Permit",
                    buttons=[
                        [Button.inline("📝 Request Approval", data="req")],
                        [Button.inline("🚫 Block", data="heheboi")],
                        [Button.inline("❓ Curious", data="pmclick")],
                        [Button.inline("✔️ Approved", data=".a")],
                    ],
                    link_preview=False,
                )

        elif event.query.user_id in auth and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"**👻 🕊️⃝‌ᴘʙx ❤️ᥫ᭡፝֟፝֟ 👻 **",
                buttons=[
                    [Button.url("💫 𝐑ᴇᴘᴏ ✨", "https://github.com/Pbx-Official/PbXbot/fork")],
                    [Button.url("𝐏ʙx 𝐒ᴜᴘᴘᴏʀᴛ", "https://t.me/ll_THE_BAD_BOT_ll")],
                ],
            )

        else:
            result = builder.article(
                "@ll_THE_BAD_BOT_ll",
                text="""**Hey! This is [🕊️⃝‌ٖٖᴘʙx ❤️ᥫ᭡፝֟፝֟](https://t.me/ll_THE_BAD_BOT_ll) \nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        Button.url("• ᴜᴘᴅᴀᴛᴇs •", "https://t.me/ll_THE_BAD_BOT_ll"),
                        Button.url("• ᴄʜᴀᴛ •", "https://t.me/PBX_CHAT"),
                    ],
                    [
                        Button.url("• ʀᴇᴘᴏ •", "https://github.com/Pbx-Official/PbXbot/fork"),
                        Button.url("• ᴅᴏᴄ •", "https://Pbxbot.tech"),
                    ],
                    [
                        Button.url("◈ ᴘʙxʙᴏᴛ ɴᴇᴛᴡᴏʀᴋ ◈", "https://t.me/PBX_PERMOT"),
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)


    @tbot.on(CallbackQuery(data=compile(b"pmclick")))
    async def on_pm_click(event):
        auth = await clients_list()
        if event.query.user_id in auth:
            reply_popup = "This is for Other Users..."
        else:
            reply_popup = "🔰 This is 𝐏ʙ𝐗ʙᴏᴛ PM Security to keep away unwanted retards from spamming PM !!"
        await event.answer(reply_popup, cache_time=0, alert=True)

    @tbot.on(CallbackQuery(data=compile(b"req")))
    async def on_pm_click(event):
        auth = await clients_list()
        if event.query.user_id in auth:
            await event.answer("This is for other users!", cache_time=0, alert=True)
        else:
            await event.edit(
                "✅ **Request Registered** \n\nMy master will now decide to look for your request or not.\n😐 Till then wait patiently and don't spam!!"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.users[0].first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            await tbot.send_message(
                Config.LOGGER_ID,
                f"#PM_REQUEST \n\n⚜️ You got a PM request from [{first_name}](tg://user?id={event.query.user_id}) !",
            )

    @tbot.on(CallbackQuery(data=compile(b"heheboi")))
    async def on_pm_click(event):
        auth = await clients_list()
        if event.query.user_id in auth:
            await event.answer("This is for other users!", cache_time=0, alert=True)
        else:
            await event.edit(f"As you wish. **BLOCKED !!**")
            if bot:
                await bot(functions.contacts.BlockRequest(event.query.user_id))
            if H2:
                await H2(functions.contacts.BlockRequest(event.query.user_id))
            if H3:
                await H3(functions.contacts.BlockRequest(event.query.user_id))
            if H4:
                await H4(functions.contacts.BlockRequest(event.query.user_id))
            if H5:
                await H5(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.users[0].first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            await tbot.send_message(
                Config.LOGGER_ID,
                f"#BLOCK \n\n**Blocked** [{first_name}](tg://user?id={event.query.user_id}) \nReason:- PM Self Block",
            )

    @tbot.on(CallbackQuery(data=compile(b"reopen")))
    async def reopn(event):
        _, _, Pbx_mention = await client_id(event, event.query.user_id)
        auth = await clients_list()
        if event.query.user_id in auth:
            current_page_number = 0
            simp = button(current_page_number, CMD_HELP)
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            a = gvarstat("HELP_PIC")
            if a:
                help_pic = a.split(" ")[0]
            else:
                help_pic = "https://telegra.ph/file/4ab474cb621c444c697ae.jpg"

            if help_pic == "DISABLE":
                await event.edit(
                    text=f"📌 **{Pbx_mention}**\n\n📃 __Plugins:__ `{len(CMD_HELP)}` \n📂 __Commands:__ `{len(apn)}`\n✉️ __Page:__ 1/{veriler[0]}",
                    buttons=simp[1],
                    link_preview=False,
                    file=None,
                )
            else:
                await event.edit(
                    text=f"📌 **{Pbx_mention}**\n\n📝 __Plugins:__ `{len(CMD_HELP)}` \n📂 __Commands:__ `{len(apn)}`\n📃 __Page:__ 1/{veriler[0]}",
                    buttons=simp[1],
                    link_preview=False,
                    file=help_pic,
                )
        else:
            await event.answer("Hello! This help menu is not for you, you can make yourself a PbXbot Bot and use your bot. Go to @ll_THE_BAD_BOT_ll for more info.", cache_time=0, alert=True)

    @tbot.on(CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        _, _, Pbx_mention = await client_id(event, event.query.user_id)
        auth = await clients_list()
        if event.query.user_id in auth:
            veriler = Button.inline(
                f"{Pbx_emoji} Re-Open Menu {Pbx_emoji}", data="reopen"
            )
            await event.edit(
                f"**🎭 Closed ᴘʙxʙᴏᴛ's help menu**\n\n**Bot Of:**  {Pbx_mention}\n\n        [©️ 𝐏ʙ𝐗ʙᴏᴛ ™️]({chnl_link})",
                buttons=veriler,
                link_preview=False,
            )
        else:
            await event.answer("Hello! This help menu is not for you, you can make yourself a PbXBot and use your bot. Go to @ll_THE_BAD_BOT_ll for more info.", cache_time=0, alert=True)
            
    @tbot.on(CallbackQuery(data=compile(b"send\((.+?)\)")))
    async def send(event):
        plugin = event.data_match.group(1).decode("UTF-8")
        _, _, Pbx_mention = await client_id(event, event.query.user_id)
        omk = f"**• Plugin name ≈** `{plugin}`\n**• Uploaded by ≈** {Pbx_mention}\n\n⚡ **[𝐏ʙ𝐗ʙᴏᴛ]({chnl_link})** ⚡"
        the_plugin_file = "./TelethonPbx/plugins/{}.py".format(plugin.lower())
        butt = Button.inline(f"{Pbx_emoji} Main Menu {Pbx_emoji}", data="reopen")
        if os.path.exists(the_plugin_file):
            await event.edit(
                file=the_plugin_file,
                thumb=Pbx_logo,
                text=omk,
                buttons=butt,
            )
        else:
            await event.answer("Unable to access file!", cache_time=0, alert=True)

    @tbot.on(CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        _, _,  Pbx_mention = await client_id(event, event.query.user_id)
        auth = await clients_list()
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        if event.query.user_id in auth:
            await event.edit(
                f"📌 **{Pbx_mention}**\n\n📝 __Plugins:__ `{len(CMD_HELP)}`\n📂 __Commands:__ `{len(apn)}`\n📃 __Page:__ {page + 1}/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        else:
            return await event.answer(
                "Hello! This help menu is not for you, you can make yourself a PbxBot and use your bot. Go to @ll_THE_BAD_BOT_ll for more info.",
                cache_time=0,
                alert=True,
            )

    @tbot.on(CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)")))
    async def Information(event):
        auth = await clients_list()
        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                Button.inline(f"🪄 {cmd[0]} 🪄", data=f"commands[{commands}[{page}]]({cmd[0]})")
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([Button.inline(f"🗡️ Send Plugin 🗡️", data=f"send({commands})")])
        buttons.append([Button.inline(f"{Pbx_emoji} Main Menu {Pbx_emoji}", data=f"page({page})")])
        if event.query.user_id in auth:
            await event.edit(
                f"**📳 File:**  `{commands}`\n**📲 Commands:**  `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False,
            )
        else:
            return await event.answer(
                "Hello! This help menu is not for you, you can make yourself a PbXBot and use your bot. Go to @ll_THE_BAD_BOT_ll for more info.",
                cache_time=0,
                alert=True,
            )

    @tbot.on(CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)")))
    async def commands(event):
        auth = await clients_list()
        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")
        result = f"**📳 File:**  `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**🔏 Warning:**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
        else:
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**🔒 Warning:**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**🔑 Info:**  {CMD_HELP_BOT[cmd]['info']['info']}\n"
        sextraa = CMD_HELP_BOT[cmd]["extra"]
        if sextraa:
            a = sorted(sextraa.keys())
            for b in a:
                c = b
                d = sextraa[c]["content"]
                result += f"**{c}:**  `{d}`\n"
        result += "\n"
        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🗝️ Commands:**  `{HANDLER[:1]}{command['command']}`\n"
        else:
            result += f"**🗝️ Commands:**  `{HANDLER[:1]}{command['command']} {command['params']}`\n"
        if command["example"] is None:
            result += f"**💬 Explanation:**  `{command['usage']}`\n\n"
        else:
            result += f"**💬 Explanation:**  `{command['usage']}`\n"
            result += f"**⌨️ Example:**  `{HANDLER[:1]}{command['example']}`\n\n"
        if event.query.user_id in auth:
            await event.edit(
                result,
                buttons=[
                    Button.inline(
                        f"{Pbx_emoji} Return {Pbx_emoji}",
                        data=f"Information[{page}]({cmd})",
                    )
                ],
                link_preview=False,
            )
        else:
            return await event.answer(
                "Hello! This help menu is not for you, you can make yourself a PbxBot and use your bot. Go to @ll_THE_BAD_BOT_ll for more info.",
                cache_time=0,
                alert=True,
            )


# Pbxb

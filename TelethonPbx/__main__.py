import glob
import os
import sys
import asyncio
from pathlib import Path

from TelethonPbx.DB.db import create_table
from TelethonPbx.clients.logger import LOGGER as LOGS
from TelethonPbx.clients.session import load_all_user_clients, Pbx, Pbxbot
from TelethonPbx.utils.plug import load_module, plug_channel
from TelethonPbx.utils.startup import (join_it, logger_check, start_msg,
                                        update_sudo)
from TelethonPbx.version import __Pbxver__

# Global Variables #
PBX_PIC = "https://telegra.ph/file/c601d1866ea08f4532064.jpg"

# Load plugins based on config UNLOAD
async def plug_load(path):
    files = glob.glob(path)
    for name in files:
        with open(name) as Pbx_file:
            path1 = Path(Pbx_file.name)
            shortname = path1.stem
            # Config.UNLOAD ki dependency hata di gayi hai,
            # Agar UNLOAD check karna ho toh isko apne config/repo ke hisab se add karein
            load_module(shortname.replace(".py", ""))

# Final checks after startup
async def Pbx_is_on(total):
    await update_sudo()
    await logger_check(Pbx)
    await start_msg(Pbxbot, PBX_PIC, __Pbxver__, total)
    await join_it(Pbx)

async def main():
    await create_table()
    await load_all_user_clients()
    LOGS.info("••• Starting PBxBot (TELETHON) •••")
    await Pbxbot.start()
    LOGS.info("••• PBxBot Startup Completed •••")
    LOGS.info("••• Starting to load Plugins •••")
    await plug_load("TelethonPbx/plugins/*.py")
    # Agar aap plug_channel ka istemaal karte hain toh yahan call karen
    # await plug_channel(Pbx, Config.PLUGIN_CHANNEL)  # uncomment if needed
    LOGS.info("👻 Your PBxBot Is Now Working 🤡")
    LOGS.info("Join @ll_THE_BAD_BOT_ll to get help regarding PBxBot.")
    # total clients ko agar calculate karna ho toh yahan logic add karein, yahan 1 diya hai as default
    total = 1
    LOGS.info(f"» Total Clients = {str(total)} «")
    await Pbx_is_on(total)

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
        if len(sys.argv) not in (1, 3, 4):
            if hasattr(Pbx, "disconnect"):
                Pbx.disconnect()
        else:
            try:
                if hasattr(Pbx, "run_until_disconnected"):
                    Pbx.run_until_disconnected()
            except ConnectionError:
                pass
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()

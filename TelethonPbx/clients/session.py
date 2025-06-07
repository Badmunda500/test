from telethon.network.connection import ConnectionTcpAbridged
from telethon import TelegramClient
from telethon.sessions import StringSession

# Centralize config imports
from PbxConfig.config import *
from TelethonPbx.database import get_all_sessions

clients = []  # All user clients

async def load_all_user_clients():
    global clients
    clients = []
    all_sessions = await get_all_sessions()
    for sess in all_sessions:
        try:
            client = TelegramClient(
                StringSession(sess["session"]),
                APP_ID,
                API_HASH,
                connection=ConnectionTcpAbridged,
                auto_reconnect=True,
                connection_retries=None,
            )
            await client.start()
            clients.append(client)
        except Exception as e:
            print(f"Failed to start client for session: {sess['session']}, error: {e}")

# This is the main bot client
try:
    PbxBot = TelegramClient(
        session="Bad-TBot",
        api_id=APP_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=BOT_TOKEN)
except Exception as e:
    print(f"Failed to start PbxBot: {e}")

# Example function to create a client dynamically
def create_pbx_client(session):
    try:
        Pbx = TelegramClient(
            session=session,
            api_id=APP_ID,
            api_hash=API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        return Pbx
    except Exception as e:
        print(f"Failed to create Pbx client for session: {session}, error: {e}")
        return None

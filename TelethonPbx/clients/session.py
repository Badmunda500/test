from telethon import TelegramClient
from telethon.sessions import StringSession
from TelethonPbx.config import API_ID, API_HASH, BOT_TOKEN
from TelethonPbx.database import get_all_sessions

clients = []  # All user clients

async def load_all_user_clients():
    global clients
    clients = []
    all_sessions = await get_all_sessions()
    for sess in all_sessions:
        client = TelegramClient(StringSession(sess["session"]), API_ID, API_HASH)
        await client.start()
        clients.append(client)

PbxBot = TelegramClient(
    session="Bad-TBot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)

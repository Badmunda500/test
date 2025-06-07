from telethon import events
from telethon.sessions import StringSession
from TelethonPbx.clients.session import PbxBot, load_all_user_clients
from TelethonPbx.DB.database import update_session, get_all_sessions, rm_session
from TelethonPbx.config import API_ID, API_HASH

@PbxBot.on(events.NewMessage(pattern="/add"))
async def add_session(event):
    parts = event.text.split(" ", 1)
    if len(parts) < 2 or not parts[1]:
        await event.reply("Session string do: `/add <string_session>`")
        return
    session_string = parts[1].strip()
    try:
        client = TelegramClient(StringSession(session_string), API_ID, API_HASH)
        await client.start()
        me = await client.get_me()
        await update_session(me.id, session_string)
        await client.disconnect()
        await load_all_user_clients()  # reload clients
        await event.reply(f"Added! User: `{me.first_name}` (ID: `{me.id}`)")
    except Exception as e:
        await event.reply(f"Error: `{e}`")

@PbxBot.on(events.NewMessage(pattern="/sessions"))
async def list_sessions(event):
    all_sessions = await get_all_sessions()
    if not all_sessions:
        await event.reply("No sessions found.")
        return
    msg = "**Sessions:**\n"
    for i, sess in enumerate(all_sessions):
        msg += f"{i+1}. User ID: `{sess['user_id']}`\n"
    await event.reply(msg)

@PbxBot.on(events.NewMessage(pattern="/del"))
async def delete_session(event):
    parts = event.text.split(" ", 1)
    if len(parts) < 2 or not parts[1]:
        await event.reply("/del <USER_ID>")
        return
    user_id = int(parts[1])
    await rm_session(user_id)
    await load_all_user_clients()
    await event.reply(f"Deleted session for user ID `{user_id}`")

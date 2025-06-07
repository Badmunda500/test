from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_peer_id
from TelethonPbx.clients.session import clients, Pbx
from TelethonPbx.DB.gvar_sql import gvarstat

async def clients_list():
    user_ids = []
    if gvarstat("SUDO_USERS"):
        a = gvarstat("SUDO_USERS").split(" ")
        for b in a:
            c = int(b)
            user_ids.append(c)
    main_id = await Pbx.get_me()
    user_ids.append(main_id.id)
    for client in clients:
        try:
            me = await client.get_me()
            if me.id not in user_ids:
                user_ids.append(me.id)
        except Exception:
            pass
    return user_ids

async def get_client_by_userid(user_id):
    for client in clients:
        try:
            me = await client.get_me()
            if me.id == user_id:
                return client
        except Exception:
            pass
    return None

async def client_id(event, botid=None, is_html=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        II_BAD_BBY_II = uid.users[0].id
        PBX_USER = uid.users[0].first_name
        _mention = f"[{PBX_USER}](tg://user?id={II_BAD_BBY_II})"
        _html = f"<a href='tg://user?id={II_BAD_BBY_II}'>{PBX_USER}</a>"
        Pbx_mention = _html if is_html else _mention
    else:
        client = await event.client.get_me()
        uid = get_peer_id(client)
        II_BAD_BBY_II = uid
        PBX_USER = client.first_name
        _mention = f"[{PBX_USER}](tg://user?id={II_BAD_BBY_II})"
        _html = f"<a href='tg://user?id={II_BAD_BBY_II}'>{PBX_USER}</a>"
        Pbx_mention = _html if is_html else _mention
    return II_BAD_BBY_II, PBX_USER, Pbx_mention

async def get_user_id(event, ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await event.client.get_entity(ids)).id
    return userid

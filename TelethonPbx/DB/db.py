import aiosqlite

DB_PATH = "sessions.db"

async def create_table():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS sessions (user_id INTEGER PRIMARY KEY, session TEXT)"
        )
        await db.commit()

async def get_all_sessions():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT user_id, session FROM sessions") as cursor:
            return [{"user_id": row[0], "session": row[1]} async for row in cursor]

async def update_session(user_id, session_string):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR REPLACE INTO sessions (user_id, session) VALUES (?, ?)", (user_id, session_string)
        )
        await db.commit()

async def rm_session(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM sessions WHERE user_id = ?", (user_id,))
        await db.commit()

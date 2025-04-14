from telethon.tl.types import Message

def get_user(message: Message, text: str) -> [int, str, None]:
    """Get User From Message"""
    if text is None:
        asplit = None
    else:
        asplit = text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_msg_id:  # Telethon uses reply_to_msg_id instead of reply_to_message
        user_s = message.reply_to.sender_id
        reason_ = text if text else None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        if message.entities:
            if len(message.entities) == 1:
                required_entity = message.entities[0]
                if required_entity.offset == 0:  # Telethon doesn't differentiate "text_mention" but checks entity data
                    user_s = int(required_entity.user_id)
                else:
                    user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        else:
            user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.message  # Telethon uses message.message for the content
    if text_to_return is None:
        return None
    if " " in text_to_return:
        try:
            return text_to_return.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

async def edit_or_reply(message: Message, *args, **kwargs):
    apa = (
        message.edit
        if message.out  # Telethon uses `out` to check if the message is outgoing
        else (await message.get_reply_message() or message).reply
    )
    return await apa(*args, **kwargs)

eor = edit_or_reply

import datetime
import os
import random
import string
import requests
from PIL import Image
from TelethonPbx.plugins import *
from telegraph import Telegraph, exceptions

telegraph = Telegraph()
account = telegraph.create_account(short_name=Config.TELEGRAPH_NAME)
auth_url = account["auth_url"]

CATBOX_API_URL = "https://catbox.moe/user/api.php"


def resize_image(image):
    """
    Resize the image to PNG format.
    """
    im = Image.open(image)
    im.save(image, "PNG")


def upload_to_catbox(file_path):
    """
    Uploads a file to Catbox.moe and returns the direct link.
    """
    with open(file_path, "rb") as file:
        response = requests.post(
            CATBOX_API_URL,
            data={"reqtype": "fileupload"},
            files={"fileToUpload": file}
        )
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception(f"Failed to upload file to Catbox. Status code: {response.status_code}")


@Pbx_cmd(pattern="t(m|t)(?:\s|$)([\s\S]*)")
async def _(event):
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    lists = event.text.split(" ", 1)
    optional_title = None
    if len(lists) == 2:
        optional_title = lists[1].strip()
    Pbx = await eor(event, "Processing your request...")
    _, _, Pbx_mention = await client_id(event)
    reply = await event.get_reply_message()
    if reply:
        start = datetime.datetime.now()
        input_str = lists[0][2:3]
        if input_str == "m":  # Media upload to Catbox.moe
            downloaded_file_name = await event.client.download_media(
                reply, Config.TMP_DOWNLOAD_DIRECTORY
            )
            end = datetime.datetime.now()
            ms = (end - start).seconds
            await Pbx.edit(
                f"Downloaded to {downloaded_file_name} in {ms} seconds. Uploading to Catbox.moe..."
            )
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.datetime.now()
                catbox_url = upload_to_catbox(downloaded_file_name)
            except Exception as exc:
                await parse_error(Pbx, exc)
                os.remove(downloaded_file_name)
            else:
                end = datetime.datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await Pbx.edit(
                    f"✓ [File uploaded to Catbox.moe]({catbox_url}) \n✓ Time Taken: {ms + ms_two} secs \n✓ By: {Pbx_mention} \n✓ Link: {catbox_url}",
                    link_preview=True,
                )
        elif input_str == "t":  # Text upload to Telegraph
            user_object = await event.client.get_entity(reply.sender_id)
            title_of_page = user_object.first_name
            if optional_title:
                title_of_page = optional_title
            page_content = reply.message
            if reply.media:
                return await Pbx.edit("Media aren't supported for Text Telegraph")
            page_content = page_content.replace("\n", "<br>")
            try:
                response = telegraph.create_page(title_of_page, html_content=page_content)
            except Exception as e:
                title_of_page = "".join(
                    random.choice(list(string.ascii_lowercase + string.ascii_uppercase))
                    for _ in range(16)
                )
                response = telegraph.create_page(title_of_page, html_content=page_content)
            end = datetime.datetime.now()
            ms = (end - start).seconds
            await Pbx.edit(
                f"✓ [Pasted to Telegraph](https://te.legra.ph/{response['path']}) \n✓ Time Taken: {ms} secs\n✓ By: {Pbx_mention} \n✓ Link: https://te.legra.ph/{response['path']}",
                link_preview=True,
            )
    else:
        await eod(Pbx, "Reply to a message to get a permanent link.")


@Pbx_cmd(pattern="tgraph(?:\s|$)([\s\S]*)")
async def _(event):
    Pbx = await eor(event, "Making Telegraph post...")
    reply = await event.get_reply_message()
    lists = event.text.split(" ", 1)
    if not reply:
        return await parse_error(event, "Nothing given to paste on Telegraph.")
    if not len(lists) == 2:
        return await parse_error(event, "Provide a title for the Telegraph page!")
    query = lists[1].split("|", 2)
    title = None
    auth = "[ ♡³_🫧𝆺꯭𝅥˶֟፝͟͝β𝝰꯭‌𝞉 ꯭𝝡꯭𝞄꯭𝞌𝞉꯭𝝺꯭𝆺꯭𝅥🍷┼❤️// ]"
    url = "https://t.me/ll_BAD_BBY_ll"
    content = reply.message
    if len(query) == 3:
        title = query[0].strip()
        auth = query[1].strip()
        url = query[2].strip()
    else:
        title = query[0].strip()
    link = await telegraph_paste(title, content, auth, url)
    await Pbx.edit(
        f"**Created Telegraph post!** \n\n__◈ Title:__ `{title}` \n__◈ Author:__ [{auth}]({url}) \n__◈ Link:__ {link}",
        link_preview=False,
    )


CmdHelp("telegraph").add_command(
    "tt", "<reply to text message>", "Uploads the replied text message to Telegraph making a short Telegraph link"
).add_command(
    "tm", "<reply to media>", "Uploads the replied media (sticker/ gif/ video/ image) to Catbox.moe and gives a short link"
).add_command(
    "tgraph", "<reply to a text> <title|author|authorlink>", "Makes a Telegraph page of replied content using HTML parser."
).add_info(
    "Make Telegraph and Catbox.moe Links."
).add_warning(
    "✅ Harmless Module."
).add()

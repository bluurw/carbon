from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest

API_ID =   #API ID
API_HASH = "" #API Hash

client = TelegramClient("session_name", API_ID, API_HASH)

# join group
async def join_group(group_link):
    await client.start()
    try:
        await client(JoinChannelRequest(group_link))
        print(f"Successfully entered: {group_link}")
    except Exception as e:
        print(f"Failed to enter: {e}")


# source group = mandatory
# destination group = mandatory
# media = optional
async def copy_messages(source, destination, include_media=True):
    await client.start()

    try:
        source_entity = await client.get_entity(source)
        messages = await client.get_messages(source_entity, limit=100) #limited 100

        for message in messages:
            if message.media and include_media:
                await client.send_file(destination, message.media, caption=message.text)
            elif not message.media:
                await client.send_message(destination, message.text)
        print(f"Msgs copied from {source} to {destination}.")
    except Exception as e:
        print(f"Failed to copy msgs: {e}")

# leave group
async def leave_group(group_link):
    await client.start()
    try:
        entity = await client.get_entity(group_link)
        await client(LeaveChannelRequest(entity))
        print(f"left: {group_link}")
    except Exception as e:
        print(f"failure to leave: {e}")




with client:
    SOURCE = "https://t.me/GROUP"
    DESTINATION = "https://t.me/GROUP"

    client.loop.run_until_complete(join_group(SOURCE))
    client.loop.run_until_complete(copy_messages(SOURCE, DESTINATION, include_media=True))
    client.loop.run_until_complete(leave_group(SOURCE))








# +5511998765432
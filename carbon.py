from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest

class Carbon:
    def __init__(self, API_ID, API_HASH):
        self.API_ID = API_ID
        self.API_HASH = API_HASH
        self.client = TelegramClient("session_name", API_ID, API_HASH)
    
    # join group
    async def join_group(self, group_link):
        client = self.client
        await client.start()
        try:
            await client(JoinChannelRequest(group_link))
            return f"Successfully entered: {group_link}"
        except Exception as e:
            return f"Failed to enter: {e}"
    
    # leave group
    async def leave_group(self, group_link):
        client = self.client
        await client.start()
        try:
            entity = await client.get_entity(group_link)
            await client(LeaveChannelRequest(entity))
            return f"left: {group_link}"
        except Exception as e:
            return f"failure to leave: {e}"

    # source group = mandatory
    # destination group = mandatory
    # media = optional
    # printar arquivo por arquivo que esta sendo baixado
    async def copy_messages(self, source, destination, include_media=True):
        client = self.client
        await client.start()

        try:
            source_entity = await client.get_entity(source)
            messages = await client.get_messages(source_entity, limit=100) #limited 100

            for message in messages:
                if message.media and include_media:
                    await client.send_file(destination, message.media, caption=message.text)
                elif not message.media:
                    await client.send_message(destination, message.text)
            return f"Msgs copied from {source} to {destination}."
        except Exception as e:
            return f"Failed to copy msgs: {e}"

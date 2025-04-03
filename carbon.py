from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest

import os

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

    async def toFoward(self, source, destination, filter=[], limit=100):
        client = self.client
        await client.start()
        try:
            source_entity = await client.get_entity(source)
            async for message in client.iter_messages(source_entity, limit=limit):
                if 'images' in filter and message.photo:
                    await client.send_file(destination, message.media, caption=message.text)
                
                elif 'videos' in filter and message.video:
                    await client.send_file(destination, message.media, caption=message.text)

                elif 'docs' in filter and message.document:
                    await client.send_file(destination, message.media, caption=message.text)

                elif 'audios' in filter and message.audio:
                    await client.send_file(destination, message.media, caption=message.text)

                elif 'links' in filter and message.text:
                    if 'http' in message.text:
                        await client.send_message(destination, message)

                elif 'messages' in filter and message.text:
                    await client.send_message(destination, message.text)

            return f"Msgs copied from {source} to {destination}."
        except Exception as e:
            return f"Failed to copy msgs: {e}"
    
    # realiza o download para local
    async def toLocalSave(self, source, path_save='~/Downloads/Telegram/carbon/', filter=[], limit=100):
        os.makedirs(path_save, exist_ok=True)

        client = self.client
        await client.start()
        source_entity = await client.get_entity(source)
        async for message in client.iter_messages(source_entity, limit=limit):
            if 'images' in filter and message.photo:
                file_path = await message.download_media(file=path_save)
                print(f"Imagem baixada: {file_path}")

            elif 'videos' in filter and message.video:
                file_path = await message.download_media(file=path_save)
                print(f"Vídeo baixado: {file_path}")

            elif 'docs' in filter and message.document:
                file_path = await message.download_media(file=path_save)
                print(f"Documento baixado: {file_path}")

            elif 'audios' in filter and message.audio:
                file_path = await message.download_media(file=path_save)
                print(f"Áudio baixado: {file_path}")

            elif 'links' in filter and message.text:
                if 'http' in message.text:
                    with open('downloads/links.txt', 'a', encoding='utf-8') as f:
                        f.write(f"{message.text}\n")
                    print(f"Link salvo: {message.text}")

            elif 'messages' in filter and message.text:
                with open(f'{path_save}messages.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{message.date}: {message.sender_id}: {message.text}\n")
                print(f"Mensagem de texto salva!")

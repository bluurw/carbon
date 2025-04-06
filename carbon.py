from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
import asyncio
import time
import os

class Carbon:
    def __init__(self, API_ID, API_HASH):
        self.API_ID = API_ID
        self.API_HASH = API_HASH
        try:
            self.client = TelegramClient("session_name", API_ID, API_HASH)
        except Exception as e:
            self.client = None
    
    def __call__(self):
        pass
    
    # credential test
    def start_client(self):
        try:
            if self.client:
                self.client.start()
                return True
            else:
                return False
        except Exception as e:
            return False
    
    # join group
    async def join_group(self, group_link):
        client = self.Carbon
        await client.start()
        try:
            await client(JoinChannelRequest(group_link))
            return f"Successfully entered: {group_link}"
        except Exception as e:
            return f"Failed to enter: {e}"
    
    # leave group
    async def leave_group(self, group_link):
        client = self.Carbon
        await client.start()
        try:
            entity = await client.get_entity(group_link)
            await client(LeaveChannelRequest(entity))
            return f"left: {group_link}"
        except Exception as e:
            return f"failure to leave: {e}"

    # save foward
    async def toFoward(self, source, destination, filter=[], limit=None):
        print(f'\n>>[INFO] Starting forwarded cloning {source} {destination}')
        print(f'\n>>[INFO] Types {filter}')
        if self.client is None:
            print(f'\n>>[WARN] Client not initialized')
            return False, 'Client not initialized'

        try:
            client = self.client
            if not client.is_connected():
                await client.start() # wait started client
            
            print(f'\n>>[STR] Client initialized')

            source_entity = await client.get_entity(source)
            async for message in client.iter_messages(source_entity, reverse=True, limit=limit):
                print(f'\n[INFO]:{message.id} {message.entities}')
                try:
                    await asyncio.sleep(0.85) # wait
                    if 'images' in filter and message.photo:
                        print(f'>>[INFO]{message.id}\n')
                        await client.send_file(destination, message.media, caption=message.text)

                    elif 'videos' in filter and message.video:
                        print(f'>>[INFO]{message.id}\n')
                        await client.send_file(destination, message.media, caption=message.text)

                    elif 'docs' in filter and message.document:
                        print(f'>>[INFO]{message.id}\n')
                        await client.send_file(destination, message.media, caption=message.text)

                    elif 'audios' in filter and message.audio:
                        print(f'>>[INFO]{message.id}\n')
                        await client.send_file(destination, message.media, caption=message.text)

                    elif 'links' in filter and message.text:
                        print(f'>>[INFO]{message.id}\n')
                        if 'http' in message.text or 'https' in message.text:
                            await client.send_message(destination, message.text)

                    elif 'messages' in filter and message.text:
                        print(f'>>[INFO]{message.id}\n')
                        await client.send_message(destination, message.text)

                except Exception as e:
                    print(f'>>[WARN]{message.id} {e}')

            return (True, 'OK')

        except Exception as e:
            print(f'>>[ERROR] {source} {e}')
            return (False, e)

        finally:
            print(f'\n>>[INFO] Process completed {source} {destination}')
            if client.is_connected():
                print(f'\n>>[END] Closed client {source} {destination}\n\n\n')
                await self.client.disconnect() # closed session

    # save locally
    async def toLocalSave(self, source, path_save, filter=[], limit=100):
        if self.client is None:
            return False, 'Client not initialized'

        if not path_save.strip():
            path_save = './saved_messages/'
        os.makedirs(path_save, exist_ok=True)

        try:
            client = self.client
            await client.start()

            source_entity = await client.get_entity(source)
            async for message in client.iter_messages(source_entity, reverse=True, limit=limit):
                await asyncio.sleep(0.85)
                try:
                    if 'images' in filter and message.photo:
                        os.makedirs(f'{path_save}/imgs/', exist_ok=True)
                        file_path = await message.download_media(file=f'{path_save}/imgs/')
                        print(f"Dowloaded Image: {file_path}")

                    elif 'videos' in filter and message.video:
                        os.makedirs(f'{path_save}/videos/', exist_ok=True)
                        file_path = await message.download_media(file=f'{path_save}/videos/')
                        print(f"Dowloaded Video: {file_path}")

                    elif 'docs' in filter and message.document:
                        os.makedirs(f'{path_save}/docs/', exist_ok=True)
                        file_path = await message.download_media(file=f'{path_save}/docs/')
                        print(f"Dowloaded Doc: {file_path}")

                    elif 'audios' in filter and message.audio:
                        os.makedirs(f'{path_save}/audio/', exist_ok=True)
                        file_path = await message.download_media(file=f'{path_save}/audio/')
                        print(f"Donwloaded Audio: {file_path}")

                    elif 'links' in filter and message.text:
                        if 'http' in message.text or 'https' in message.text:
                            sender = await client.get_entity(message.sender_id)
                            with open(f'{path_save}/links.txt', 'a', encoding='utf-8') as f:
                                sender_name = sender.first_name if sender.first_name else "Unknown"
                                f.write(f"{message.date} : Sender:({message.sender_id}|{sender_name}) Chat:{message.chat_id} : {message.text}\n")
                            print(f"Link included in saved message: {message.text}")

                    elif 'messages' in filter and message.text:
                        sender = await client.get_entity(message.sender_id)
                        with open(f'{path_save}/messages.txt', 'a', encoding='utf-8') as f:
                            sender_name = sender.first_name if sender.first_name else "Unknown"
                            f.write(f"{message.date} : Sender:({message.sender_id}|{sender_name}) Chat:{message.chat_id} : {message.text}\n")
                        print(f"Saved text message")
                except Exception as e:
                    print(f"Erro ao processar: {message.id} {e}")

            return (True, 'OK')

        except Exception as e:
            return (False, e)

        finally:
            if client.is_connected():
                await self.client.disconnect()



# Carbon works with a single session for each task.
# This way, every time you start a function it will start and end in the same task.

# In the Future i may implement the option of using a single session for more than one task.
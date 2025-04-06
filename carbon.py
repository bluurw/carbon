from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
import asyncio
import time
import os

import system

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
        print(f'\n\033[1;32m[INFO]\033[0m Starting forwarded cloning {source} {destination}')
        print(f'\n\033[1;32m[INFO]\033[0m Types {filter}')
        system.load_log(f'[INFO] Starting forwarded cloning {source} {destination}\n')
        system.load_log(f'[INFO] Types {filter}\n')
        if self.client is None:
            print(f'\n\033[1;31m[WARN]\033[0m Client not initialized')
            system.load_log(f'[WARN] Client not initialized\n')
            return False, 'Client not initialized'
        try:
            client = self.client
            if not client.is_connected():
                await client.start() # wait started client
            print(f'\n\033[1;32m[START]\033[0m Client initialized')
            system.load_log(f'[START] Client initialized\n')

            source_entity = await client.get_entity(source)
            async for message in client.iter_messages(source_entity, reverse=True, limit=limit):
                print(f'\033[1;33m[INFO]\033[0m Content: {message.id} {message.entities}')
                system.load_log(f'[INFO] Content: {message.id} {message.entities}\n')
                try:
                    await asyncio.sleep(0.85) # wait
                    if 'images' in filter and message.photo:
                        print(f'\033[1;33m[INFO]\033[0m image {message.id}\n')
                        system.load_log(f'[INFO] image {message.id}\n')
                        await client.send_file(destination, message.media, caption=message.text)

                    elif 'videos' in filter and message.video:
                        print(f'\033[1;33m[INFO]\033[0m video {message.id}\n')
                        system.load_log(f'[INFO] video {message.id}\n')
                        await client.send_file(destination, message.media, caption=message.text)

                    elif 'docs' in filter and message.document:
                        print(f'\033[1;33m[INFO]\033[0m doc {message.id}\n')
                        system.load_log(f'[INFO] doc {message.id}\n')
                        await client.send_file(destination, message.media, caption=message.text)

                    elif 'audios' in filter and message.audio:
                        print(f'\033[1;33m[INFO]\033[0m audio {message.id}\n')
                        system.load_log(f'[INFO] audio {message.id}\n')
                        await client.send_file(destination, message.media, caption=message.text)

                    elif 'links' in filter and message.text:
                        if 'http' in message.text or 'https' in message.text:
                            print(f'\033[1;33m[INFO]\033[0m link {message.id}\n')
                            system.load_log(f'[INFO] link {message.id}\n')
                            await client.send_message(destination, message.text)

                    elif 'messages' in filter and message.text:
                        print(f'\033[1;33m[INFO]\033[0m message {message.id}\n')
                        system.load_log(f'[INFO] message {message.id}\n')
                        await client.send_message(destination, message.text)
                except Exception as e:
                    print(f'\033[1;31m[WARN]\033[0m {message.id} {e}\n')
                    system.load_log(f'[WARN] {message.id} {e}\n')

            print(f'\n\033[1;33m[INFO]\033[0m Process completed\n')
            system.load_log(f'[INFO] Process completed\n')
            return (True, 'OK')

        except Exception as e:
            print(f'\033[1;31m[WARN]\033[0m {source} {e}\n')
            system.load_log(f'[WARN] Process not completed {source} {e}\n')
            return (False, e)

        finally:
            print(f'\n\033[1;33m[INFO]\033[0m Finally {source} {destination}\n')
            system.load_log(f'[INFO] Finally {source} {destination}\n')
            if client.is_connected():
                print(f'\n\033[1;32m[END]\033[0m Closed client\n\n\n')
                system.load_log(f'[END] Closed client\n\n\n')
                await asyncio.sleep(1.5) # wait
                await self.client.disconnect() # closed session

    # save locally
    async def toLocalSave(self, source, path_save, filter=[], limit=None):
        print(f'\n\033[1;32m[INFO]\033[0m Starting forwarded cloning {source} {path_save}')
        print(f'\n\033[1;32m[INFO]\033[0m Types {filter}')
        system.load_log(f'[INFO] Starting forwarded cloning {source} {path_save}\n')
        system.load_log(f'[INFO] Types {filter}\n')
        if self.client is None:
            print(f'\n\033[1;31m[WARN]\033[0m Client not initialized')
            system.load_log(f'[WARN] Client not initialized\n')
            return False, 'Client not initialized'

        if not path_save.strip():
            path_save = './saved_messages/'
        os.makedirs(path_save, exist_ok=True)
        print(f'\n\033[1;32m[INFO]\033[0m Folder created {path_save}')
        system.load_log(f'[INFO] Folder created {path_save}\n')

        try:
            client = self.client
            if not client.is_connected():
                await client.start() # wait started client
            print(f'\n\033[1;32m[START]\033[0m Client initialized')
            system.load_log(f'[START] Client initialized\n')

            source_entity = await client.get_entity(source)
            async for message in client.iter_messages(source_entity, reverse=True, limit=limit):
                print(f'\033[1;33m[INFO]\033[0m Content: {message.id} {message.entities}')
                system.load_log(f'[INFO] Content: {message.id} {message.entities}\n')
                try:
                    await asyncio.sleep(0.85)
                    if 'images' in filter and message.photo:
                        os.makedirs(f'{path_save}/imgs/', exist_ok=True) # if exists
                        file_path = await message.download_media(file=f'{path_save}/imgs/')
                        print(f'\033[1;33m[INFO]\033[0m image saved {message.id} {file_path}\n')
                        system.load_log(f'[INFO] image saved {message.id} {file_path}\n')

                    elif 'videos' in filter and message.video:
                        os.makedirs(f'{path_save}/videos/', exist_ok=True)
                        file_path = await message.download_media(file=f'{path_save}/videos/')
                        print(f'\033[1;33m[INFO]\033[0m video saved {message.id} {file_path}\n')
                        system.load_log(f'[INFO] video saved {message.id} {file_path}\n')

                    elif 'docs' in filter and message.document:
                        os.makedirs(f'{path_save}/docs/', exist_ok=True)
                        file_path = await message.download_media(file=f'{path_save}/docs/')
                        print(f'\033[1;33m[INFO]\033[0m doc saved {message.id} {file_path}\n')
                        system.load_log(f'[INFO] doc saved {message.id} {file_path}\n')

                    elif 'audios' in filter and message.audio:
                        os.makedirs(f'{path_save}/audios/', exist_ok=True)
                        file_path = await message.download_media(file=f'{path_save}/audio/')
                        print(f'\033[1;33m[INFO]\033[0m audio saved {message.id} {file_path}\n')
                        system.load_log(f'[INFO] audio saved {message.id} {file_path}\n')

                    elif 'links' in filter and message.text:
                        if 'http' in message.text or 'https' in message.text:
                            sender = await client.get_entity(message.sender_id)
                            with open(f'{path_save}/links.txt', 'a', encoding='utf-8') as f:
                                sender_name = sender.first_name if sender.first_name else "Unknown"
                                f.write(f"{message.date} : Sender:({message.sender_id}|{sender_name}) Chat:{message.chat_id} : {message.text}\n")
                            print(f'\033[1;33m[INFO]\033[0m link saved {message.id} {file_path}\n')
                            system.load_log(f'[INFO] link saved {message.id} {file_path}\n')

                    elif 'messages' in filter and message.text:
                        sender = await client.get_entity(message.sender_id)
                        with open(f'{path_save}/messages.txt', 'a', encoding='utf-8') as f:
                            sender_name = sender.first_name if sender.first_name else "Unknown"
                            f.write(f"{message.date} : Sender:({message.sender_id}|{sender_name}) Chat:{message.chat_id} : {message.text}\n")
                        print(f'\033[1;33m[INFO]\033[0m message saved {message.id} {file_path}\n')
                        system.load_log(f'[INFO] message saved {message.id} {file_path}\n')
                except Exception as e:
                    print(f'\033[1;31m[WARN]\033[0m {message.id} {e}')
                    system.load_log(f'[WARN] {message.id} {e}\n')

            print(f'\n\033[1;33m[INFO]\033[0m Process completed')
            system.load_log(f'[INFO] Process completed\n')
            return (True, 'OK')

        except Exception as e:
            print(f'\033[1;31m[WARN]\033[0m {source} {e}')
            system.load_log(f'[WARN] Process not completed {source} {e}\n')
            return (False, e)

        finally:
            print(f'\n\033[1;33m[INFO]\033[0m Finally {source} {path_save}\n')
            system.load_log(f'[INFO] Finally {source} {path_save}\n')
            if client.is_connected():
                print(f'\n\033[1;32m[END]\033[0m Closed client\n\n\n')
                system.load_log(f'[END] Closed client\n\n\n')
                await asyncio.sleep(1.5) # wait
                await self.client.disconnect() # closed session



# Carbon works with a single session for each task.
# This way, every time you start a function it will start and end in the same task.

# In the Future i may implement the option of using a single session for more than one task.
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
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
    async def toFoward(self, source, destination, filter=[], limit=100):
        if self.client is None:
            return False, 'Client not initialized'
            
        try:
            client = self.client
            await client.start()
            
            source_entity = await client.get_entity(source)
            async for message in client.iter_messages(source_entity, limit=limit):
                if 'images' in filter and message.photo:
                    print(message)
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

            return True
        
        except Exception as e:
            return False, f"Failed to copy msgs: {e}"
        
        finally:
            await self.client.disconnect()
    
    # save locally
    async def toLocalSave(self, source, path_save, filter=[], limit=100):
        if self.client is None:
            return False, 'Client not initialized'
        
        if path_save == '' or path_save == ' ':
            path_save = 't.me/'
            os.makedirs(path_save, exist_ok=True)
        else:
            os.makedirs(path_save, exist_ok=True)

        try:
            client = self.client
            await client.start()

            source_entity = await client.get_entity(source)
            async for message in client.iter_messages(source_entity, limit=limit):
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
                        sender_id = await client.get_entity(message.sender_id)  # id remetente
                        with open(f'{path_save}/links.txt', 'a', encoding='utf-8') as f:
                            try:
                                sender_name = sender.first_name if sender.first_name else "Unknown"
                                f.write(f"{message.date} : Sender:({message.sender_id}|{sender_name}) Chat:{message.chat_id} : {message.text}\n")
                            except:
                                f.write(f"{message.date} : Sender:{message.sender_id} Chat:{message.chat_id} : {message.text}\n")    
                        print(f"Link included in saved message: {message.text}")

                elif 'messages' in filter and message.text:
                    sender_id = await client.get_entity(message.sender_id)  # id remetente
                    with open(f'{path_save}/messages.txt', 'a', encoding='utf-8') as f:
                        try:
                            sender_name = sender.first_name if sender.first_name else "Unknown"
                            f.write(f"{message.date} : Sender:({message.sender_id}|{sender_name}) Chat:{message.chat_id} : {message.text}\n")
                        except:
                            f.write(f"{message.date} : Sender:{message.sender_id} Chat:{message.chat_id} : {message.text}\n")
                    print(f"Saved text message")
                
            return True

        except Exception as e:
            return False, f"Failed to copy msgs: {e}"
        
        finally:
            await self.client.disconnect() # end the session


# Carbon works with a single session for each task.
# This way, every time you start a function it will start and end in the same task.

# In the Future i may implement the option of using a single session for more than one task.
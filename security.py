import os
from dotenv import load_dotenv
from pathlib import Path

def load_credentials():
    try:
        dotenv_path = Path('./credentials.env') # serach for file credentials
        for key in ["API_ID", "API_HASH"]:
            if key in os.environ: # cache delete
                del os.environ[key]
        load_dotenv(dotenv_path=dotenv_path) # load file credentials
        API_ID = os.getenv("API_ID")
        API_HASH = os.getenv("API_HASH")
        return API_ID, API_HASH
    except Exception as err:
        return 0

def create_credentials(API_ID, API_HASH):
    env_file = Path('credentials.env')
    if env_file.exists(): # if exists
        env_file.unlink() # delete
    try:
        if len(API_ID) == 0 or len(API_HASH) == 0:
            return 0
        else:
            with open(env_file, 'a') as file:
                file.write(f'API_ID={API_ID}\n') # write ID
                file.write(f'API_HASH={API_HASH}\n') # write HASH
                return 1
    except Exception as err:
        return 0
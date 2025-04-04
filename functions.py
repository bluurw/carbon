import os
from dotenv import load_dotenv
from pathlib import Path

def load_credentials():
    try:
        dotenv_path = Path('./credentials.env')
        load_dotenv(dotenv_path=dotenv_path)
        API_ID = os.getenv("API_ID")
        API_HASH = os.getenv("API_HASH")
        if len(API_ID) == 0 or len(API_HASH) == 0:
            return 0
        else:
            return API_ID, API_HASH
    except Exception as err:
        return 0

def create_credentials(API_ID, API_HASH):
    try:
        if len(API_ID) == 0 or len(API_HASH) == 0:
            return 0
        else:
            with open('credentials.env', 'w') as file:
                file.write(f'API_ID={API_ID}\n')
                file.write(f'API_HASH={API_HASH}\n')
                return 1
    except Exception as err:
        return 0
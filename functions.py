import os
from dotenv import load_dotenv

def load_credentials():
    try:
        load_dotenv()
        API_ID = os.getenv("API_ID")
        API_HASH = os.getenv("API_HASH")
        return API_ID, API_HASH
    except Exception as err:
        return 0

def create_credentials(API_ID, API_HASH):
    try:
        with open('credentials.env', 'w') as file:
            file.write(f'API_ID={API_ID}\n')
            file.write(f'API_HASH={API_HASH}\n')
            return 1
    except Exception as err:
        return 0
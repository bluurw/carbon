import os
from pathlib import Path
from datetime import datetime

def load_log(log:str, log_path='log.txt'):
    try:
        with open(log_path, 'a') as file:
            date_time_local = datetime.now()
            file.write(f'{date_time_local.strftime("%Y-%m-%d %H:%M:%S")} {log} \n')
            return 1
    except Exception as err:
        return 0
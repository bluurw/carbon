import time

import banners
import panels

# banner for negative credentials test result
def error_credentials():
    banners.carbon_banner_bluured()
    print('> The parakeets invalidate your key.')
    print('> Create valid credencials, or correct existing ones.')
    time.sleep(1.0)
    input('\n...PRESS ANY KEY...')

# filter
def get_filters():
    panels.filter_itens_panel()
    filter_map = ["messages", "images", "videos", "audios", "docs", "links", "stickers"] # types
    filter_input = input('> Enter the number of types you want to filter (no space): ')
    return [filter_map[int(i)] for i in filter_input if i.isdigit() and int(i) < len(filter_map)]
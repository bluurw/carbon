import os
import time

from carbon import Carbon
import functions
import banners
import panels

def error_credentials():
    banners.carbon_banner_bluured()
    print('> The parakeets invalidate your key.')
    print('> Create valid credencials, or correct existing ones.')
    time.sleep(1.0)
    input('\n...PRESS ANY KEY...')

while True:
    #IMPLANTAR TRY
    #ValueError
    banners.carbon_banner_bluured()
    panels.options_panel()
    choose_option = int(input('> Enter chosen option: '))
    
    if choose_option == 1:
        while True:
            banners.carbon_banner_bluured()
            panels.options_clone_panel()
            choose_option_save_clone = int(input('> Enter chosen option: '))
            
            if choose_option_save_clone == 1:

                credentials = functions.load_credentials()
            
                if credentials == 0:
                    error_credentials()

                else:
                    banners.carbon_banner_bluured()
                    print('\033[1mC\033[0mLONAR_\033[1mC\033[0mANAL - SAVE_FOWARD \n')
                    source_input = str(input(f'> Source Group: t.me/'))
                    destination_input = str(input(f'> Destination Group: t.me/'))
                    SOURCE = f"t.me/{source_input}" 
                    DESTINATION = f"t.me/{destination_input}"

                    panels.filter_itens_panel()
                    filter_itens_input = list(input('> Insira o numero de cada opcao que deseja filtrar: '))
                    filters = ["messages", "images", "videos", "audios", "docs", "links"]
                    filter = [filters[int(i)] for i in filter_itens_input]

                    Carbon = Carbon(credentials[0], credentials[1])
                    Carbon.client.loop.run_until_complete(Carbon.toFoward(SOURCE, DESTINATION, filter=filter))
                
            elif choose_option_save_clone == 2:

                credentials = functions.load_credentials()

                if credentials == 0:
                    error_credentials()
                
                else:
                    banners.carbon_banner_bluured()
                    print('\033[1mC\033[0mLONAR_\033[1mC\033[0mANAL - SAVE_LOCAL \n')
                    source_input = str(input(f'> Source Group: t.me/'))
                    SOURCE = f"t.me/{source_input}" # INSIRA SOMENTE O NOME t.me/Nome
                    DESTINATION = str(input(f'> Local Save: '))
                    
                    panels.filter_itens_panel()
                    filter_itens_input = list(input('> Insira o numero de cada opcao que deseja filtrar: '))
                    filters = ["messages", "images", "videos", "audios", "docs", "links"]
                    filter = [filters[int(i)] for i in filter_itens_input]

                    Carbon.client.loop.run_until_complete(Carbon.toLocalSave(SOURCE, path_save=DESTINATION, filter=filter))
                
            elif choose_option_save_clone == 3:

                credentials = functions.load_credentials()

                if credentials == 0:
                    error_credentials()
                    
                else:
                    banners.carbon_banner_bluured()
                    print('Ainda em desenvolvimento')
                    time.sleep(1.0)
                    input('\n...PRESS ANY KEY...')
                
            elif choose_option_save_clone == 0:
                break
                
            else:
                continue

    elif choose_option == 2:
        while True:
            banners.carbon_banner_bluured()
            panels.credentials_panel()
            choose_option_credentials = int(input('> Enter chosen option: '))

            if choose_option_credentials == 1:
                banners.carbon_banner_bluured()
                print('\033[1mC\033[0mONFIG_API_\033[1mC\033[0mREDENTIALS \n')
                input_api_id = str(input('> Digite o ID da API: '))
                input_api_hash = str(input('> Digite a HASH da API: '))
                create_credential = functions.create_credentials(input_api_id, input_api_hash)
                if create_credential == 1:
                    time.sleep(1.5)
                    print('\n> Sucess creating file with credentials')
                    time.sleep(1.0)
                    input('\n...PRESS ANY KEY...')
                elif create_credential == 0:
                    time.sleep(1.5)
                    print('\n> Failed to create file with credentials')
                    time.sleep(1.0)
                    input('\n...PRESS ANY KEY...')

            elif choose_option_credentials == 2:
                banners.carbon_banner_bluured()
                print('\033[1mC\033[0mREDENTIALS \n')
                credentials = functions.load_credentials()
                print(f'API_ID: {credentials[0]} \nAPI_HASH: {credentials[1]} \n')
                time.sleep(2.5)
                input('...PRESS ANY KEY...')
            elif choose_option_credentials == 0:
                break
            else:
                banners.carbon_banner_bluured()
                continue

    elif choose_option == 3:
        banners.carbon_banner_bluured()
        panels.about_me()
        time.sleep(5)
        input('...PRESS ANY KEY...')
    
    elif choose_option == 0:
        os.system('clear')
        break
   
    else:
        continue
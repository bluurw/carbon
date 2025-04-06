import os
import time
import asyncio

from carbon import Carbon
import functions
import banners
import panels
import security
import system


while True:
    #IMPLANTAR TRY
    #ValueError
    
    banners.random_banner()
    panels.options_panel()
    choose_option = int(input('> Enter chosen option: '))
    
    if choose_option == 1:
        while True:
            banners.random_banner()
            panels.options_clone_panel()
            choose_option_save_clone = int(input('> Enter chosen option: '))
            
            if choose_option_save_clone == 1:
                while True:
                    credentials = security.load_credentials()
                    carbon_instance = Carbon(credentials[0], credentials[1])

                    # credential test 
                    test_credential = carbon_instance.start_client()

                    if test_credential:
                        banners.random_banner()
                        print('\033[1mC\033[0mLONE_\033[1mC\033[0mHANNEL - SAVE_FOWARD \n')
                        SOURCE = str(input(f'> Source Group (link or ID): t.me/'))
                        DESTINATION = str(input(f'> Destination Group (link or ID): t.me/'))

                        if not source_input.isnumeric():
                            SOURCE = f"t.me/{SOURCE}"
                            DESTINATION = f"t.me/{DESTINATION}"

                        filter = functions.get_filters()
                        carbon_instance.client.loop.run_until_complete(carbon_instance.toFoward(SOURCE, DESTINATION, filter=filter))
                        break
                    
                    else:
                        functions.error_credentials()
                        break

            elif choose_option_save_clone == 2:
                while True:
                    credentials = security.load_credentials()
                    carbon_instance = Carbon(credentials[0], credentials[1])

                    # credential test 
                    test_credential = carbon_instance.start_client()

                    if test_credential:
                        banners.random_banner()
                        print('\033[1mC\033[0mLONE_\033[1mC\033[0mHANNEL - SAVE_LOCAL \n')
                        source_input = str(input(f'> Source Group: t.me/'))
                        SOURCE = f"t.me/{source_input}" # t.me/Nome
                        DESTINATION = str(input(f'> Local Save: '))

                        if not source_input.isnumeric():
                            SOURCE = f"t.me/{SOURCE}"
                            DESTINATION = f"t.me/{DESTINATION}"

                        if DESTINATION == '' or DESTINATION == ' ':
                            DESTINATION = SOURCE
                    
                        filter = functions.get_filters()
                        carbon_instance.client.loop.run_until_complete(carbon_instance.toLocalSave(SOURCE, path_save=DESTINATION, filter=filter))
                        break
                
                    else:
                        functions.error_credentials()
                        break
                
            elif choose_option_save_clone == 3:

                credentials = security.load_credentials()

                if credentials == 0:
                    functions.error_credentials()
                    break
                else:
                    banners.random_banner()
                    print('Still in development')
                    time.sleep(1.0)
                    input('\n...PRESS ANY KEY...')
                
            elif choose_option_save_clone == 0:
                break
                
            else:
                continue

    elif choose_option == 2:
        while True:
            banners.random_banner()
            panels.credentials_panel()
            choose_option_credentials = int(input('> Enter chosen option: '))

            if choose_option_credentials == 1:
                banners.random_banner()
                print('\033[1mC\033[0mONFIG_API_\033[1mC\033[0mREDENTIALS \n')
                input_api_id = str(input('> Enter API ID: '))
                input_api_hash = str(input('> Enter API HASH: '))
                create_credential = security.create_credentials(input_api_id, input_api_hash)
                if create_credential == 1:
                    security.load_credentials()
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
                banners.random_banner()
                print('\033[1mC\033[0mREDENTIALS \n')
                credentials = security.load_credentials()
                print(f'API_ID: {credentials[0]} \nAPI_HASH: {credentials[1]} \n')
                time.sleep(2.5)
                input('...PRESS ANY KEY...')
            elif choose_option_credentials == 0:
                break
            else:
                banners.random_banner()
                continue

    elif choose_option == 3:
        banners.random_banner()
        panels.about_me()
        time.sleep(5)
        input('...PRESS ANY KEY...')
    
    elif choose_option == 0:
        os.system('clear')
        break

    else:
        continue
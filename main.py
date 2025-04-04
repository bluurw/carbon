import os
import time

from carbon import Carbon
import functions
import banners
import panels

credentials = functions.load_credentials()
Carbon = Carbon(credentials[0], credentials[1])

while True:
    banners.carbon_banner_bluured()
    panels.options_panel()
    choose_option = int(input('Enter chosen option: '))
    
    if choose_option == 1:
        
        banners.carbon_banner_bluured()
        panels.options_clone_panel()
        choose_option_save_clone = int(input('Enter chosen option: '))
        
        if choose_option_save_clone == 1:
            banners.carbon_banner_bluured()
            print('\033[1mC\033[0mLONAR_\033[1mC\033[0mANAL - SAVE_FOWARD')
            source_input = str(input(f'SOURCE GROUP: t.me/'))
            destination_input = str(input(f'DESTINATION GROUP: t.me/'))
            SOURCE = f"t.me/{source_input}" 
            DESTINATION = f"t.me/{destination_input}"

            panels.filter_itens_panel()
            filter_itens_input = list(input('Insira o numero de cada opcao que deseja filtrar: '))
            filters = ["messages", "images", "videos", "audios", "docs", "links"]
            filter = [filters[int(i)] for i in filter_itens_input]

            Carbon.client.loop.run_until_complete(Carbon.toFoward(SOURCE, DESTINATION, filter=filter))
            
        elif choose_option_save_clone == 2:
            banners.carbon_banner_bluured()
            print('\033[1mC\033[0mLONAR_\033[1mC\033[0mANAL - SAVE_LOCAL')
            source_input = str(input(f'SOURCE GROUP: t.me/'))
            path_save_input = str(input(f'LOCAL SAVE: '))
            SOURCE = f"t.me/{source_input}" # INSIRA SOMENTE O NOME t.me/Nome
                
            panels.filter_itens_panel()
            filter_itens_input = list(input('Insira o numero de cada opcao que deseja filtrar: '))
            filters = ["messages", "images", "videos", "audios", "docs", "links"]
            filter = [filters[int(i)] for i in filter_itens_input]

            Carbon.client.loop.run_until_complete(Carbon.toLocalSave(SOURCE, path_save=path_save_input, filter=filter))
            
        elif choose_option_save_clone == 3:
            print('Ainda em desenvolvimento')
            
        elif choose_option_save_clone == 0:
            break
            
        else:
            banners.carbon_banner_bluured()
            input_clone_save_foward_panel()

    elif choose_option == 2:
        while True:
            banners.carbon_banner_bluured()
            credentials_panel()
            choose_option_credentials = int(input('DIGITE UMA DAS OPCOES: '))

            if choose_option_credentials == 1:
                banners.carbon_banner_bluured()
                print('\033[1mC\033[0mONFIG_API_\033[1mC\033[0mREDENTIALS')
                input_api_id = str(input('Digite o ID da API: '))
                input_api_hash = str(input('Digite a HASH da API: '))
                create_credentials(input_api_id, input_api_hash)
                if create_credentials == 1:
                    print('Arquivo de credenciais criado com sucesso')
                    input('Pressione qualquer tecla para voltar ao menu')
                elif create_credentials == 0:
                    print('Erro ao criar arquivo de credenciais')

            elif choose_option_credentials == 2:
                banners.carbon_banner_bluured()
                print('\033[1mC\033[0mREDENTIALS')
                credentials = functions.load_credentials()
                print(f'API_ID: {credentials[0]} \nAPI_HASH: {credentials[1]}')
                time.sleep(5)
                input('PRESS ANY KEY')
            elif choose_option_credentials == 0:
                break
            else:
                banners.carbon_banner_bluured()
                continue

    elif choose_option == 3:
        banners.carbon_banner_bluured()
        about_me()
        input()
    
    elif choose_option == 0:
        os.system('exit')
   
    else:
        banners.carbon_banner_bluured()
        continue
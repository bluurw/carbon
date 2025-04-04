from carbon import Carbon
import os

import banners
import panels

# Criar um arquivo para guardar estas configuracoes
API_ID =   #API ID
API_HASH = "" #API Hash
Carbon = Carbon(API_ID, API_HASH)

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
            source_input = str(input(f'INSIRA O NOME DO GRUPO ORIGEM: t.me/')) # INSIRA SOMENTE O NOME t.me/Nome
            destination_input = str(input(f'INSIRA O NOME DO GRUPO DESTINO: t.me/')) # INSIRA SOMENTE O NOME t.me/Nome
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
            source_input = str(input(f'INSIRA O NOME DO GRUPO ORIGEM: t.me/'))
            SOURCE = f"t.me/{source_input}" # INSIRA SOMENTE O NOME t.me/Nome
                
            panels.filter_itens_panel()
            filter_itens_input = list(input('Insira o numero de cada opcao que deseja filtrar: '))
            filters = ["messages", "images", "videos", "audios", "docs", "links"]
            filter = [filters[int(i)] for i in filter_itens_input]

            Carbon.client.loop.run_until_complete(Carbon.toLocalSave(SOURCE, filter=filter))
            
        elif choose_option_save_clone == 3:
            print('Ainda em desenvolvimento')
            
        elif choose_option_save_clone == 0:
            break
            
        else:
            banners.carbon_banner_bluured()
            input_clone_save_foward_panel()

    elif choose_option == 2:
        print('Arquivo de configuracao')
        #Remover arquivo existente
        #Criar novo arquivo
    
    elif choose_option == 3:
        banners.carbon_banner_bluured()
        about_me()
        input()
    
    elif choose_option == 0:
        os.system('exit')
   
    else:
        banners.carbon_banner_bluured()
        options_panel()


# +5511998765432
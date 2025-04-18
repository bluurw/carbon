[![License](https://img.shields.io/badge/license-MIT-_red.svg)](https://opensource.org/licenses/MIT)
[![Contribuitions Welcome](https://img.shields.io/badge/contribuitions-welcome-brightgreen.svg?style=flat)](https://github.com/bluurw/carbon/issues)

     ▄▄·  ▄▄▄· ▄▄▄  ▄▄▄▄·        ▐ ▄ 
    ▐█ ▌▪▐█ ▀█ ▀▄ █·▐█ ▀█▪ ▄█▀▄ •█▌▐█
    ██ ▄▄▄█▀▀█ ▐▀▀▄ ▐█▀▀█▄▐█▌.▐▌▐█▐▐▌
    ▐███▌▐█▪ ▐▌▐█•█▌██▄▪▐█▐█▌.▐▌██▐█▌
    ·▀▀▀  ▀  ▀ .▀  ▀·▀▀▀▀  ▀█▄▀▪▀▀ █▪


# **Carbon (Carbono)**

![Python Version](https://img.shields.io/badge/Python-3.11-blue)  
![Linux Support](https://img.shields.io/badge/Linux-Compatible-green)

## **Razão**
O projeto Carbon, ou Carbono, tem o nome derivado das folhas de carbono que servem para fazer cópias.  
Desta maneira, o foco do projeto está em copiar informações de grupos do Telegram, antes que eles sejam extintos.

Atualmente, a moderação do Telegram está banindo muitos canais, alguns sem qualquer motivo, outros por má conduta.  
![alt text](/imgs/telgram_moderation_overview_graphic.png)  
[Mais informações sobre moderação do Telegram](https://telegram.org/moderation)

## **Funcionamento**
![alt text](/imgs/Carbon.png)


### Passo 1: Clone ou faca o download do Repositorio
```bash
git clone https://github.com/bluurw/Carbon
```

### Passo 2: Certifique-se de instalar todas as bibliotecas e dependências
*Isto funcionará melhor em um ambiente virtual

```bash
python -m venv "carbon"  
source /bin/activate  
pip install -r requeriments.txt
```

### Passo 3: Obtenha uma credencial de API no Telegram
Se ainda não possui ou não sabe como obtê-la, siga este link: [API Telegram](https://my.telegram.org/apps "Telegram")


### Passo 4: Executar o Projeto
Com o ambiente preparado, execute o arquivo `main.py`:  
```bash
python main.py
```

### Passo 5: Configurar Credenciais no Menu
No menu do *Carbon*, selecione a opção *[2] OPTIONS* e configure suas credenciais da API do Telegram.
Após configurar, você poderá utilizar as funcionalidades livremente!


## **Linha do Tempo**

- **Conceito:** 27/03/2025  
- **Primeira Versão (1.v):** 04/04/2025  
- **Atualização 1:** 05/04/2025
  - Correção de bugs & atualização da interface.
- **Atualização 2:** 05/04/2025
  - Correção de bugs & atualização da interface; e
  - Implantação de arquivo de log.
- **Atualização 3:** 07/04/2025
  - Correção de bugs & atualização da interface;
  - Inserido o modo sem filtros, e stickers no Carbon; e
  - Inserido no painels nova opção.


## **Próximas Atualizações**

- **Integração com GitHub**:
  Permitir que o usuário clone o conteúdo de um grupo diretamente para um repositório do GitHub.
- **Compactação de Dados**:  
  Melhorar o processo de compactação, tanto para o salvamento local quanto para a clonagem no GitHub.
- **Criação de Grupos**:  
  Permite criar grupos automaticamente via API do Telegram, facilitando a organização e o gerenciamento de comunidades.
- **Re-clonagem Sequencial**:
  Permitir a clonagem contínua do mesmo grupo a partir da última mensagem clonada, evitando repetições desnecessárias.
- **Tratamento do Erro de Tempo de Espera** [URGENTE]:
  Corrigir o problema em que o encaminhamento de muitas mensagens gera uma solicitação de tempo de espera, que atualmente é interpretada como erro.

## **Compatibilidade**

![Linux Support](https://img.shields.io/badge/Linux-OK-green)  
![Windows Support](https://img.shields.io/badge/Windows-Não%20Testado-yellow)  
![Mac Support](https://img.shields.io/badge/Mac-Não%20Testado-yellow)  

- **Linux:** OK  
- **Windows:** Não testado  
- **Mac:** Não testado
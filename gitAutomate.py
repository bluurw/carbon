import os

class Git:
    def __init__(self, clone_name, user, password, name_repository):
        self.clone_name = clone_name
        self.user = user
        self.password = password
        self.name_repository = f'https://github.com/{user}/{name_repository}.git'
    
    def gitInit():
        git_version = os.system('git --version')
        if 'git' not in git_version:
            print('Necessario ter o git instalado')
        else:
            os.system('git init')
            print('Repositorio incializado')
    
    # Sera um arquivo de nome padrao zipado
    def gitAdd(file_path:str):
        os.system(f'git add {file_path}')
        print('adicionado')
    
    def gitCommit(file_path:str, comment:str=" "):
        comment = comment
        if len(comment) == 0:
            comment = 'arquivo clone'
        os.system(f'git commit -m {comment}')
    
    def gitRemoteAdd(self):
        os.system(f'git remote add origin {self.name_repository}')
    
    def gitPush():
        os.system(f'git push -u origin master')
    

    #os.remove(path_file)
    #o arquivo devera ser removido do ambiente local

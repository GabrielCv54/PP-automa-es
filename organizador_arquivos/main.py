import os
from loguru import logger
import psutil
import time

#print(os.listdir('.'))


def list_all_directorys():
    all_files = os.system('dir')
    print(all_files)

def create_new_folder():
    try:
        dir_path = os.getcwd()
        name_folder = str(input("Qual nome do diretório ?:"))
        type_files_folder = str(input("Qual o tipo de arquivos que deseja guardar ")).lower()
        if os.path.exists(f'{name_folder}'):
            logger.error("Esse diretório já existe e não é possível cria-lo novamente!!")
        elif not os.listdir(dir_path):
            logger.info("Seu diretório está vazio, não arquivos para serem analisados! ")
        else:
            os.system(f"if not exist {name_folder} mkdir {name_folder}")
            os.system(f"move *.{type_files_folder} {name_folder}\ ")
            os.system(f"echo Pasta {name_folder} criada!!")
            logger.success(f"Seu diretório '{name_folder}' foi criado com sucesso!")
    except Exception as erro:
        logger.error(f"Ocorreu um erro durante a criação do diretório e dos arquivos: {erro} !")
    

def create_new_file():
    file = str(input("Qual o nome do arquivo que deseja criar?: "))
    os.system(f"echo Texto inicial & > {file}.txt")
    question = str(input("Deseja mexer no arquivo ou não? ")).lower()
    if question == 's':
        content = str(input("o que deseja escrever sobre o arquivo?: "))
        os.system(f'start {file}')
        time.sleep(5)
        os.system(f"{content}")
    
    elif question == 'n':
        os.system('exit')

def show_files_of_specific_folder():
    try:
        organization_files_path = os.getcwd()
        type_file = str(input("Qual pasta deseja ver?: "))
        os.chdir(f'{organization_files_path}\{type_file}')
        os.system('dir')
    except Exception as error:
        logger.error(f"Erro ao tentar mostrar o diretório: {error}")


def edit_folder():
    try:
        org_files_path = os.getcwd()
        folder_name = str(input("Em qual pasta você deseja mexer?: "))
        os.chdir(f"{org_files_path}\{folder_name}")
        file = str(input("Qual arquivo deseja editar?: "))
        os.system(f'start {file}')
        logger.success("Arquivo salvo com sucesso!!")
    except Exception as error:
        logger.error(f"Ocorreu um erro durante a edição deste arquivo: {error}")

def exclude_folder():
    try:
        folder_exclude = str(input("Em qual pasta está o arquivo?: "))
        os.chdir(f"{os.getcwd()}\{folder_exclude}")
        file_exclude = str(input("qual o arquivo você deseja excluir?: "))
        os.system(f"del {file_exclude}")
        logger.success(f"Arquivo {file_exclude} com sucesso!")
    except Exception as erro:
        logger.error(f"Ocorreu um erro ao tentar deletar: {erro}")

def register_user_in_system():
    try:
        users_txt = 'users.txt'
        username = str(input("Qual o seu username?: "))
        password = str(input("Qual a sua senha?: "))
        if os.path.exists(f"{os.getcwd()}\{users_txt}"):
            os.system(f"echo Username:{username}  Senha: {password} >> users.txt")
            logger.success(f"Arquivo users.txt atualizado com sucesso!!")
        else:
            os.system(f"echo Username:{username} Senha:{password}  > users.txt")
            logger.success("users.txt criado com sucesso!!")
        #os.system(f"exit")
    except Exception as erro:
        logger.error(f"Erro : {erro}")

def show_systeminfo():
    print("="*30 +"Configurações do sistema "+"="*30)
    system_info = os.system("systeminfo")
    print(system_info)

def show_hardware_info():
    ram_memory = psutil.virtual_memory()
    disk = psutil.disk_usage('.')
    print("*"*30+" Memória RAM "+"*"*30)
    logger.info(f"Porcentagem da RAM: {ram_memory.percent}%")
    logger.info(f"Memória disponível para uso: {ram_memory.available}")
    logger.info(f"Usada : {ram_memory.used / (1024**3):.2f} GB")
    logger.info(f"Total: {ram_memory.total / (1024**3):.2f} GB")
    print('*'*30+" Disco "+"*"*30)
    logger.info(f"Total: {disk.total /  (1024**3):.2f} GB")
    logger.info(f"Uso do disco: {disk.used / (1024**3):.2f} GB")
    logger.info(f"Livre: {disk.free / (1024**3):.2f} GB")
    logger.info(F"Porcentagem :  {disk.percent}%")

def main():
    while True:
        print("0- Encerrar terminal\n"
              "1- Mostrar todos os diretórios\n"
              '2- Criar um novo diretório\n'
              "3- Mostrar um diretório específico\n"
              "4- Editar um diretório\n"
              "5- Excluir diretório\n"
              "6- Registrar usuário no arquivo txt users\n"
              "7- Mostrar informações do sistema\n"
              "8- Mostrar informações do Hardware(Disco e RAM)\n")
        functions = int(input("Qual ação deseja executar?: "))
       
        path_ = os.getcwd()
        print(f"Caminho do projeto: {path_}")
        if functions == 1:
            list_all_directorys()
        elif functions == 2:
            create_new_folder()
        elif functions == 3:
            show_files_of_specific_folder()
        elif functions == 4:
            edit_folder()
        elif functions == 5:
            exclude_folder()
        elif functions == 6:
            register_user_in_system()
        elif functions == 7:
            show_systeminfo()
        elif functions == 8:
            show_hardware_info()
        elif functions == 0:
            print("Bye")
            break
         


if __name__ == '__main__':
    main()
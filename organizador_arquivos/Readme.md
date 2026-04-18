## Automação de organização de arquivos

Projeto realizado no intuito de organizar diretórios pelos tipos de arquivos informados, evitando assim confusão na procura de determinado arquivo, necessitando apenas procurar pela pasta que contém o tipo dele. Além de também criar pastas e informar qual tipo de arquivo deseja acrescentar nelas.

## Tecnologias Utilizadas
- Linguagem Python🐍
- Bibliotecas: os(manipulação de arquivos e diretórios), loguru(logs do projeto) e psutil(informações do SO)⚙️

## Baixar o projeto 
` git clone https://github.com/GabrielCv54/PP-automa-es.git`


### Rodar o projeto
```
cd organizador_arquivos
python main.py ou python -m main
```

### Funções presentes no projeto
- list_all_directorys() - Mostra os diretórios que estão no projeto
- create_new_folder() - Criar um novo diretório
- create_new_file() - Criar um novo arquivo
- show_files_of_specific_folder() - Mostrar os arquivos de determinado diretório
- edit_folder() - Editar diretório específico
- exclude_folder() - Excluir diretório específico
- register_user_in_system() - Criar um novo usuário para armazená-lo no arquivo users.txt
- show_systeminfo() - Mostra as configurações do sistema
- show_hardware_info() - Mostra as informações do disco e da memória RAM
- main() - Função princiapl responsável pela execução de todas as outras
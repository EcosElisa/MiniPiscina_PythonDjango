#!/bin/sh

#Pip: um gerenciador de pacotes para Python.
pip_version=$(pip --version)
echo "The used version of pip is: $pip_version"

#Utiliza o pip para instalar ou atualizar o pacote path.py do repositório Git fornecido.
pip install --upgrade git+https://github.com/jaraco/path.py.git > path_install.log
# > path_install.log': redireciona a saída do comando para um arquivo chamado path_install.log,
# que será criado (ou substituído se já existir), para registrar informações sobre a instalação.

#Cria um ambiente virtual Python (venv) chamado local_lib.
#venv: um ambiente isolado onde você pode instalar pacotes Python sem afetar o sistema global.
python3 -m venv local_lib

#Executa o programa my_program.py(apenas se ele existir no mesmo diretorio onde o
# script esta sendo rodado).
python3 my_program.py
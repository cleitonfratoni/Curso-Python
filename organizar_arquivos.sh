#!/bin/bash

# Organiza os arquivos em ordem alfabética
ls -1 | sort > arquivos_ordenados.txt

# Adiciona todos os arquivos ao commit
git add .

# Realiza o commit com uma mensagem
git commit -m "Organizando arquivos em ordem alfabética"

# Realiza o push para o repositório remoto
git push hub-curso-python main

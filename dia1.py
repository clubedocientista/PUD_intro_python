# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 20:38:20 2020

@author: Rafael
Clube do Cientista
Curso Python
Munk2020

"""


####################  PUD
###############       Seminário Python
##########            Comandos básicos
#####                 Nossos comandos = INPUT (In) no Console

## Hello World
print ("Hello World")                          
# imprime (Out) algo no console
print ('Bem vindos ao seminário de introdução ao python')
# \n = proxima linha ('Enter')
# \t = tabulação ('Tab')      

import os
os.getcwd()         # retorna o diretório atual
os.chdir('D:\\Documentos\\Clube do Cientista\\cursos\\Python_PUD')      # altera o diretório para PATH
# muda com SO ('\', '\\', ou '/')
os.listdir()            

## Manuseando diretórios e arquivos
# explorador de arquivos x explorador de variáveis

arquivos = os.listdir()   # salva lista de arquivos em variável
import glob
glob.glob('*.py')         # retorna arquivos com extensão .py
glob.glob('*.txt')

print (arquivos)
type (arquivos)                                 # lista de texto strings
arquivos[0]                                     # diferença entre () e []

dir = 'testes'
os.mkdir(dir)                                   # criando diretório '\testes'
os.chdir(dir)                                   # alterando diretório para '\testes'
os.listdir()

# salvando arquivo de texto
texto1 = 'Seminário PUD + Clube do Cientista\nHello World'
print (texto1)
texto1

texto2 = input ('Qual é o seu nome?\n')  # salva input em variávell
print (texto2)
texto3 = input ('Qual é a sua idade?\n') 

file = open('aulas_teste.txt', 'w') # cria arquivo no modo 'write'
file.write(texto1+'\n')             # escreve texto1 e próxima linha
file.write(texto2+'\n')          
file.write(texto3)                      
file.close()                        # fecha o arquivo


# outro modo - identação
with open('aulas_teste.txt', 'w') as file:
    file.write(texto1)             # identação indica as linhas que estão dentro da função 'open'
    file.write('\n\n')
    file.write(texto2)


from shutil import copyfile, rmtree
copyfile('aulas_teste.txt', 'aulas_teste2.txt') # copiando e renomeando arquivo
os.remove('aulas_teste.txt')                    # apagando arquivo
cd ..
rmtree ('testes')                               # apagando diretório

## copiar e colar em um novo arquivo e rodar com %runfile
'''
PATH = 'D:\\Documentos\\Clube do Cientista\\cursos\\Python_PUD'
import os
os.getcwd()          # retorna o diretório atual
os.chdir(PATH)   
nome_arq = input("Qual será o nome do arquivo: ")
nome_completo = os.path.join(nome_arq+".txt")         
arq           = open(nome_completo, "w")
texto         = input("Escreva o que você quer no arquivo:\n")
arq.write(texto)
arq.close()
print ('O nome do meu arquivo é : ', nome_completo, '\nO conteudo dele é: ', texto)
'''

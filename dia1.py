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
print ('Bem vindos ao seminário de curso de introdução\nao python do Clube do Cientista')
# \n = proxima linha ('Enter')
# \t = tabulação ('Tab')      

PATH = 'D:\\Documentos\\Clube do Cientista\\cursos\\Python_PUD' # muda com SO ('\', '\\', ou '/')
import os
os.getcwd()                                      # retorna o diretório atual
os.chdir(PATH)                                   # altera o diretório para PATH
os.listdir()            

## Manuseando diretórios e arquivos
# explorador de arquivos x explorador de variáveis

arquivos = listdir()                            # lista de arquivos salvo como variável
import glob
glob.glob('*.py')                               # arquivos com extensão .py
glob.glob('*.txt')

print (arquivos)
type (arquivos)                                 # lista de texto strings
arquivos[0]                                     # diferença entre () e []

dir = 'testes'
os.mkdir(dir)                                   # criando diretório '\testes'
os.chdir(dir)                                   # alterando diretório para '\testes'

texto1 = 'Hello World\nturma Cousteau2020'
print (texto1)

texto1

texto2 = input ('Qual é o seu nome?\n')         # gravao o input In em variável
print (texto2)


file = open('aulas_teste.txt', 'w')             # cria arquivo no modo 'write'
file.write(texto1+'\n')                         # escreve texto1 e próxima linha
file.write(texto2)                              # escreve texto2
file.close()                                    # fecha o arquivo


# outro modo - identação
with open('aulas_teste.txt', 'w') as file:
    file.write(texto1)                          # identação indica as linhas que estão dentro da função 'open'
    file.write('\n\n')
    file.write(texto2)


from shutil import copyfile, rmtree
copyfile('aulas_teste.txt', 'aulas_teste2.txt') # copiando e renomeando arquivo
os.remove('aulas_teste.txt')                    # apagando arquivo
cd ..
rmtree ('testes')                               # apagando diretório


#  cria diretório se inexistente
try:                                            # tentativa de executar comandos
    os.mkdir(dir)
    print("O diretório " , dir ,  " foi criado ")    
except FileExistsError:                         # se o erro for do tipo 'FileExistsError
    print("O diretório " , dir ,  " já existe")


rmtree ('testes')



PATH = ('D:\\Documentos\\Clube do Cientista\\curso Python\\Cousteau2020') # muda com SO ('\', '\\', ou '/')
import os
os.getcwd()                                      # retorna o diretório atual
os.chdir(PATH)   
name_of_file = input("What is the name of the file: ")
completeName = os.path.join(name_of_file+".txt")         
file1        = open(completeName, "w")
toFile       = input("Write what you want into the field")
file1.write(toFile)
file1.close()

print ('O nome do meu arquivo é : ', completeName, '\nO conteudo dele e: ', toFile)


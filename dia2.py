# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:32:36 2020

@author: Rafael
Clube do Cientista
Curso Python
Munk2020
"""

####################  PUD
###############       Seminário Python
##########            Introdução a Data Mining

import numpy as np
import pandas as pd

### listas, dataframes e operações simples
lista1 = [1,2,3,4,5]               # lista de int
lista1
lista1 = np.arange(1,6,1)
lista1
lista2 = [[1,2,3,4,5],[5,4,3,2,1]] # lista de listas
lista2

print (lista1[1])                  # posição 1
print (lista1[-1])                 # última posição
print (lista2[1][2])               # posição 2 do item 1
print (lista1[0:2])                # intervalo de posições

# boolean
a = True
print (a)
type (a)                           # bool  = True or False

# operações
type (lista1)    == int            # é igual a 
type (lista1[1]) != float          # é diferente de 

lista1[0:-1:2]                     # primeiro ao ultimo a cada dois 
lista1[lista1>2]   
lista1[(lista1>2) & (lista1<4)]    # condição E
lista1[(lista1>4) | (lista1<=2)]   # condição OU

# dataframes (tabelas)
lista1 = np.random.randint(low = 3, high = 30, size = 100)
lista1 # vetor aleatório com 100 números inteiros de 3 a 30
lista2 = np.random.randint(low = 1, high = 360, size = 100)
lista2 # vetor aleatório com 100 números inteiros de 1 a 360
 
pd.Series(lista2)               # formato Series (~coluna)
df = pd.concat([pd.Series(lista1), pd.Series(lista2)], axis = 1)
# axis = 1 --> para colunas
df
df.columns = ['Var1','Var2']    # renomeia colunas do dataframe
df

df['Var1'].head()  # retorna as 5 primeiras linhas da coluna Var1
len(df)            # retorna a quantidade de linhas do dataframe
len(df.columns)    # retorna a quantidade de colunas do dataframe
df.loc[2,]         # retorna todos os dados da terceira linha
df.Var2            # retorna todos os dados da coluna Var2
df.loc[1,'Var2']   # retorna o valor da segunda linha da coluna Var2

df['Var3'] = df['Var1']*np.sqrt(df['Var2'])
df['Var3'].head()

df.to_csv('minha_tabela.csv', sep = ';')


### condicionais e repetição

# if
if type (df) == float: # se tipo de 'df' é float
    print ('df é uma variável do tipo float') 
elif type(df) == bool: # ou se tipo de 'df' é bool
    print ('df é uma variável do tipo bool') 
else:                  
    print ('df não é uma variável do tipo float nem bool')

# while
nomes = []
c     = 0
while c < 5: 
    nomes.append (input ('Qual seu nome:'))
    c = c + 1

# for   
n = np.arange(10)
for i in n:     # para cada elemento (i) em n 
    print (i)   # imprimir o elemento (i)

# for + if
n = df['Var1']
print (n)
r = []
for x in n:
    #print (n[i])
    if x < 10:
        r.append(x)
print(r)       # r = valores em n menores do que 10
print (len(r))

# exempplo compacto: for e if em uma linha
del r
r = [i for i in n if i < 10] 
print(r)  
print (len(r))

#ou
n[n<10]  
    
# lendo dados COVID
# https://ourworldindata.org/coronavirus-source-data
    
import xlrd
from os import chdir
chdir ('D:\\Documentos\\Clube do Cientista\\cursos\\Python_PUD')
df_covid  = pd.read_excel('owid-covid-data.xlsx', sheet_name = 'Sheet1')
df_covid2 = df_covid[~df_covid.location.isin(['World','International'])]
df_paises = df_covid2.drop_duplicates(subset='location')
df_paises.columns
df_paises.columns[22]
lista_paises = df_paises['location']
df_paises    = df_paises[df_paises.columns[22:-1]]
df_paises    = df_paises.reset_index(drop=True)

obitos, casos, testes = [],[],[]
for p in lista_paises:
    df_covid_f = df_covid2[df_covid2.location == p]
    obitos.append(df_covid_f.total_deaths.max())
    casos.append(df_covid_f.total_cases.max())
    testes.append(df_covid_f.total_tests.max())

df_paises = pd.concat([df_paises, pd.Series(obitos, name = 'total_obitos'),pd.Series(casos, name = 'total_casos'),pd.Series(testes, name = 'total_testes')],axis=1)

df_paises.describe()
cor_table = df_paises.corr()

'''
import statsmodels.formula.api as sm
modelB = sm.ols(formula='B ~ SR', data=df2)
modelB_trained = modelB.fit()
modelB_trained.summary()

modelB = sm.ols(formula='B ~ SR + WS', data=df2)
modelB_trained = modelB.fit()
modelB_trained.summary()
'''

# Textos
# https://forms.gle/vut4wWavN8WesRZJA
%run wordcloud_PUD.py
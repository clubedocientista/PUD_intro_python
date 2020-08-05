# -*- coding: utf-8 -*-
"""
Created on Jun 2019
@author: Rafael Menezes
"""

def remover_plural(sentence):
    sufixos_plural = ['ões', 'eis', 'res', 'ais', 's', 'ção', 'rão']
    sufixos_sing   = ['ão',  'el',  'r',   'al',  '', '', '']
    for s in range(0,len(sufixos_plural)):
        sufixo = sufixos_plural[s]
        ids    = [index for index,value in enumerate(sentence) if value.endswith(sufixo) == True]
        for i in ids:
            palavra     = sentence[i]
            sentence[i] = palavra[:-len(sufixo)] + sufixos_sing[s]
            #sentence[i] = sentence[i].replace(sufixo,sufixos_sing[s])
    return sentence

def remover_sinonimos(sentence):
    buscar_por   = ['ma']
    trocar_por   = ['']
    for s in range(0,len(buscar_por)):
        sinonimo = buscar_por[s]
        ids    = [index for index,value in enumerate(sentence) if value == sinonimo]
        for i in ids:
            sentence[i] = sentence[i].replace(sinonimo,trocar_por[s])
    return sentence

def preprocess(data):
    from nltk.corpus import stopwords
    user_stops     = ['uso','deixar','ato','apresentaram','destas','destes','apena','mal','dia','Para','outro','para','etc', 'onde','bem', '0s','et','al', 'faz','receberam', 'português','inglês', 'https','parte','longo','dentro','durante','ponto','número','toda', 'podem', 'porém', 'destas', 'levou', 's', 'dessas', 'dessa', 'todo', 'momento', 'pode', 'outras', 'vez', 'é', 'sobre', 'cada', 'apenas', 'ainda', 'ano', 'assim', 'forma', 'ser', 'desta', 'outra', 'principalmente', 'possível', 'sendo']
    stops          = stopwords.words('portuguese') + user_stops  
    reviews_tokens = []

    import re
    for review in data:
        if str(review) != 'nan':
            review              = review.lower()
            raw_word_tokens     = re.findall(r'(?:\w+)', review, flags = re.UNICODE) #remove pontuaction
            word_tokens         = remover_plural(raw_word_tokens)
            word_tokens         = [w for w in word_tokens if not w in stops] # do not add stop words
            word_tokens         = remover_sinonimos(word_tokens)
            reviews_tokens.append(word_tokens)

    n_palavras = [len(reviews_tokens[i]) for i in range(0,len(reviews_tokens))]
    return reviews_tokens, n_palavras #return all tokens
       
def nuvem_palavras (fig, textos):
    from matplotlib.colors import ListedColormap
    from wordcloud import WordCloud
    import itertools
        
    tokenized_reviews, n_palavras = preprocess(textos) #apply the preprocess step
    reviews      = list(itertools.chain(*tokenized_reviews))
    text_reviews = " ".join(reviews)
    #'firebrick','goldenrod','darkmagenta','steelblue','darkgray','black','seagreen'
    mapa_cores   = ListedColormap(['seagreen', 'steelblue','darkmagenta','goldenrod','black'])
    wordcloud    = WordCloud(background_color = 'white', max_words=15, colormap = mapa_cores, margin=0).generate(text_reviews)
        
    plt.imshow(wordcloud, interpolation = "bilinear")
    plt.axis("off")
    return fig, n_palavras

def main ():
    import pandas as pd 
    import xlrd

    pasta   = 'D:\\Documentos\\Clube do Cientista\\cursos\\Python_PUD\\'
    arquivo = 'PUD + Clube do Cientista (respostas).xlsx'
    df_respostas  = pd.read_excel(pasta + arquivo, sheet_name = 'Respostas ao formulário 1')
    frases= df_respostas[df_respostas.columns[1]]
    fig             = plt.figure(figsize=(17,8.5))
    fig, n_palavras = nuvem_palavras(fig, frases.to_list())
    print ('\nNúmero de palavras: ', n_palavras)
    fig.show()


import matplotlib.pyplot as plt
if __name__ == "__main__":
	main() 
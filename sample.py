import nltk,sys

texto = sys.argv[1]

# Acessando o corpus MacMorpho
mac_morpho = nltk.corpus.mac_morpho

#acessando em blocos de sentenças do MacMorpho
colection = nltk.corpus.mac_morpho.tagged_sents()

#separamos cada palavra (Tokenização)
sentense = nltk.word_tokenize(texto)

#Training Unigram Tagger - Determinar uma tag para cada token(palavra)
unigrama = nltk.tag.UnigramTagger(colection)

#Encontrar os resultados marcados após o treinamento
array = unigrama.tag(sentense)

#Legendas para tradução dos termos
arr1 = ['ADJ','ADV-KS','ADV-KS-REL','ART','KC','KS','IN','N','NPROP','NUM','PCP','PDEN','PREP','PROADJ','PRO-KS','PROPESS','PRO-KS-REL','PROSUB','V','VAUX','CUR']
arr2 = [
    'Adjetivo',
    'Advérbio conectivo subordinativo',
    'Advérbio relativo subordinativo',
    'Artigo def. ou indef.',
    'Conjunção coordenativa',
    'Conjunção subordinativa',
    'Interjeição',
    'Substantivo',
    'Substantivo próprio',
    'Numeral',
    'Particípio',
    'Palavra denotativa',
    'Preposição',
    'Pronome adjetivo',
    'Pronome conectivo subordinativo',
    'Pronome pessoal',
    'Pronome relativo conectivo subordinativo',
    'Pronome substantivo',
    'Verbo',
    'Verbo auxiliar',
    'Simbolo de moeda corrente',
]

#Apresentação dos resultados
for n in array:
    print(n[0], ' = ', arr2[arr1.index(n[1])])
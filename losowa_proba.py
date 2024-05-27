'''program losujacy bez powtórzeń 100 sekwencji z wybranego pliku fasta'''

import re
import random

#podział pliku fasta na listę sekwencji
sciezka = "sciezka do pliku wejsciowego"
plik = open(sciezka,"r")
wzorseq = re.compile(r'>')
plik.read(1)
listaseq = wzorseq.split(plik.read())
plik.close()

lista =['>'+i for i in listaseq]

#wylosowanie 100 sekwencji bez powtorzen
nowa_lista = random.sample(lista, 100)

#zapisanie wyników w pliku fasta
wyjscie = "sciezka do pliku wyjsciowego"
plik2 = open(wyjscie,'w')
for i in nowa_lista:
    plik2.write(i)
plik2.close()
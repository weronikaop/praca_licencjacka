'''program filtrujacy dane sekencji pochodzące z pliku fasta
zachowuje te, które opisane są słowem 'protease' lub 'peptidase' 
oraz należą do cyjanobakterii''' 
import re
from Bio import Entrez

sciezka = "sciezka do pliku wejsciowego"
#utworzenie listy nazw wszystkich białek w pliku
plik = open(sciezka,'r')
wzor = re.compile(r'^>([\S]+)',re.M)
lista = wzor.findall(plik.read())
plik.close()

#utworzenie listy wszystkich sekwencji
plik = open(sciezka,'r')
wzorseq = re.compile(r'>')
plik.read(1)
listaseq = wzorseq.split(plik.read())
plik.close()

seq = ""
numer = 0

Entrez.email = "weronika.oprzedek@student.uj.edu.pl"

for i in lista:
    #pozyskanie danych dla danego białka z bazy danych Entrez
    handle = Entrez.efetch(db="protein", id=i, retmode="xml")
    record = Entrez.read(handle)
    handle.close()
    #przeszukanie danych zapisanych w formacie xml
    if('Cyanobacteriota' in record[0]['GBSeq_taxonomy']):
        opis = ""
        for j in record[0]['GBSeq_feature-table']:
            if('GBFeature_quals' in j):
                for k in j['GBFeature_quals']:
                    if('GBQualifier_value' in k):
                        opis +=k['GBQualifier_value']
        if('protease' in opis or 'peptidase' in opis):
            #spełniające warunki sekwencji są zapamiętywane
            seq += '>'+listaseq[numer]
    numer += 1

#zapisanie wyników w pliku fasta
wyjscie = "sciezka do pliku wyjsciowego"
plik2 = open(wyjscie,'w')
plik2.write(seq)
plik2.close()

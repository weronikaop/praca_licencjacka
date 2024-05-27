'''program, który dla pliku w formacie fasta, posiadającego zduplikowane sekwencje,
dzieli go na plik zawierający sekwencje bez duplikatów oraz na plik zawierający
tylko sekwencje będące duplikatami'''

import re

#podział pliku fasta na listę sekwencji
sciezka = "sciezka do pliku wejsciowego"
plik = open(sciezka,"r")
wzorseq = re.compile(r'>')
plik.read(1)
listaseq = wzorseq.split(plik.read())
plik.close()

lista =['>'+i for i in listaseq]

#oddzielenie duplikatów od pozostałych sekwencji
res = []
dup = []
for x in lista:
    if (x not in res):
        res.append(x)
    else:
        dup.append(x)

#ilość sekwencji unikatowych
print(len(res))

listaseq = list(set(lista))

#zapisanie sekwencji bez duplikatów do pliku
wyjscie1 = "sciezka do pliku wyjsciowego z wynikami"
plik2 = open(wyjscie1,'w')
for i in res:
    plik2.write(i)
plik2.close()

#zapisanie sekwencji duplikatów do pliku
wyjscie2 = "sciezka do pliku wyjsciowego z dublikatami"
plik3 = open(wyjscie2,'w')
for i in dup:
    plik3.write(i)
plik3.close()
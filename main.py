class Ksiazka:
  def __init__(self, tytul, autor):
    self.tytul = str(tytul)
    self.autor = str(autor)

class Egzemplarz:
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

def sortowanie(Ksiazka):
    return Ksiazka.tytul

def sprawdzenie(ksiazki, tytul, autor):
    for i in range (len(ksiazki)):
        ksiazka = ksiazki[i]
        if tytul == ksiazka.tytul and autor == ksiazka.autor:
            return True
    return False

ksiazki = []
egzemplarz = []

w = input()
for i in range(0, int(w)):
    k = 0
    temp = eval(input())
    if not ksiazki:
        ksiazki.append(Ksiazka(temp[0], temp[1]))
    else:
        jestBiblioteka = sprawdzenie(ksiazki, temp[0], temp[1])
        if jestBiblioteka is False:
            ksiazki.append(Ksiazka(temp[0], temp[1]))
    ksiazki.sort(key=sortowanie)

for j in range(len(ksiazki)):
    licz = 0
    temp = ksiazki[j]
    for i in range(len(egzemplarz)):
        ks = egzemplarz[j]
        if temp.tytul == ks.tytul and temp.autor == ks.autor:
            licz = licz + 1
    licz = str(licz)
    print("('"+temp.tytul+"',","'"+temp.autor+"',",licz+")")

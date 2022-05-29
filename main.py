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
        k = ksiazki[i]
        if tytul == k.tytul and autor == k.autor:
            return True
    return False

ksiazki = []
egzemplarz = []

w = input()
for i in range(0, int(w)):
    l = 0
    temp = eval(input())
    if not ksiazki:
        ksiazki.append(Ksiazka(temp[0], temp[1]))
    else:
        jestBiblioteka = sprawdzenie(ksiazki, temp[0], temp[1])
        if jestBiblioteka is False:
            ksiazki.append(Ksiazka(temp[0], temp[1]))
    egzemplarz.append(Egzemplarz(temp[0], temp[1], temp[2]))
    
ksiazki.sort(key=sortowanie)

for i in range(len(ksiazki)):
    licz = 0
    temp = ksiazki[i]
    for i in range(len(egzemplarz)):
        ks = egzemplarz[i]
        if temp.tytul == ks.tytul and temp.autor == ks.autor:
            licz = licz + 1
    licz = str(licz)
    print("('"+temp.tytul+"',","'"+temp.autor+"',",licz+")")

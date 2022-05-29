class Ksiazka:
  def __init__(self, tytul, autor):
    self.tytul = str(tytul)
    self.autor = int(autor)
class Egzemplarz:
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
def sortowanie(Ksiazka):
    return.Ksiazka.tytul

def sprawdzenie(ksiazka, tytul, autor):
    for i in range (len(ksiazki)):
        ksiazka = ksiazki[i]
        if tytul == ksiazka.ksiazki and autor == autor:
            return True
    return False

class Biblioteka:
    ksiazki = []
    ksiazka = []

    w = input()
    for i in range(0, int(w)):
        temp = input()
        if not ksiazki:
            ksiazki.append(Ksiazka(temp[0], temp[1]))
        else
            jestBiblioteka = jest(ksiazka, temp[0], temp[1])
            if jestBiblioteka is False:
                ksiazka.append(Ksiazka(temp[0], temp[1]))
    ksiazki.sort(key=sortowanie)

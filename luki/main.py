dane = list(map(int, open("dane4.txt").readlines()))
# dane = [4,11,4,1,4,7,11,12,13,14,7,0,3]
# dane = [14,7,0,3]

def oblicz_roznice(a,b):
    if a is None or b is None:
        return None
    return abs(a - b)

roznice = [oblicz_roznice(a,b) for a,b in zip(dane[1:], dane)]

print("zad1")
print("min", min(roznice))
print("max", max(roznice))


ciagi_regularne = []
bufor = []

def ostatnia_liczba_dodana_do_ciagu():
    if ciagi_regularne == []:
        return None
    
    return ciagi_regularne[-1][-1]

for i, liczba in enumerate(dane[:-1]):
    aktualna_liczba, kolejna_liczba = [liczba, dane[i+1]]
    ostatnia_liczba = ostatnia_liczba_dodana_do_ciagu()

    def porownaj_roznice(a,b):
        if a == -1:
            return False
        return a == b

    def bufor_jest_pusty():
         return bufor == []

    def w_buforze_jest_jedna_liczba():
        return len(bufor) == 1

    def kolejna_liczba_jest_ostatnia_liczba():
        return len(dane) == i+2
    
    def aktualna_liczba_pasuje_do_bufora():
        return porownaj_roznice(aktualna_roznica(), roznica_bufora())
    
    def kolejna_liczba_pasuje_do_bufora():
        return porownaj_roznice(kolejna_roznica(), roznica_bufora())
    
    def ostatnia_liczba_pasuje_do_2_kolejnych_liczb():
        return porownaj_roznice(oblicz_roznice(ostatnia_liczba, aktualna_liczba), oblicz_roznice(aktualna_liczba, kolejna_liczba))

    def roznica_bufora():
        if len(bufor) < 2:
            return None
        return oblicz_roznice(bufor[0], bufor[1])

    def aktualna_roznica():
        return oblicz_roznice(aktualna_liczba, bufor[-1])

    def kolejna_roznica():
        return oblicz_roznice(kolejna_liczba, bufor[-1])


    def czy_dodac_bufor_do_ciagow():
        return len(bufor) >= 2 and porownaj_roznice(roznica_bufora(), kolejna_roznica()) is False \
            or kolejna_liczba_jest_ostatnia_liczba()

    def czy_dodac_aktualna_liczbe_do_bufora(): 
        return len(bufor) <= 1 or aktualna_liczba_pasuje_do_bufora()

    def czy_dodac_ostatnia_liczbe_do_bufora():
        return len(bufor) == 0 and ostatnia_liczba_pasuje_do_2_kolejnych_liczb()

    def czy_dodac_kolejna_liczbe_do_bufora():
        return kolejna_liczba_pasuje_do_bufora() and kolejna_liczba_jest_ostatnia_liczba()

    if czy_dodac_ostatnia_liczbe_do_bufora():
        bufor.append(ostatnia_liczba)

    if czy_dodac_aktualna_liczbe_do_bufora():
        bufor.append(aktualna_liczba)
    
    if czy_dodac_kolejna_liczbe_do_bufora():
        bufor.append(kolejna_liczba)

    if czy_dodac_bufor_do_ciagow():
        ciagi_regularne.append(bufor)
        bufor = []
        if kolejna_liczba_jest_ostatnia_liczba():
            ciagi_regularne.append([aktualna_liczba, kolejna_liczba])
    
max_ciag = max(ciagi_regularne, key=len)

print("zad2", max_ciag[0], max_ciag[-1], ", dlugosc:",len(max_ciag))

    
krotnosci = {k: 0 for k in set(roznice)}

for roznica in roznice: 
    krotnosci[roznica] += 1

print("zad3", max(krotnosci, key=lambda x: krotnosci[x]))

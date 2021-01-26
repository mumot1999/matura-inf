# dane = list(map(int, open("dane4.txt").readlines()))
dane = [4,11,4,1,4,7,11,12,13,14,7,0,-7]
# dane = [14,7,0,3]

def oblicz_roznice(a,b):
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

for i, liczba in enumerate(dane):
    aktualna_liczba, kolejna_liczba = [liczba, dane[i+1] if i+1 < len(dane) else None]

    if kolejna_liczba is None:
        ciagi_regularne.append([ostatnia_liczba_dodana_do_ciagu(), aktualna_liczba])
        continue
            

    if bufor == []:
        if(ostatnia_liczba_dodana_do_ciagu() and oblicz_roznice(aktualna_liczba, kolejna_liczba) == oblicz_roznice(ostatnia_liczba_dodana_do_ciagu(), aktualna_liczba)):
            bufor = [ostatnia_liczba_dodana_do_ciagu(), aktualna_liczba]
        else:
            bufor = [aktualna_liczba]
        continue
    
    if len(bufor) == 1:
        bufor.append(aktualna_liczba)
        continue

    aktualna_roznica = oblicz_roznice(aktualna_liczba, bufor[-1])
    roznica_bufora = oblicz_roznice(bufor[0], bufor[1])

    if aktualna_roznica == roznica_bufora:
        bufor += [aktualna_liczba]

    kolejna_roznica = oblicz_roznice(kolejna_liczba, bufor[-1])

    if kolejna_roznica != roznica_bufora:
        ciagi_regularne.append(bufor)
        bufor = []
    
print(dane)
print(ciagi_regularne)
print(len(max(ciagi_regularne, key=len))+1)

    



# 1.1. Gražina trijų paduotų skaičių sumą.
def sk_suma(x, y, z):
    suma = x + y + z
    return suma


print("1.", sk_suma(22, 445, 303))


# 1.2.  Gražina paduoto sąrašo iš skaičių, sumą.
def sudeti(skaiciu_sarasas):
    skaiciu_sarasas = [35, 555, 87, 3, 66, 39, 470, 11, 22, 9]
    return sum(skaiciu_sarasas)


print("2.", sudeti(skaiciu_sarasas=[]))


# 1.3 Atspausdina didžiausią iš kelių paduotų skaičių (panaudojant *args).
def didziausias_skaicius(*args):
    return max(222, 3333, 99, 111, 2222, 333, 11, 4747)


print("3.", didziausias_skaicius())


# 1.4 Turi gražinti paduotą stringą atbulai.
def atvirkscia_fraze(fraze):
    return fraze[::-1]


fraze = atvirkscia_fraze("Laba diena su vištiena")

print("4.", fraze)


# 1.5 Atspausdina, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
def suskaiciuok(zod_raid_sk):
    maz_r = 0
    did_r = 0
    sk = 0

    # zod_raid_sk = "3 Laba Diena Su ViŠtieNa"
    for raide in zod_raid_sk:
        if raide.islower():
            maz_r += 1
            # return maz_r
        if raide.isupper():
            did_r += 1
            # return did_r
        if raide.isnumeric():
            sk += 1
    print(f"5. Mažųjų raidžių: {maz_r}, didžiųjų raidžių: {did_r}, skaičių: {sk}")
    print(f"5.1. Frazėje yra žodžių: {len(zod_raid_sk.split())}")


suskaiciuok("2 Laba Diena Su 3 ViŠtieNa")


# 1.6 Gražinti sąrašą tik su unikaliais paduoto sąrašo elementais.
def sarasas_su_elementais(visas_sarasas):
    sarasas = []
    for elementas in visas_sarasas:
        if elementas not in sarasas:
            sarasas.append(elementas)
    return sarasas


print("6. Unikalios reikšmės =", sarasas_su_elementais([2, 444, "Aš", 6, 323, 454, "Aš", 5, "Aš", 444, 1, 2, 323]))

# 1.7 Gražinti, ar paduotas skaičius yra pirminis.

ivestas_skaicius = int(input("7. Įveskite norimą skaičių: "))


def ar_ivestas_pirminis(sk):
    if sk > 1:
        for nezinomas in range(2, sk):
            if sk % nezinomas == 0:
                return False
        return True
    return False


print(f"   Ar įvestas skaičius pirminis? {ar_ivestas_pirminis(ivestas_skaicius)}")

# 1.8 Išrikiuoti paduoto stringo žodžius nuo paskutinio iki pirmojo.

mano_fraze = "Laba diena su vištiena"

def paskutinis_pirmas(mano_fraze):
    po_viena_zodi = mano_fraze.split()[::-1]
    return "  ".join(po_viena_zodi)

print(f"8. {paskutinis_pirmas(mano_fraze)}")

# 1.9 Gražina, ar paduoti metai yra keliamieji, ar ne.
import calendar

def tai_kurie_tie_metai(metai_sk):
     return calendar.isleap(metai_sk)

print(f"9. Ar metai keliamieji?\n   2000: {tai_kurie_tie_metai(2000)}, 1900: {tai_kurie_tie_metai(1900)}, 2400: {tai_kurie_tie_metai(2400)}")
#print(tai_kurie_tie_metai(1900))
#print(tai_kurie_tie_metai(2400))

# 1.10 Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.
import datetime

def kiek_praejo_nuo(mano_data):
    norima_data = datetime.datetime.strptime(mano_data, "%Y-%m-%d %X")  # nedet kabutese kablelio tarp datos ir laiko!!!
    siandien = datetime.datetime.now()
    #print(siandien.strftime("%Y-%m-%d %X"))
    #print(str(siandien)[:19])
    print(f"10.Nuo {str(siandien)[:19]} iki {norima_data} praėjo:")

    kiek_skiriasi = (siandien - norima_data)

#print("Data skiriasi dienų: ", kiek_skiriasi.days)

    print("Kiek metų? ", kiek_skiriasi.days // 365)
    print("Kiek mėnesių? ", round(kiek_skiriasi.days / 365 * 12))
    print("Kiek savaičių? ", kiek_skiriasi.days // 7)
    print("Kiek dienų? ", kiek_skiriasi.days)
    print("Kiek valandų? ", round(kiek_skiriasi.total_seconds() // 3600))
    print("Kiek minučių? ", round(kiek_skiriasi.total_seconds() / 60))
    print("Kiek sekundžių? ", round(kiek_skiriasi.total_seconds()))

kiek_praejo_nuo("2020-02-20 20:00:20")

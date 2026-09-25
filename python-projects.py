print("="*40)

# --- CALCULATOR SI SIMULATOR DE MEDIE SCOLARA ---

print("=== CALCULATOR DE MEDIE SI PROGNOZA DE NOTA ===")

nume_elev = input("Introdu numele tău: ")
materia = input("La ce materie calculăm media? ")

# 1. Preluarea notelor (conversie și operatii)
n1 = int(input("Introdu prima notă: "))
n2 = int(input("Introdu a doua notă: "))
n3 = int(input("Introdu a treia notă: "))

# Suma și împărțirea pentru medie (Operatori aritmetici: +, /)
suma_note = n1 + n2 + n3
media_actuala = suma_note / 3

print(f"\nMedia ta actuală la {materia} este: {media_actuala:.2f}")

# 2. Verificare promovabilitate și bursă (Operatori de comparare și logici)
promovat = media_actuala >= 4.50
medie_bursa = media_actuala >= 9.50 and (n1 >= 5 and n2 >= 5 and n3 >= 5)

if medie_bursa:
    print(" Status: Felicitări! Te încadrezi la bursă la această materie!")
elif promovat:
    print(" Status: Ești promovat la această materie.")
else:
    print(" Status: Atenție! Ești în pericol de corigență.")

# 3. SIMULATOR: Ce notă îți trebuie la următoarea ascultare?
print("\n--- SIMULATOR PENTRU URMĂTOAREA NOTĂ ---")
medie_dorita = float(input("Ce medie ți-ai dori să ai în total? "))

# Formula matematică: (Suma notelor + Nota NOUA) / 4 = Media Dorită
# Deci: Nota NOUA = (Media Dorită * 4) - Suma notelor existente
nota_necesara = (medie_dorita * 4) - suma_note

print("\n" + "="*40)
print(f"REZULTAT PROGNOZĂ PENTRU {nume_elev.upper()}:")

# Verificăm dacă nota necesară este realistă (între 1 și 10)
if nota_necesara > 10:
    print(f"Din păcate, chiar dacă iei 10, nu mai poți ajunge la media {medie_dorita}.")
    print(f"Media maximă pe care o poți obține cu un 10 este: {(suma_note + 10) / 4:.2f}")
elif nota_necesara <= 1:
    print(f"Ești deja într-o poziție excelentă! Orice notă iei, îți păstrezi sau depășești media {medie_dorita}.")
else:
    # Rotunjim nota necesară în sus
    print(f"Pentru a obține media {medie_dorita}, trebuie să iei minim nota {int(nota_necesara + 0.99)} la următoarea ascultare/lucrare.")

print("="*40)

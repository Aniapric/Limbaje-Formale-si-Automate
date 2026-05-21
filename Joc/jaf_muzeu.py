import time # ma ajuta sa afisez mesajul cu tranzitie ( fiecare caracter pe rand)
import os

# ca sa sterg ce s-a afisat pana atunci in terminal 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# pt ca jucatorul sa aiba o experienta interactiva, folosesc enter
def asteapta_enter(mesaj="[ Apasa ENTER pentru a continua... ]"):
    input(f"\n  {mesaj}")

#functie care inlocuieste print-ul normal, printeaza caracterele pe rand folosind un delay
def tipareste_incet(text, delay=0.04):
    for caracter in text:
        print(caracter, end='', flush=True)
        time.sleep(delay)
    print()

# DESENE : 

#deseneaza muzeul la inceput
def deseneaza_fata_muzeu():
    print(r"""
   🕵️  <-- tu

         -----------------------------
        |   MUZEU NATIONAL DE ARTA    |
        |   -----   -----   -----     |
        |   |   |   |   |   | 🖼️ |     |
        |   -----   -----   -----     |
        |                             |
        -----------[ usa ]-------------
    """)

# deseneaza caracter la intrare
def deseneaza_intrare():
    print(r"""
         -----------------------------
        |   MUZEU NATIONAL DE ARTA    |
        |   -----   -----   -----     |
        |   |   |   |   |   | 🖼️ |     |
        |   -----   -----   -----     |
        |         --> 🕵️ <--           |
        -----------[ usa ]-------------
    """)

#aici desenez faza de parcurgere a salilor pentru a ajunge la tablou
def deseneaza_sala(nr_sala, total_sali):
    sali_afisate = ""
    for i in range(1, total_sali + 1):
        if i < nr_sala:
            sali_afisate += " [✓]    "
        elif i == nr_sala:
            sali_afisate += " [🕵️]   "
        else:
            sali_afisate += " [ ]    "

    print(f"""
        -----------------------------
        |   MUZEU NATIONAL DE ARTA    |
        |   -----   -----   -----     |
        |   |   |   |   |   | 🖼️ |     |
        |   -----   -----   -----     |
        |   {sali_afisate:<40}
        -----------[ usa ]-------------
    """)

# deseneaza tablou furat
def deseneaza_tablou_furat():
    print(r"""
         -----------------------------
        |   MUZEU NATIONAL DE ARTA    |
        |   -----   -----   -------   |
        |   |   |   |   |   | 🖼️ 🕵️ |   |
        |   -----   -----   -------   |
        |                             |
        -----------[ usa ]-------------
    """)

# aii desenez parcurgerea inversa a salilor pentru a evada
def deseneaza_evadare(sali_ramase, total_sali):
    sali_afisate = ""
    for i in range(1, total_sali + 1):
        if i < sali_ramase:
            sali_afisate += " [🔒]   "   # sali la care nu ai ajuns inca
        elif i == sali_ramase:
            sali_afisate += "[🕵️]   "   # tu esti aici
        else:
            sali_afisate += " [✓]    "   # sali deja parcurse 


    print(f"""
        -----------------------------
        |   MUZEU NATIONAL DE ARTA    |
        |   -----   -----   -----     |
        |   |   |   |   |   | ❌ |     |
        |   -----   -----   -----     |
        |   {sali_afisate:<40}
        -----------[ usa ]-------------
    """)

def deseneaza_evadat():
    print(r"""
   🕵️💨 <-- ai scapat!

        +------------------------------------------+
        |          MUZEU NATIONAL DE ARTA           |
        |   🚔🚔 politia soseste... prea tarziu!   |
        +------------------------------------------+
    """)

# Etapele jocului: 


# povestea de inceput
def intro():
    clear()
    print("=" * 50)
    print("      🏛️  JEFUIESTE MUZEUL  🏛️")
    print("=" * 50)
    asteapta_enter()

    clear()
    tipareste_incet("\n  E miezul noptii. Orasul doarme.")
    time.sleep(0.3)
    tipareste_incet("  De luni intregi ai studiat planul muzeului.")
    time.sleep(0.3)
    tipareste_incet("  Astazi e ziua cea mare.\n")
    asteapta_enter()

    clear()
    tipareste_incet("  Te afli acum in fata muzeului...")
    time.sleep(0.4)
    deseneaza_fata_muzeu()
    tipareste_incet("  Trebuie sa treci de trei usi 🚪 .")
    tipareste_incet("  La evadare, vei iesi exact pe unde ai intrat.")
    asteapta_enter("[ Apasa ENTER ca sa incepi infiltrarea... ]")


#Faza de infiltrare
# automatul incarca secvential simboluri din alfabetul stivei in memoria sa de tip LIFO.
def faza_infiltrare(stiva, sali_muzeu):
    clear()
    print("\n🏛️  --- FAZA 1: INFILTRAREA  --- 🏛️\n")
    time.sleep(0.5)

    tipareste_incet("  Te strecori pe usa din spate...")
    asteapta_enter()

    clear()
    tipareste_incet("  Ai ajuns la usa principala...")
    deseneaza_intrare()
    asteapta_enter()

    for i, sala in enumerate(sali_muzeu):
        stiva.append(sala) # Tranzitie de push : adaugam simbolul pe stiva PDA-ului
        clear()
        tipareste_incet(f"  Te furisezi in sala 👣 {i + 1}...")
        time.sleep(0.3)
        tipareste_incet(" Securitate sparta! Usa se blocheaza in spate. [🔓]")
        deseneaza_sala(i + 1, len(sali_muzeu))
        asteapta_enter()

    clear()
    tipareste_incet("  Ai gasit tabloul.  🖼️ ")
    time.sleep(0.5)
    tipareste_incet("  Il iei de pe perete...")
    time.sleep(0.6)
    deseneaza_tablou_furat()
    tipareste_incet("  Trebuie sa iesi pe EXACT drumul pe care ai venit!")
    asteapta_enter("[ Apasa ENTER sa incepi evadarea... ]")


#faza de evadare
def faza_evadare(stiva, securitate):
    clear()
    print("\n🏃  --- FAZA 2: EVADAREA  --- 🏃\n")
    time.sleep(0.4)
    tipareste_incet("  Fiecare usa are un panou de securitate.")
    tipareste_incet("  Citeste indiciul si introdu parola corecta.\n")
    time.sleep(0.3)

    total_sali = len(stiva)

    while stiva:
        # Citim doar varful stivei , fara sa il stergem inca
        sala_curenta = stiva[-1]
        indiciu = securitate.get(sala_curenta, "Fara indiciu.")

        deseneaza_evadare(len(stiva), total_sali)

        print(f"  Panou blocat! 🔐")
        print(f"  Indiciu 💡 : {indiciu}")
        #Citim cuvantul de pe banda de intrare (Alfabetul de intrare Σ)
        raspuns = input("  Parola  ⌨️ : ")

        # Functia de tranzitie : daca inputul coincide cu varful stivei
        if raspuns.strip().lower() == sala_curenta.lower():
            # Cuvant acceptat de tranzitie -> execut POP
            stiva.pop()
            clear()
            print(" Corect! Usa s-a deschis. ✅ \n")
            time.sleep(0.6)
        else:
            clear()
            print("\n GRESIT! ")
            time.sleep(0.3)
            tipareste_incet(" Politia te-a prins. Game over. 🚓 ")
            return False

    clear()
    deseneaza_evadat()
    time.sleep(0.3)
    # Acceptare prin stiva goala. :)
    tipareste_incet("  Misiune indeplinita ! 🏆 \n")
    return True


# MAIN 

if __name__ == "__main__":
    securitate = {
        "Claude Monet": "A fost obsedat de modul în care lumina se schimbă pe parcursul zilei și a pictat sute de variante ale aceleiași teme, celebrele 'Nuferi' din grădina sa de la Giverny.",
        "Marie Curie": "A descoperit două elemente chimice noi care străluceau în întuneric. Este singura persoană din istorie cu premii Nobel în două științe distincte.",
        "Mozart": "A compus peste 600 de lucrări înainte de a se stinge fulgerător la doar 35 de ani. Ultima sa operă, celebrul 'Requiem', a rămas neterminată pe patul de moarte.."
    }

    stiva_pda = []
    sali = ["Claude Monet", "Marie Curie", "Mozart"] #  alfabetul de intrare al PDA-ului

    intro()
    faza_infiltrare(stiva_pda, sali)
    faza_evadare(stiva_pda, securitate)

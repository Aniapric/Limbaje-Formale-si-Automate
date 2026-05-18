# Parserul este folosit pentru a extrage limbajul din fisier 
# il folosesc atat in DFA.py cat si in NFA.py ca sa nu extrag limbaj
def incarca_automat(nume_fisier):
    alfabet = []
    stari = []
    stari_finale = []
    stare_initiala = ""
    tranzitii = {}

    citeste = False

    with open(nume_fisier, "r") as f:
        for linie in f:
            linie = linie.strip()

            if linie == "!start!":
                citeste = True
                continue
            if linie == "!stop!":
                citeste = False
                break # Oprim citirea după !stop!

            if not citeste or not linie or linie.startswith("!"):
                continue

            if "=" in linie and "=>" not in linie:
                cheie, valoare = linie.split("=")
                cheie, valoare = cheie.strip(), valoare.strip()

                if cheie == "A":
                    alfabet = [x.strip() for x in valoare.split(",")]
                elif cheie == "Q":
                    stari = [x.strip() for x in valoare.split(",")]
                elif cheie == "F":
                    stari_finale = [x.strip() for x in valoare.split(",")]
                elif cheie == "S":
                    stare_initiala = valoare.strip()
            
            elif "=>" in linie:
                stanga, dreapta = linie.strip().split("=>")
                stare_noua = dreapta.strip()
                
                params = stanga.replace("(", "").replace(")", "").split()
                if len(params) == 2:
                    stare_sursa, simbol = params

                    cheie = (stare_sursa,simbol)
                    if(cheie not in tranzitii):
                        tranzitii[cheie] = []
                    
                    if(stare_noua not in tranzitii[cheie]):
                        tranzitii[cheie].append(stare_noua)


    return alfabet, stari, stari_finale, stare_initiala, tranzitii


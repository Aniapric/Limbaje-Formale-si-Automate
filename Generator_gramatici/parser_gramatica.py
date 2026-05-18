#aplic aceeasi logica de despachetare in python ca la celelalte parsere
def incarca_cfg(nume_fisier):
    reguli = {}
    start_simbol = ""
    citeste = False

    with open(nume_fisier, "r") as f:
        for linie in f:
            linie = linie.strip()
            if linie == "!start!":
                citeste = True
                continue
            if linie == "!stop!":
                citeste = False
                break
            
            if not citeste or not linie or linie.startswith("!"):
                continue

            if "->" in linie:
                stanga, dreapta = linie.split("->")
                variabila = stanga.strip()
                productie = dreapta.strip().split()
                
                if variabila not in reguli:
                    reguli[variabila] = []
                reguli[variabila].append(productie)
                
            elif "=" in linie:
                cheie, val = linie.split("=")
                if cheie.strip() == "S":
                    start_simbol = val.strip()
    
    return reguli, start_simbol
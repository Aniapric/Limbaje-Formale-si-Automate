#Acesta este parserul pentru PDA

def incarca_pda(nume_fisier):
    alfabet, stari, finale, start = [], [], [], ""
    tranzitii = {}
    citeste = False

    with open(nume_fisier, "r") as f:
        for linie in f:
            linie = linie.strip()
            if linie == "!start!": citeste = True; continue
            if linie == "!stop!": citeste = False; break
            if not citeste or not linie or linie.startswith("!"): continue

            if "=" in linie and "=>" not in linie:
                cheie, val = linie.split("=")
                cheie, val = cheie.strip(), val.strip()
                if cheie == "A": alfabet = [x.strip() for x in val.split(",")]
                elif cheie == "Q": stari = [x.strip() for x in val.split(",")]
                elif cheie == "F": finale = [x.strip() for x in val.split(",")]
                elif cheie == "S": start = val
            
            elif "=>" in linie:
                stanga, dreapta = linie.split("=>")
                # Curat parantezele: (q1 0 .) -> ["q1", "0", "."]
                p_in = stanga.replace("(", "").replace(")", "").split()
                p_out = dreapta.replace("(", "").replace(")", "").split()
                
                if len(p_in) == 3 and len(p_out) == 2:
                    cheie = (p_in[0], p_in[1], p_in[2]) # (stare, char, pop)
                    valoare = (p_out[0], p_out[1])      # (stare_noua, push)
                    
                    if cheie not in tranzitii: tranzitii[cheie] = []
                    tranzitii[cheie].append(valoare)

    return alfabet, stari, finale, start, tranzitii
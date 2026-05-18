from parser_automat import incarca_automat

def ruleaza_dfa(cuvant, start, finale, delta):
    stare_actuala = start
    
    for simbol in cuvant:
        cheie = (stare_actuala, simbol)

        if cheie  in delta:
            stare_actuala = delta[cheie][0]
        else:
            return False
            
    return stare_actuala in finale

if __name__ == "__main__":
    alfabet, stari, finale, start, delta = incarca_automat("limbaj.dfa")
    
    cuvant = input("Introdu un cuvant pentru testare DFA: ")
    rezultat = ruleaza_dfa(cuvant, start, finale, delta)
    
    if rezultat:
        print(f"Cuvantul '{cuvant}' a fost ACCEPTAT.")
    else:
        print(f"Cuvantul '{cuvant}' a fost RESPINS.")
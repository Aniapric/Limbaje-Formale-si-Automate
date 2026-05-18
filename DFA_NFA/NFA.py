from parser_automat import incarca_automat


def epsilon_closure(stari_initiale, delta):
    inchidere = set(stari_initiale)
    
    while True:
        stari_noi = set()
        for stare in inchidere:
            if (stare, '.') in delta:
                for vecina in delta[(stare, '.')]:
                    if vecina not in inchidere:
                        stari_noi.add(vecina)
       
        if not stari_noi:
            break
       
        inchidere.update(stari_noi)
        
    return inchidere

def ruleaza_nfa(cuvant, start, finale, delta):
    stari_actuale = epsilon_closure({start}, delta)
    
    for simbol in cuvant:
        urmatoarele_stari = set()
        
        for s in stari_actuale:
            if (s, simbol) in delta:
              
                for dest in delta[(s, simbol)]:
                    urmatoarele_stari.add(dest)
       
        stari_actuale = epsilon_closure(urmatoarele_stari, delta)
        
        if not stari_actuale:
            return False
    
    for s in stari_actuale:
        if s in finale:
            return True
            
    return False

if __name__ == "__main__":
    alfabet, stari, finale, start, delta = incarca_automat("limbaj.nfa")
    cuvant = input("Cuvant NFA: ")
    
    rezultat = ruleaza_nfa(cuvant, start, finale, delta)
    if rezultat:
        print(f"Cuvântul '{cuvant}' a fost ACCEPTAT.")
    else:
        print(f"Cuvântul '{cuvant}' a fost RESPINS.")
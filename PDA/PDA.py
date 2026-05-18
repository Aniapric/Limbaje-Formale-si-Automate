from parser_automat import incarca_pda

def ruleaza_pda(cuvant, start, finale, delta):
    # (index_cuvant, stare_actuala, stiva)
    # Stiva este reprezentata ca un tuplu 
    configuratii_actuale = {(0, start, ())}
    
    # adaug si posibilitatea de a incepe cu tranzitii epsilon
    configuratii_actuale = exploreaza_epsilon(configuratii_actuale, delta)

    while configuratii_actuale:
        urmatoarele_configuratii = set()
        
        for idx, stare, stiva in configuratii_actuale:
            # Daca am terminat cuvantul si suntem intr-o stare finala
            if idx == len(cuvant) and stare in finale:
                return True
            
            simbol = cuvant[idx] if idx < len(cuvant) else None
            
            # incercam tranzitii cu simbol real
            if simbol:
                urmatoarele_configuratii.update(
                    tranzitie(stare, simbol, stiva, idx + 1, delta)
                )
            
            # tranzitiile epsilon sunt mereu verificate (simbol '.')
            urmatoarele_configuratii.update(
                tranzitie(stare, '.', stiva, idx, delta)
            )
        # conditie ca sa evitam buclele infinite 
        if urmatoarele_configuratii == configuratii_actuale:
            break
        configuratii_actuale = urmatoarele_configuratii

    return False

def tranzitie(stare, simbol, stiva, urmator_idx, delta):
    noi_config = set()
    top = stiva[-1] if stiva else '.'
    
    # verificam doua cazuri de POP: simbolul de sus sau ignore (.)
    for pop_simbol in [top, '.']:
        if (stare, simbol, pop_simbol) in delta:
            for noua_stare, push_simbol in delta[(stare, simbol, pop_simbol)]:
                noua_stiva = list(stiva)
                if pop_simbol != '.': # daca am scos ceva, eliminam de pe stiva
                    noua_stiva.pop()
                if push_simbol != '.': # daca trebuie sa punem ceva
                    noua_stiva.append(push_simbol)
                
                noi_config.add((urmator_idx, noua_stare, tuple(noua_stiva)))
    return noi_config

def exploreaza_epsilon(configuratii, delta):
    #epsilon closure pt PDA
    schimbare = True
    while schimbare:
        schimbare = False
        noi = set()
        for idx, stare, stiva in configuratii:
            gasite = tranzitie(stare, '.', stiva, idx, delta)
            for g in gasite:
                if g not in configuratii:
                    noi.add(g)
                    schimbare = True
        configuratii.update(noi)
    return configuratii

if __name__ == "__main__":
    _, _, finale, start, delta = incarca_pda("limbaj.pda")
    cuvant = input("Introdu cuvant PDA (ex: 0011): ")
    rezultat = ruleaza_pda(cuvant, start, finale, delta)
    
    if rezultat:
        print(f"Cuvântul '{cuvant}' a fost ACCEPTAT.")
    else:
        print(f"Cuvântul '{cuvant}' a fost RESPINS.")
#Functie care genereaza gramatici - reguli 

import random
from parser_gramatica import incarca_cfg

def genereaza_sir(reguli, simbol_curent):
    # daca simbolul nu apare în stanga niciunei reguli, e TERMINAL
    if simbol_curent not in reguli:
        # '.' este simbol  pt sirul vid
        return "" if simbol_curent == "." else simbol_curent
    
    #alegem o productie la intamplare ( folosesc functia random )
    optiuni = reguli[simbol_curent]
    productie_aleasa = random.choice(optiuni)
    
    # construim recursiv sirul 
    rezultat = ""
    for simbol in productie_aleasa:
        rezultat += genereaza_sir(reguli, simbol)
    
    return rezultat

if __name__ == "__main__":
    try:
        reguli, start = incarca_cfg("limbaj.cfg") #in limbaj.cfg scrii regulile
        
        print("--- Rezultate Generare CFG ---")
        for i in range(5): # am pus limita pana la 5 ca sa nu mearga la infinit
            sir_final = genereaza_sir(reguli, start)
            print(f"Derivarea {i+1}: {sir_final if sir_final != '' else 'ε'}")
            
    except FileNotFoundError:
        print("Eroare: Fișierul 'limbaj.cfg' nu a fost găsit!")
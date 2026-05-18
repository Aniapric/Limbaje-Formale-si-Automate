from parser_regex import incarca_regex

def match_regex_manual(pattern, cuvant):
    # Cazul pt siruri goale (Acceptare)
    if not pattern:
        return not cuvant
        
    # Cazul pt un singur caracter in regex
    if len(pattern) == 1:
        return len(cuvant) == 1 and (pattern == '.' or pattern == cuvant)

    # izolam reuniunea '|' doar la nivelul principal (nu in interiorul parantezelor)
    parti = []
    nivel = 0
    curent = ""
    for c in pattern:
        if c == '(': nivel += 1
        elif c == ')': nivel -= 1
        
        if c == '|' and nivel == 0:
            parti.append(curent)
            curent = ""
        else:
            curent += c
    parti.append(curent)
    
    if len(parti) > 1:
        return any(match_regex_manual(p, cuvant) for p in parti)

    # extragem primul token (caracter simplu sau bloc intre paranteze)
    if pattern[0] == '(':
        nivel = 0
        for i, c in enumerate(pattern):
            if c == '(': nivel += 1
            elif c == ')': nivel -= 1
            if nivel == 0:
                break
        
        # daca parantezele nu sunt formatate corect
        if nivel != 0: i = len(pattern) - 1
            
        element = pattern[1:i] # excludem parantezele exterioare
        rest_pattern = pattern[i+1:]
    else:
        element = pattern[0]
        rest_pattern = pattern[1:]

    # verificare daca token ul e urmat de (*)
    are_stea = False
    if rest_pattern and rest_pattern[0] == '*':
        are_stea = True
        rest_pattern = rest_pattern[1:]

    # aplicam logica de potrivire si avansam cuvantul in mod recursiv
    if are_stea:
        # ramura A: Ignoram elementul cu * (0 aparitii)
        if match_regex_manual(rest_pattern, cuvant):
            return True
            
        # ramura B: Consumam din cuvant o potrivire a elementului si pastram * (+1 aparitii)
        for i in range(1, len(cuvant) + 1):
            if match_regex_manual(element, cuvant[:i]) and match_regex_manual(pattern, cuvant[i:]):
                return True
        return False
        
    else:
        # fara *, cautam o singura potrivire (Concatenare)
        for i in range(1, len(cuvant) + 1):
            if match_regex_manual(element, cuvant[:i]) and match_regex_manual(rest_pattern, cuvant[i:]):
                return True
        return False

if __name__ == "__main__":
    try:
        regex = incarca_regex("limbaj.regex") # citim regex-ul
        sir = input(f"Test regex [{regex}]: ") #testam cuvantul
        
        if match_regex_manual(regex, sir):
            print("DA - Acceptat")
        else:
            print("NU - Respins")
    except FileNotFoundError:
        print("Eroare: Lipseste limbaj.regex!")
def incarca_regex(nume_fisier):
    regex_pattern = ""
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

            #considerăm ca prima linie validă după !start! este regex-ul
            regex_pattern = linie
            break 
            
    return regex_pattern
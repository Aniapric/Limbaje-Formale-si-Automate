import networkx as nx # biblioteca standard in python pt crearea si analiza grafurilor

#functie simpla de testare putere de 2
def este_putere_de_2(n):
    """
    Ignoram lungimile mai mici decât 4.
    Deoarece am orientat graful (pt a folosi functia simple_cycles), 
    muchiile au devenit bidirectionale (A->B și B->A).
    Acest lucru creeaza cicluri false de lungime 2. 
    Daca nu am bloca valoarea 2, programul ar raporta fals-pozitive.
    """
    if n < 4:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True

# functie pt a gasi cicluri le lung putere a lui 2
def are_ciclu_putere_de_2(G):
    """
    nx.simple_cycles cauta cicluri elementare ( nu se repeta noduri ) in graf.
    Problema este ca functia functioneaza doar pe grafuri orientate, deci
    ma folosesc de functia to_directed() pt a transforma graful in graf orientat
    """
    cicluri = nx.simple_cycles(G.to_directed())
    for ciclu in cicluri:
        # verificam doar lungimea fiecarui ciclu gasit
        if este_putere_de_2(len(ciclu)):
            return True, len(ciclu) # ne oprim la primul ciclu valid gasit
    return False, None

#functia principala pt rularea experimentului
def ruleaza_experiment(numar_grafuri, numar_noduri):
    satisfacute = 0

    for i in range(numar_grafuri):
        """
        nx.random_regular_graph generează un graf în care toate nodurile 
        au exact gradul 3 (fiecare nod are 3 muchii), respectând ipoteza conjecturii.
        """
        G = nx.random_regular_graph(3, numar_noduri)
        gasit, lungime = are_ciclu_putere_de_2(G)

        if gasit:
            satisfacute += 1
            print("Graful " + str(i + 1) + ": DA - ciclu de lungime " + str(lungime))
        else:
            print("Graful " + str(i + 1) + ": NU - contraexemplu potential!")

    
    print("Satisfac conjectura: " + str(satisfacute) + " din " + str(numar_grafuri))

# experimentul pe 10 grafuri aleatoare cu 16 noduri fiecare
ruleaza_experiment(200, 16)

"""
Am incercat sa folosesc si nx.cycle_basis(G) care extrage o baza de cicluri 
a grafului G , adica un set minim de cicluri care sunt independente 
( din care poti construi orice alt ciclu din graf)
Doar ca imi gasea "contraexemple" ( ex: un ciclu de lungime 8 poate fi format din 
doua cicluri de lungime 5 si l-ar fi luat ca contraexemplu)
Daca am extrage toate ciclurile posibile ar fi ft lent , plus ca numarul total 
de cicluri poate creste foarte mult 
"""
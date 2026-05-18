#Laboratoare LFA (Limbaje Formale și Automate)
Acest repository conține implementările laboratoarelor pentru cursul de Limbaje Formale și Automate. 

Structura repository-ului:
Ierarhia fișierelor este organizată pe categorii tematice:

* DFA_NFA/: Implementări ale automatelor finite deterministe și nedeterministe.

* Generator_gramatici/: Un generator de limbaje bazat pe gramatici formale.

* Joc/: Implementarea unui joc interactiv bazat pe logica automatelor pushdown ("Jaf la Muzeu") .

* PDA/: Implementări de automate finite cu stivă PDA (Pushdown Automaton) pentru recunoașterea limbajelor context-free.

* Regex/: Un motor de potrivire (matching) a expresiilor regulate implementat manual prin backtracking.
  

🏛️ Descrierea jocului "Jaf la Muzeu" (PDA Game)

*Acest joc este o implementare practică a unui Automat Finit cu Stivă (PDA - Pushdown Automaton).

Cum se joacă 🎮 :

Ești un hoț de artă care trebuie să se infiltreze într-un muzeu și să evadeze cu tabloul furat.
Jocul este împărțit în două faze logice care respectă principiul LIFO (Last-In, First-Out):

*Faza de Infiltrare (PUSH): Pe măsură ce treci prin sălile muzeului, fiecare sală este „împinsă” în stiva PDA-ului.Această stivă reține traseul parcurs.

*Faza de Evadare (POP): Pentru a ieși, trebuie să parcurgi traseul invers. Fiecare ieșire dintr-o sală necesită introducerea parolei corecte pentru a „scoate” (pop) sala respectivă din stivă. Dacă stiva se golește, înseamnă că ai evadat cu succes.

Concepte teoretice implementate 📖:

*Alfabetul de intrare : Numele sălilor (Da Vinci, Marie Curie, Mozart).

*Memorie de tip LIFO: PDA-ul folosește o listă (stivă) pentru a forța jucătorul să respecte ordinea inversă a sălilor parcurse.

*Funcția de tranziție : Fiecare tentativă de evadare verifică dacă input-ul utilizatorului coincide cu vârful stivei.

*Acceptarea: Misiunea este considerată îndeplinită (șir acceptat) dacă și numai dacă stiva ajunge să fie goală.

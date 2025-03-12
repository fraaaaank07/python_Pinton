#esempio uso variabili (visconti merda)
print("scrivi il tuo nome, caro utente")
#per poter acquisire qualcosa che digita l'utente uso la funzione "input"
NomeUser = input()

print("benvenuto", NomeUser)

#faccio la stessa cosa in modo piu veloce passando come argomento all'input una frase
#funzione (argomento) - - > tutto questo si chiama firma del METODO 
CognomeUser = input("scrivi il tuo cognome")
print("il tuo cognome è", CognomeUser)
#tutto ciò che scrive un utente viene considerato testo COMPRESI I NUMERI
print("----------------numeri-----------------")
Num1=int(input("scrivi un nummero"))
Num2=int(input("scrivi un altro nummero"))
somma = Num1 + Num2
print("la somma vale:", somma)
#esempio
Num3 = int("3")
Num4 = int("4")
somma2 = Num3 + Num4
print (somma2)
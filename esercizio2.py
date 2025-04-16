numeri = (12, 3, 7, 24, 5, 18, 9, 10, 15, 2)

numeri_pari = [n for n in numeri if n % 2 == 0]
print("Numeri pari:", numeri_pari)

somma_dispari = sum(n for n in numeri if n % 2 != 0)
print("Somma dei numeri dispari:", somma_dispari)

massimo = max(numeri)
print("Numero massimo:", massimo)

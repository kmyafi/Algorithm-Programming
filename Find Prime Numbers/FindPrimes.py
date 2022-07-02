n = input("Masukan angka: ")
str_n = str(n)
angka = []
prima = []

for k in range(1, len(n)+1):
    for i in range(len(n)-k+1):
        angka.append(int(str_n[i : i + k]))

angka = list(dict.fromkeys(angka))

def prime(n): 
    if n <= 0:
        return "Not defined" 
    elif n == 1:
        return "Not prime" 
    for i in range(2, n): 
        if n%i == 0:
            return "not prime" 
    return "prime"

for a in angka:
    x = prime(a)
    if x == "prime":
        prima.append(a)

print(prima)
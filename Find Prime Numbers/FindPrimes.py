from math import sqrt

n = input("Masukan angka: ")
str_n = str(n)
angka = []
prima = []

for k in range(1, len(n)+1):
    for i in range(len(n)-k+1):
        angka.append(int(str_n[i : i + k]))

angka = list(dict.fromkeys(angka))

def prime(n: int): 
    """
    Function that checks whether an integer number is prime or not.
    A prime number is a number which has two distinct divisors: itself and 1.
   
    @param n: int 
    @return: str
    
    """
    # first check if n is not negative.
    if n <= 0:
        return "Not defined" 
    
    # 1 is not a prime
    # note that 1 have only 1 distinct divisor which is itself.
    elif n == 1:
        return "Not prime" 
    
    # if n >= 2 then iterate through all numbers from 2 to the square root of n
    # to check if there is another number that divide n
    # note that we stopped at sqrt(n) since (i divide n) -> (i/n divide n) and either one of the two (i & n/i) is below sqrt(n)
    for i in range(2, int(sqrt(n)) + 1):
        # i divide n is equivalent to n%i == 0
        if n%i == 0:
            return "not prime" 
    return "prime"

for a in angka:
    x = prime(a)
    if x == "prime":
        prima.append(a)

print(prima)

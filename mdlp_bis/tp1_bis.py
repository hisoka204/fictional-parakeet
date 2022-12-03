def divisible(nbr):
    for i in range(0, nbr):
        if(i % 3 == 0):
            if(i % 5 == 0):
                print("Trois et Cinq")
            else:
                print("Trois")
        elif(i % 5 == 0):
            print("cinq")
        else:
            print(i)
            
divisible(101)

def fib_recursive(n):
    lst = [0, 1]

    for i in range(2, n):
        lst.append(lst[i-1] + lst[i - 2])
    
    return lst

print(fib_recursive(50))

def fib_n(n):
    m = n+1
    fib_n = int(1 / 5**0.5 * (((1 + 5**0.5) / 2)**n - ((1 - 5**0.5) / 2)**n))
    fib_m = int(1 / 5**0.5 * (((1 + 5**0.5) / 2)**m - ((1 - 5**0.5) / 2)**m))

    print(n, fib_n)
    print(m, fib_m)
    
def fib_get():
    n = int(input("entrez un nombre n:"))
    fib_n(n)
    
fib_get()

def fib_dico(n):
    dico = {}
    dico[0] = [0, 0]
    dico[1] = [1, 1]

    for i in range(2, n+1):
        j = i + 1
        fib_i = int(1 / 5**0.5 * (((1 + 5**0.5) / 2)**i - ((1 - 5**0.5) / 2)**i))
        fib_j = int(1 / 5**0.5 * (((1 + 5**0.5) / 2)**j - ((1 - 5**0.5) / 2)**j))

        dico[i] = [fib_i, fib_j / fib_i]

    return dico

def fib_dico_get():
    n = int(input("entrez un nombre n:"))
    dic = fib_dico(n)

    m = int(input("entrez un nombre m < n:"))
    print(m, dic[m][0], dic[m][1])
    
fib_dico_get()
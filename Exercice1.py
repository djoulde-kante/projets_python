def fibonacci_superieur(n):
    if n < 1:
        return 1
    
    f1, f2 = 1, 1
    while f2 <= n:
        f1, f2 = f2, f1 + f2
    return f2

def main():
    for n in [75, 50, 100]:
        resultat = fibonacci_superieur(n)
        print(f"Premier nombre de Fibonacci supérieur à {n}: {resultat}")

if __name__ == "__main__":
    main()

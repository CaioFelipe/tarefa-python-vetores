def main():
    print("--- Exercício 01 ---")
    vetor = []
    for i in range(10):
        while True:
            try:
                num = int(input(f"Digite o {i+1}º número inteiro: "))
                vetor.append(num)
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número inteiro.")
    
    print("\nVetor armazenado:")
    print(vetor)

if __name__ == "__main__":
    main()

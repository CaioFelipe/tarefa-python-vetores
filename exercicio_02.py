def main():
    print("--- Exercício 02 ---")
    vetor = []
    for i in range(10):
        while True:
            try:
                num = float(input(f"Digite o {i+1}º número: "))
                vetor.append(num)
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número (pode ser decimal).")
    
    soma = sum(vetor)
    print("\nOs valores armazenados no vetor são:", vetor)
    print(f"A soma de todos os valores é: {soma}")

if __name__ == "__main__":
    main()

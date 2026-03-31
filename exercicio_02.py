def main():
    print("--- Exercício 02 ---")
    vetor = [0.0] * 10
    for i in range(10):
        while True:
            try:
                num = float(input(f"Digite o {i+1}º número: "))
                vetor[i] = num
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número (pode ser decimal).")

    soma = 0
    for i in range(10):
        soma = soma + vetor[i]

    print("\nOs valores armazenados no vetor são:", vetor)
    print(f"A soma de todos os valores é: {soma}")

if __name__ == "__main__":
    main()

def main():
    print("--- Exercício 07 ---")
    vetor = []
    
    print("Digite 20 números inteiros:")
    for i in range(20):
        while True:
            try:
                num = int(input(f"{i+1}º elemento: "))
                vetor.append(num)
                break
            except ValueError:
                print("Valor inválido. Insira um número inteiro.")

    # Exibindo o vetor inteiro
    print("\nVetor lido:", vetor)

    # Exibe a contagem total de elementos (que sempre será 20 conforme o laço)
    total_elementos = len(vetor)
    print(f"Total de valores existentes no vetor: {total_elementos}")
    
    # Exibe também quantos valores DISTINTOS (únicos) existem como extra,
    # caso o enunciado implicasse isso.
    valores_unicos = len(set(vetor))
    print(f"Quantidade de valores únicos no vetor: {valores_unicos}")

if __name__ == "__main__":
    main()

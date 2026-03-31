def main():
    print("--- Exercício 07 ---")
    vetor = [0] * 20
    print("Digite 20 números inteiros:")
    for i in range(20):
        while True:
            try:
                num = int(input(f"{i+1}º elemento: "))
                vetor[i] = num
                break
            except ValueError:
                print("Valor inválido. Insira um número inteiro.")

    print("\nVetor lido:", vetor)
    total_elementos = 20
    print(f"Total de valores existentes no vetor: {total_elementos}")
    valores_unicos = 0
    for i in range(20):
        eh_unico = True
        for j in range(i):
            if vetor[i] == vetor[j]:
                eh_unico = False
                break
        if eh_unico:
            valores_unicos = valores_unicos + 1

    print(f"Quantidade de valores únicos no vetor: {valores_unicos}")

if __name__ == "__main__":
    main()

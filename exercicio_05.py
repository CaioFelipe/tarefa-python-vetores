def main():
    print("--- Exercício 05 ---")
    vetor = []
    
    print("Digite 15 números inteiros para o vetor:")
    for i in range(15):
        while True:
            try:
                num = int(input(f"Posição {i+1}: "))
                vetor.append(num)
                break
            except ValueError:
                print("Por favor, digite um número inteiro.")
                
    while True:
        try:
            x = int(input("\nDigite o valor X que deseja buscar: "))
            break
        except ValueError:
            print("Por favor, digite um valor inteiro para X.")

    # Verifica quantas vezes X aparece no vetor
    ocorrencias = vetor.count(x)
    
    print("\nVetor:", vetor)
    if ocorrencias > 0:
        print(f"O valor {x} está presente no vetor.")
        print(f"Ele aparece {ocorrencias} vez(es).")
    else:
        print(f"O valor {x} NÃO está presente no vetor.")

if __name__ == "__main__":
    main()

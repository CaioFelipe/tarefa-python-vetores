def main():
    print("--- Exercício 04 ---")
    vetor = []
    
    for i in range(10):
        while True:
            try:
                num = int(input(f"Digite o {i+1}º número inteiro: "))
                vetor.append(num)
                break
            except ValueError:
                print("Por favor, digite um número inteiro.")

    multiplicacao_pares = 1
    soma_impares = 0
    tem_par = False
    
    for num in vetor:
        if num % 2 == 0:
            multiplicacao_pares *= num
            tem_par = True
        else:
            soma_impares += num

    # Se não houver números pares, a multiplicação exibida seria 1, porém faz mais sentido ser 0
    if not tem_par:
        multiplicacao_pares = 0
        
    print("\nResultados:")
    print("Vetor digitado:", vetor)
    print("Multiplicação dos elementos pares:", multiplicacao_pares)
    print("Soma dos elementos ímpares:", soma_impares)

if __name__ == "__main__":
    main()

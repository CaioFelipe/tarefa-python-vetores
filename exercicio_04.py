def main():
    print("--- Exercício 04 ---")
    vetor = [0] * 10
    
    for i in range(10):
        while True:
            try:
                num = int(input(f"Digite o {i+1}º número inteiro: "))
                vetor[i] = num
                break
            except ValueError:
                print("Por favor, digite um número inteiro.")

    multiplicacao_pares = 1
    soma_impares = 0
    tem_par = False
    
    for i in range(10):
        if vetor[i] % 2 == 0:
            multiplicacao_pares = multiplicacao_pares * vetor[i]
            tem_par = True
        else:
            soma_impares = soma_impares + vetor[i]
            
    if not tem_par:
        multiplicacao_pares = 0
        
    print("\nResultados:")
    print("Vetor digitado:", vetor)
    print("Multiplicação dos elementos pares:", multiplicacao_pares)
    print("Soma dos elementos ímpares:", soma_impares)

if __name__ == "__main__":
    main()

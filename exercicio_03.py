def main():
    print("--- Exercício 03 ---")
    vetor = [0.0] * 20 
    
    while True:
        try:
            primeiro_valor = float(input("Digite a 1ª posição (pode ser número real): "))
            break
        except ValueError:
            print("Valor inválido.")

    vetor[0] = primeiro_valor
    
    for i in range(1, 20):
        vetor[i] = vetor[i - 1] * 2
        
    print("\nVetor após preenchimento (20 posições):")
    for i in range(20):
        print(f"Posição {i+1}: {vetor[i]}")

if __name__ == "__main__":
    main()

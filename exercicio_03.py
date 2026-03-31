def main():
    print("--- Exercício 03 ---")
    vetor = []
    
    while True:
        try:
            primeiro_valor = float(input("Digite a 1ª posição (pode ser número real): "))
            break
        except ValueError:
            print("Valor inválido.")

    vetor.append(primeiro_valor)
    
    for i in range(1, 20):
        # Cada posição é o dobro da anterior
        proximo_valor = vetor[-1] * 2
        vetor.append(proximo_valor)
        
    print("\nVetor após preenchimento (20 posições):")
    for i, valor in enumerate(vetor):
        print(f"Posição {i+1}: {valor}")

if __name__ == "__main__":
    main()

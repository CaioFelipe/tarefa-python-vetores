def ler_vetor(nome_vetor):
    vetor = []
    print(f"\nPreenchendo o vetor {nome_vetor} (10 posições):")
    for i in range(10):
        while True:
            try:
                num = float(input(f"Posição {i+1} de {nome_vetor}: "))
                vetor.append(num)
                break
            except ValueError:
                print("Valor inválido. Digite um número.")
    return vetor

def main():
    print("--- Exercício 08 ---")
    vetor_1 = ler_vetor("1")
    vetor_2 = ler_vetor("2")
    
    vetor_3 = []
    
    # Multiplicando os elementos de mesmo índice
    for i in range(10):
        resultado = vetor_1[i] * vetor_2[i]
        vetor_3.append(resultado)
        
    print("\nResultados:")
    print("Vetor 1:", vetor_1)
    print("Vetor 2:", vetor_2)
    print("Vetor 3 (Multiplicação dos índices correspondentes):")
    print(vetor_3)

if __name__ == "__main__":
    main()

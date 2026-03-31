def ler_vetor(nome_vetor):
    vetor = [0.0] * 10
    print(f"\nPreenchendo o vetor {nome_vetor} (10 posições):")
    for i in range(10):
        while True:
            try:
                num = float(input(f"Posição {i+1} de {nome_vetor}: "))
                vetor[i] = num
                break
            except ValueError:
                print("Valor inválido. Digite um número.")
    return vetor

def main():
    print("--- Exercício 08 ---")
    vetor_1 = ler_vetor("1")
    vetor_2 = ler_vetor("2")
    vetor_3 = [0.0] * 10
    for i in range(10):
        vetor_3[i] = vetor_1[i] * vetor_2[i]
        
    print("\nResultados:")
    print("Vetor 1:", vetor_1)
    print("Vetor 2:", vetor_2)
    print("Vetor 3 (Multiplicação dos índices correspondentes):")
    print(vetor_3)

if __name__ == "__main__":
    main()

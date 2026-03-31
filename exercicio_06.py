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
                print("Valor inválido.")
    return vetor

def main():
    print("--- Exercício 06 ---")
    vec_a = ler_vetor("A")
    vec_b = ler_vetor("B")
    
    vec_c = []
    
    # Intercalando os elementos
    for i in range(10):
        vec_c.append(vec_a[i])
        vec_c.append(vec_b[i])
        
    print("\nResultados:")
    print("Vetor A:", vec_a)
    print("Vetor B:", vec_b)
    print("Vetor C (A e B intercalados):")
    print(vec_c)

if __name__ == "__main__":
    main()

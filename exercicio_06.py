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
                print("Valor inválido.")
    return vetor

def main():
    print("--- Exercício 06 ---")
    vec_a = ler_vetor("A")
    vec_b = ler_vetor("B")
    vec_c = [0.0] * 20 
    pos = 0
    for i in range(10):
        vec_c[pos] = vec_a[i]
        pos = pos + 1
        vec_c[pos] = vec_b[i]
        pos = pos + 1
        
    print("\nResultados:")
    print("Vetor A:", vec_a)
    print("Vetor B:", vec_b)
    print("Vetor C (A e B intercalados):")
    print(vec_c)

if __name__ == "__main__":
    main()

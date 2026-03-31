import os

def ler_vetor_float(nome_vetor):
    """Função auxiliar para ler vetores de números reais (utilizada nos exercícios 6 e 8)."""
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

def exercicio_01():
    print("\n--- Exercício 01 ---")
    vetor = [0] * 10
    for i in range(10):
        while True:
            try:
                num = int(input(f"Digite o {i+1}º número inteiro: "))
                vetor[i] = num
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número inteiro.")
    
    print("\nVetor armazenado:")
    print(vetor)

def exercicio_02():
    print("\n--- Exercício 02 ---")
    vetor = [0.0] * 10
    for i in range(10):
        while True:
            try:
                num = float(input(f"Digite o {i+1}º número: "))
                vetor[i] = num
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número (pode ser decimal).")

    soma = sum(vetor)
    print("\nOs valores armazenados no vetor são:", vetor)
    print(f"A soma de todos os valores é: {soma}")

def exercicio_03():
    print("\n--- Exercício 03 ---")
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

def exercicio_04():
    print("\n--- Exercício 04 ---")
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

def exercicio_05():
    print("\n--- Exercício 05 ---")
    vetor = [0] * 15
    
    print("Digite 15 números inteiros para o vetor:")
    for i in range(15):
        while True:
            try:
                num = int(input(f"Posição {i+1}: "))
                vetor[i] = num
                break
            except ValueError:
                print("Por favor, digite um número inteiro.")
                
    while True:
        try:
            x = int(input("\nDigite o valor X que deseja buscar: "))
            break
        except ValueError:
            print("Por favor, digite um valor inteiro para X.")

    ocorrencias = vetor.count(x)
    
    print("\nVetor:", vetor)
    if ocorrencias > 0:
        print(f"O valor {x} está presente no vetor.")
        print(f"Ele aparece {ocorrencias} vez(es).")
    else:
        print(f"O valor {x} NÃO está presente no vetor.")

def exercicio_06():
    print("\n--- Exercício 06 ---")
    vec_a = ler_vetor_float("A")
    vec_b = ler_vetor_float("B")
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

def exercicio_07():
    print("\n--- Exercício 07 ---")
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
    tamanho = len(vetor)
    print("\nTamanho:", tamanho)

def exercicio_08():
    print("\n--- Exercício 08 ---")
    vetor_1 = ler_vetor_float("1")
    vetor_2 = ler_vetor_float("2")
    vetor_3 = [0.0] * 10
    for i in range(10):
        vetor_3[i] = vetor_1[i] * vetor_2[i]
        
    print("\nResultados:")
    print("Vetor 1:", vetor_1)
    print("Vetor 2:", vetor_2)
    print("Vetor 3 (Multiplicação dos índices correspondentes):")
    print(vetor_3)

def menu():
    while True:
        print("\n" + "="*30)
        print("      MENU DE EXERCÍCIOS")
        print("="*30)
        print("1. Exercício 01")
        print("2. Exercício 02")
        print("3. Exercício 03")
        print("4. Exercício 04")
        print("5. Exercício 05")
        print("6. Exercício 06")
        print("7. Exercício 07")
        print("8. Exercício 08")
        print("0. Sair")
        print("-" * 30)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            exercicio_01()
        elif opcao == '2':
            exercicio_02()
        elif opcao == '3':
            exercicio_03()
        elif opcao == '4':
            exercicio_04()
        elif opcao == '5':
            exercicio_05()
        elif opcao == '6':
            exercicio_06()
        elif opcao == '7':
            exercicio_07()
        elif opcao == '8':
            exercicio_08()
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

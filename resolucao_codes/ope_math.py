def main():
    print("Bem-vindo à Calculadora!")
    
    # Solicita dois números ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    while True:
        # Exibe o menu de operações
        print("\nEscolha uma operação:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Sair")
        
        # Solicita a escolha do usuário
        escolha = input("Digite o número da operação desejada: ")
        
        # Realiza a operação escolhida
        if escolha == '1':
            resultado = num1 + num2
            print(f"O resultado da adição é: {resultado}")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"O resultado da subtração é: {resultado}")
        elif escolha == '3':
            resultado = num1 * num2
            print(f"O resultado da multiplicação é: {resultado}")
        elif escolha == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"O resultado da divisão é: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        elif escolha == '5':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
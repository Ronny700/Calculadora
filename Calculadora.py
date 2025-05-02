def calcular (num1, num2, operacao):
    
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 !=0:
            return num1 / num2
        else:
            return "Erro: divisão por zero"
    else:
        return "Operação inválida"
    
while True:
    print ("===== Calculadora Simples =====")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input ("Escolha a opração (+,/,*,/): ")

        resultado = calcular(num1,num2,operacao)
        print ("Resultado: ", resultado)

    except ValueError:
        print("Por favor, insira números válidos.")
        continue

    continuar = input("\nDeseja fazer outro cálculo? (sim/não): ").strip().lower()
    if continuar != 'sim':
        print("Até logo! :)")
        break
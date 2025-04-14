num = input("Digite um número de 5 dígitos: ")

# Verificar se o número tem 5 dígitos
while len(num) != 5 or not num.isdigit():
    print("Insira um número com apenas 5 dígitos.")
    num = input("Digite novamente: ")

# Exibir os números separados por três espaços
for digito in num:
    print(digito, end="   ")

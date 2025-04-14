def caixa(lado):
    for i in range(lado):
        print('* ' * lado)
    print()

def oval(altura, largura):
    for i in range(altura):
        for j in range(largura):
            dist = ((i - altura/2)**2) / (altura/2)**2 + ((j - largura/2)**2) / (largura/2)**2
            if dist <= 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    print()

def seta(tamanho):
    for i in range(tamanho):
        print(' ' * (tamanho - i - 1) + '* ' * (i + 1))
    for i in range(tamanho):
        print(' ' * (tamanho - 1) + '*')
    print()

def losango(tamanho):
    for i in range(tamanho):
        print(' ' * (tamanho - i - 1) + '* ' * (i + 1))
    for i in range(tamanho - 2, -1, -1):
        print(' ' * (tamanho - i - 1) + '* ' * (i + 1))
    print()

# Chamadas de exemplo
print("Caixa:")
caixa(5)

print("Oval:")
oval(7, 15)

print("Seta:")
seta(5)

print("Losango:")
losango(5)


while True:
    try:
        senha = int(input('digite uma senha que leva 3 digitos de 100 a 500: '))
        if(100 <= senha <=500):
            break
        print('O número deve ter 3 dígitos de 100 a 500')
    except ValueError:
        print('Não foi digitado um número')

idade = int(input('Qual e sua idade: '))
if(0 <= idade <= 12):
    print('Criança')
elif(13 <= idade <= 18):
    print('Adolecente')
elif(19 <= idade <= 59):
    print('Adulto')
elif( idade > 59):
    print('Idoso')



primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'O {primeiro_valor} é maior que o {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'O {segundo_valor} valor é maior que o {primeiro_valor}')
else:
    print('Os valores são iguais')
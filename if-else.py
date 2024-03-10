# Condicionais - if/ elif / else
# ------------- se / senão se/ senão

entrada = str(input('Você quer "entrar" ou "sair" ?'))
# em js const entrada = prompt('Você quer "entrar" ou "sair" ?')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você precisa digitar "entrar" ou "sair"')



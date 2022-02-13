"""Demonstrativo Mensal de Pagamento"""

print('\033[1;32m========= HOLERITE =========')
print('=== PAGAMENTO MENSALISTA === \033[m\n')

"""DADOS INICIAIS"""
nome = str(input('Funcionario: ')).strip()
salarioBaseMes = float(input('Salario base: '))
diasTrabMes: int = int(input('Dias trabalhado mês: '))
print('\n')

"""ADIANTAMENTO"""
print('\033[1;32mPagamento adiantamento quinzenal - 40% salário base \033[m')
adto = str(input('Recebe adiantamento quinzenal [SIM/NÃO]: ')).upper()
if adto == 'SIM' and diasTrabMes <= 14:
    print('\033[1;31mNão recebe adto quinzenal, dias trabalhados insuficientes para receber pagamento \033[m')
elif adto == 'SIM' and diasTrabMes >= 15:
    valor = (((salarioBaseMes / 30) * diasTrabMes) * 40) / 100
    print('Adiantamento quinzenal R$ {:.2f}'.format(valor))
elif adto == 'NÃO':
    print('\033[1;31mNão tem pgto adto quinzenal \033[m')
else:
    print('\033[1;31mOPÇÃO ERRADA. SEM CALCCULO DE ADTO SALÁRIO.')
print('\n')


print('\033[1;32mSALARIO FAMILIA:\033[m \033[1;31mValor pago para remunerações até R$ 1503,25. Cota por filho R$ 51,27 \033[m')
if salarioBaseMes <= 1503.25:
    salarioFam = depenSalarioFam * 51.27
    print('Salario Familia: {:.2f}'.format(salarioFam))
elif salarioBaseMes >= 1503.26:
    print('\033[1;32mNão recebe salario familia \n \033[m')

"""INSS"""
inss = float
print('\033[1;32mDedução INSS\033[m')
if 0 <= salarioBaseMes <= 1100.00:
    inss = (salarioBaseMes * 7.5) / 100

elif 1100.01 <= salarioBaseMes <= 2203.48:
    inss = (((salarioBaseMes - 1100.00) * 9) / 100) + 82.50

elif 2203.49 <= salarioBaseMes <= 3305.22:
    inss = (((salarioBaseMes - 2203.48) * 12) / 100) + 181.81

elif 3305.23 <= salarioBaseMes <= 6433.57:
    inss = (((salarioBaseMes - 3305.23) * 14) / 100) + 314.02

elif salarioBaseMes >= 6433.58:
    inss = 751.99

print('Desconto do INSS é de R$ {:.2f}'.format(inss))
liquido:float = salarioBaseMes - inss
print('Liquido R$ {:.2f} \n'.format(liquido))

"""IR"""
ir = float
liquido1 = float
print('\033[1;32mDedução IR\033[m')
dependente = int(input('Quantos dependetes de IR: '))
if dependente >= 1:
    ir = dependente * 189.59
    print('Dedução IR por {} dependente é de R$ {}'.format(dependente, ir))
    liquido1 = liquido - ir
    print('Liquido R$ {:.2f}'.format(liquido1))

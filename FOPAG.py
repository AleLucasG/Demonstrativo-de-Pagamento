"""Demonstrativo Mensal de Pagamento"""

print('\033[1;32m========= HOLERITE =========')
print('=== PAGAMENTO MENSALISTA === \033[m\n')

"""DADOS INICIAIS"""
nome = str(input('Funcionario: ')).strip()
salarioBaseMes = float(input('Salario base: '))
diasTrabMes: int = int(input('Dias trabalhado mês: '))
dependente = int(input('Quant. Dependenete IRRF: '))
depenSalarioFam = int(input('Quant. Dependnete Salário Fámilia até 14 anos: '))
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
print('\n')

print('\033[1;32mSALARIO FAMILIA: Valor pago para remunerações até R$ 1503,25. Cota por filho R$ 51,27 \033[m')
if salarioBaseMes <= 1503.25:
    salarioFam = depenSalarioFam * 51.27
    print('Salario Familia: {:.2f}'.format(salarioFam))
elif salarioBaseMes >= 1503.26:
    print('\033[1;32mNão recebe salario familia \033[m')
print('\n')

"""INSS"""
print('\033[1;32mDedução INSS\033[m')
if salarioBaseMes <= 1100.00:
    inss = (salarioBaseMes * 7.5) / 100
elif salarioBaseMes >= 1100.01 and <= 2203.48:
    inss = ((salarioBaseMes * 9) / 100) + 82.50
elif salarioBaseMes >= 2203.49 and <= 3305.22:
    inss = ((salarioBaseMes * 12) / 100) + 181.81
elif salarioBaseMes >= 3305.23 and <= 6433.57:
    inss = ((salarioBaseMes * 14) / 100) + 314.02
elif salarioBaseMes >= 6433.58:
    inss = 751.99
print(''.format(inss))

"""Demonstrativo Mensal de Pagamento"""

print('\033[1;32m========= HOLERITE =========')
print('=== PAGAMENTO MENSALISTA === \033[m\n')

"""DADOS INICIAIS"""
nome = str(input('Funcionario: ')).strip()
salarioBaseMes = float(input('Salario base: '))
diasTrabMes: int = int(input('Dias trabalhado mês: '))
dependente = int(input('Quant. Dependenete IRRF: '))
depenSalarioFam = int(input('Quant. Dependnete Salário Fámilia:  '))
print('\n')

"""ADIANTAMENTO"""
print('\033[1;32mPagamento adiantamento quinzenal - 40% salário base \033[m')
adto = str(input('Recebe adiantamento quinzenal [SIM/NÃO]: ')).upper()
if adto == 'SIM' and diasTrabMes <= 14:
    print('\033[1;31mNão recebe adto quinzenal, dias trabalhados insuficiente para pagamento \033[m')
else:
      if adto == 'SIM' and diasTrabMes >= 15:
        valor = (((salarioBaseMes / 30) * diasTrabMes) * 40) / 100
        print('Adiantamento quinzenal R$ {:.2f}'.format(valor))
      else:
          if adto == 'NÃO':
              print('\033[1;31mNão tem pgto adto quinzenal \033[m')

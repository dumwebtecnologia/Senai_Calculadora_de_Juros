# apresentaçao
print('\n\t\t CALCULADORA DE JUROS SIMPLES \n\n  ')

# entrada

print('')
N1 = float(input('\n\t\t\tValor do capital - '))

print('')
N2 = float(input('\n\t\t\tValor da taxa - '))

print('')
N3 = float(input('\n\t\t\tprazo  - '))

# processamento

total = N1 * N2 * N3
total2 = total / 100

# saida

print('\t\t\t\n\tO juros a ser cobrado corresponde  \n')
print(f'\n\t\t{total2}')
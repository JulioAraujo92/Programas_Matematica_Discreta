print('BEM VINDO AO CONVERSOR DE DECIMAL PARA BINÁRIO')
print('\n')
num = int(input('Digite um número para começar a conversão: '))
quo = num
string = ""

while num != 0:
  resto = str(num % 2)
  num = num // 2
  string += resto
  if num == 1:
    string = '1' + string
string = string + " "
invertido = ""
for i in range(len(string) - 1, 0, -1):
  invertido = invertido + string[i]
print('\n')
print(f' O número {quo} em binário é {invertido}')
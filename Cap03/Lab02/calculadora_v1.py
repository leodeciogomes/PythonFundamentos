# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

def soma(s1,s2):
    soma_resultado = s1+s2
    print(s1,'+', s2, '=', soma_resultado )

def subtracao(sub1,sub2):
    sub_resultado = sub1 - sub2
    print(sub1,'-', sub2, '=', sub_resultado )

def multiplicacao(mult1,mult2):
    mult_resultado = mult1 * mult2
    print(mult1,'x', mult2, '=', mult_resultado )

def divisao(div1,div2):
    div_resultado = div1 / div2
    print(div1,'/', div2, '=', div_resultado )

print("\n******************* Python Calculator *******************\n")

print('Selecione a operação desejada:\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n')

calculadora = 0

while calculadora not in ('1','2','3','4'):
    calculadora = operacao = input('Digite sua opção (1/2/3/4):\n')
    if operacao not in ('1','2','3','4'):
        print('Você digitou um comando inválido. Digite novamente o número da operação desejada:\n')

n1 = int(input('Digite o primeiro número:\n'))
n2 = int(input('Digite o segundo número:\n'))

if operacao == '1':
    soma(n1,n2)
elif operacao == '2':
    subtracao(n1,n2)
elif operacao == '3':
    multiplicacao(n1,n2)
else:
    divisao(n1,n2)


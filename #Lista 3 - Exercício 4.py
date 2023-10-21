#Lista 3 - Exercício 4

a = int(input('Informe o lado A de um triângulo: '))
b = int(input('Informe o lado B de um triângulo: '))
c = int(input('Informe o lado C de um triângulo: '))
while a <=0 or b <=0 or c <=0:
    print('Não é possível escolher valor negativo ou nulo para um dos lados.')
    a = int(input('Informe o lado A de um triângulo: '))
    b = int(input('Informe o lado B de um triângulo: '))
    c = int(input('Informe o lado C de um triângulo: '))
if a<b+c and b<c+a and c<a+b:
    print(f'O perímetro do triângulo é de: {a+b+c}')
else:
    print('Para formar um triângulo, cada suposto lado deve ser menor do que a soma dos outros dois lados.')
    

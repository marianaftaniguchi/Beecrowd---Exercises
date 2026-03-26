# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

N = int(input())

a = N // 100 
x = N % 100
b = (x) // 50 
c = ((x) % 50) // 20
d = (((x) % 50) % 20) // 10
e = ((((x) % 50) % 20) % 10) // 5
f = (((((x) % 50) % 20) % 10) % 5) // 2
g = ((((((x) % 50) % 20) % 10) % 5) % 2) // 1

print (N)
print (a, "nota(s) de R$ 100,00") 
print (b, "nota(s) de R$ 50,00")
print (c, "nota(s) de R$ 20,00")
print (d, "nota(s) de R$ 10,00")
print (e, "nota(s) de R$ 5,00")
print (f, "nota(s) de R$ 2,00")
print (g, "nota(s) de R$ 1,00") 
# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
# se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
# se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
# se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

A, B, C= input().split (" ")

A = float (A)
B = float (B)
C = float (C)

lista = [A, B, C]

lista.sort(reverse=True)

A, B, C = lista

if A >= B + C:
 print ("NAO FORMA TRIANGULO") 

else: 

    if A ** 2 ==B **2 + C ** 2:
        print ("TRIANGULO RETANGULO")

    elif A ** 2 > B ** 2 + C ** 2:
        print ("TRIANGULO OBTUSANGULO")

    elif A ** 2 < B ** 2 + C ** 2:
        print ("TRIANGULO ACUTANGULO") 

if A == B == C:
  print ('TRIANGULO EQUILATERO')

else: 
   
     if A == B: 
         print ('TRIANGULO ISOSCELES')

     elif C == B:
         print ('TRIANGULO ISOSCELES')

     elif A == C:
         print ('TRIANGULO ISOSCELES')












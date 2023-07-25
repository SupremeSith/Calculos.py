import os 
A = 1
B = 2 
C = 3
D = 4 

x= int(input("Insira o metodo escolhido para fazer sua conta!  \n 1-Adição \n 2-Multiplicação \n 3-Divisão \n 4-Subtração \n \n "))
if A == 1:
        print("Adição escolhida com sucesso! \n ")
        int(input("Insira os números para fazer a conta \n \n Escreva aqui:"))
else:
        if B == 2:
            print("Multiplicação escolhida com sucesso! \n ")
            int(input("Insira os números para fazer a conta \n \n Escreva aqui:"))
        else:
               if C == 3:
                print("Divisão escolhida com sucesso! \n")
                int(input("Insira os números para fazer a conta \n \n Escreva aqui:"))
               else:
                     if D == 4:
                        print("Subtração escolhida com sucesso! \n ")
                        int(input("Insira os números para fazer a conta \n \n Escreva aqui:"))
y = input("Deseja sair Agora?  \n s - sim \n n -não \n")
if y == "s":
        x =3
else:
        print("Opção Invalida")
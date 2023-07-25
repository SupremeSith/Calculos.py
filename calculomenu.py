import os 
def menu():
    print('''
            MENU:
            [1] - Numeros Primos
            [2] - Números Descrecentes
            [3] - Mediana de 3 Números
            [4] - Sair
        ''')
    str(input('Escolha uma opção: '))
numerosprimos= "1"
numerosdecrescentes= "2"
medianade3numeros= "3"
sair= "4"
menu()
if(numerosprimos):
    while (numerosprimos):
        n = int(input(" Digite 1 para proceder em Lógicas: \n Digite 0 para Voltar: \n  "))
        if (n != 0):
                    n = int(input("Digite um número inteiro:"))
                    cont = 0
                    i = 0 
                    while i <= n or cont <2 :
                         i = i + 1
                         x = n % i 
                         if x == 0:
                              cont = cont + 1 

                              if cont <= 2:
                                   print("primo")
                              else:
                                   print("não é primo")
                    n = int(input("Número Primo Calculado com suceso ! \n (0 = Voltar ao menu):  \n ")) 
                    if (n == 0):
                          os.system("pause")
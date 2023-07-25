import os
x = 1
z = 1
while x == 1:
    print("        Sistema Iniciado")
    a = input("    \n         [MENU]: \n  \n       [1] - Número primo \n \n       [2] - Número decrescente \n \n       [3] - Mediana de 3 números \n    \n       [4] - Sair \n \n")
    z = 1
    while z == 1:
        b = 1
        if a == "1":
            os.system ("cls")
            print("Número primo selecionado \n") 
            lógica = input("[1] Prosseguir para a lógica \n \n[2] Refazer \n \n[3] Voltar  \n \n") 
            if lógica == "1":
                b = int(input("Digite o valor desejado \n"))
                if (b % 3 > 0 and b % 5 > 0 and b % 7 > 0 and b % 2 > 0 and b > 2): 
                    print ("O número é primo.")
                else:
                    print("O número não é primo.")
                c =input("Deseja refazer a operação? Se desejar retornar ao início, digite N  \n s - Sim \n n - Não \n")
                if c == "s":
                    os.system ("cls")
                    a = "1"
                    lógica = "1"
                else:
                    os.system ("cls")
                    z = 2
            elif lógica == "2":
                if b == 1:
                    
                    print("Não é possível refazer")
                
                a = "1"

            elif lógica == "3":

                os.system("cls")

                z = 2

        if a == "2":

            os.system ("cls")

            print("Número decrescente selecionado")
            lógica = input("[1] Prosseguir para a lógica \n[2] Refazer \n[3] Voltar \n[4] Sair \n")
            if lógica == "1":
                d = int(input("insira o valor desejado: \n "))
                while d >= 0:
                    print (d)
                    d -= 1
                if d == 0:
                    print ("Contagem finalizada!")
                c =input("Deseja refazer a operação? Se desejar retornar ao início, digite N \n s - Sim \n n - Não \n")
                if c == "s":

                    os.system ("cls")

                    a = "1"
                    lógica = "1"
                else:

                    os.system ("cls")

                    z = 2
            elif lógica == "2":
                if b == 1:
                    print("Não é possível refazer! ")
                else:
                    a = "2"

            elif lógica == "3":

                os.system("cls")

                z = 2
            elif lógica == "4":
                x = 2

        if a == "3":
            os.system ("cls")

            print("Mediana de três números selecionada")
            lógica = input("[1] Prosseguir para a lógica \n[2] Voltar \n")
            if lógica == "1":
                b = input("Digite o primeiro valor:\n ")
                c = input("Digite o segundo valor:\n ")
                d = input("Digite o terceiro valor:\n ")
                números = [b,c,d]
                números.sort()
                print(números[1])
                c =input("Deseja refazer a operação? Se desejar retornar ao início, digite N \n s - Sim \n n - Não \n")
                if c == "s":

                    os.system ("cls")

                    a = "1"
                    lógica = "1"
                else:

                    os.system ("cls")

                    z = 2
            elif lógica == "2":
                if b == 1:
                    print("Não é possível refazer")
                else:
                    a = "3"

            elif lógica == "3":

                os.system("cls")

                z = 2

        if a == "4":
            print("Finalizando sistema")
            z = 2
            x = 2
            os.system ("pause")

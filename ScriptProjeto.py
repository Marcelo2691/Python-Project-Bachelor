global Agenda,DNA,values
values = []
Agenda = {}
DNA = []

import pickle

def MenuPrincipal(Agenda,values,DNA):

    print("1 - Introduzir novo cliente")
    print("2 - Associar um contacto de um cliente")
    print("3 - Associar um DNA de um cliente")
    print("4 - Testar gene de um DNA")
    print("5 - Excluir um cliente ")
    print("6 - Consultar Agenda")
    print("7 - Gravar dados para um ficheiro")
    print("8 - Ler dados de um ficheiro \n ")
    print("0 - Sair do programa")
    opcao =int(input("Escolha uma opção"))

    if opcao == 1:
        menu1(Agenda, values, DNA)
    elif opcao == 2:
        menu2(Agenda, values, DNA)
    elif opcao == 3:
        menu3(Agenda, values, DNA)
    elif opcao == 4:
        menu4(Agenda, values, DNA)
    elif opcao == 5:
        menu5(Agenda, values, DNA)
    elif opcao == 6:
        menu6(Agenda, values, DNA)
    elif opcao == 7:
        menu7(Agenda, values, DNA)
    elif opcao == 8:
        menu8(Agenda, values, DNA)
    else:
        print("Erro.Introduza um número de menu válido!")
        MenuPrincipal(Agenda, values)

def menu1(Agenda, values, DNA):
    contactos=[]
    NomeCliente = input("Diga o nome do Cliente:")
    Agenda[NomeCliente]= contactos
    contacto = int(input("Diga o contacto do Cliente (0 para terminar registo):"))
    contactos.append(contacto)
    x = True
    while x:
        contacto = int(input("Diga o contacto do Cliente (0 para terminar registo):"))

        if contacto != 0:
            contactos.append(contacto)
            Agenda[NomeCliente] = contactos
        else:
            x = False
    print("Contacto criado com sucesso!")
    values.append(contactos)
    print(Agenda)
    MenuPrincipal(Agenda,values,DNA)

def menu2(Agenda,values,DNA):
    contactos=[]
    if Agenda == {}:
        print("Erro. Cliente não encontrado!")
        menu1(Agenda,contactos,DNA)
        print("Contacto criado com sucesso!")
    else:
        NomeCliente = input("Diga o nome do cliente para adicionar:")
        if Agenda[NomeCliente]:
            contacto = int(input("Diga o contacto do Cliente (0 para terminar):"))
            contactos.append(contacto)
            x = True
            while x:
                contacto = int(input("Diga o contacto do Cliente (0 para terminar):"))

                if contacto != 0:
                    contactos.append(contacto)
                    Agenda[NomeCliente] = contactos
                else:
                    x = False
            print("Contacto/s adicionado/s com sucesso!")
            values.append(contactos)
            Agenda[NomeCliente] = values
    print(Agenda)
    MenuPrincipal(Agenda, values, DNA)


def menu3(Agenda,values,DNA):
    values=[]
    DNA=[]
    aminoacidos=['A','T','G','C']
    if Agenda == {}:
        menu1(Agenda, values,DNA)
    else:
        NomeCliente = input("Diga o nome do cliente para adicionar")
        if NomeCliente in Agenda.keys():
            values=Agenda.get(NomeCliente)
            DNA = input("Insira a sequência de DNA: ").upper()
            DNA=[i for i in DNA]
            for i in range(len(DNA)):
                if DNA[i] in aminoacidos:
                    pass
                else:
                    print("ERRO: A sequência de DNA não é valida", "\n")
                    menu3(Agenda,values,DNA)
            print("Sequência DNA adicionada ao contacto!")
            DNA = "".join(DNA)
            values=values.append(DNA)
        else:
            print("Contacto não encontrado. Crie um contacto válido!")
            MenuPrincipal(Agenda, values, DNA)

    print(Agenda)
    MenuPrincipal(Agenda,values,DNA)


def menu4(Agenda,values,DNA):
    if Agenda == {}:
        menu1(Agenda,values,DNA)
    else:
        NomeCliente = input("Diga o nome do cliente para teste do seu DNA")
        if NomeCliente in Agenda.keys():
            DNA= Agenda.get(NomeCliente)
            if DNA[0:3] == "ATG" and len(DNA) % 3 == 0:
                if DNA[-3:] == "TAG" or "TAA" or "TGA":
                    print("O gene é XPT")

            else:
                print("O gene nao é XPT")
    MenuPrincipal(Agenda,values,DNA)




def menu5(Agenda,values,DNA):
    NomeCliente = input("Diga o nome do cliente")
    if NomeCliente in Agenda.keys():
        Agenda.pop(NomeCliente)
    print(Agenda)
    MenuPrincipal(Agenda,values,DNA)




def menu6 (Agenda,values,DNA):
        print(Agenda)
        MenuPrincipal(Agenda,values,DNA)



def menu7 (Agenda,values,DNA):
    Agenda = Agenda
    f = open("Agenda.txt","w")
    f.write(str(Agenda))
    f.close()
    MenuPrincipal(Agenda,values,DNA)



def menu8(Agenda,values,DNA):
    f = open("Agenda.txt", "r")
    str = f.readline()
    f.close()
    MenuPrincipal(Agenda,values,DNA)



if __name__ == '__main__':
    MenuPrincipal(Agenda, values, DNA)


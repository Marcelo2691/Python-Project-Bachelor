global Agenda,DNA,values
values = []
Agenda = {}
DNA = []

def MenuPrincipal(Agenda,values):

    print("1 - Introduzir novo cliente")
    print("2 - Associar um contacto de um cliente")
    print("3 - Associar um DNA de um cliente")
    print("4 - Testar gene de um DNA")
    print("5 - Excluir um contacto de um cliente ")
    print("6 - Consultar Agenda")
    print("7 - Gravar dados para um ficheiro")
    print("8 - Ler dados de um ficheiro \n ")
    print("0 - Sair do programa")
    opcao =int(input("Escolha uma opção"))

    if opcao == 1:
        menu1(Agenda,values)
    elif opcao ==2:
        menu2(Agenda,values)
    elif opcao ==3:
        menu3(Agenda, values)
    elif opcao ==4:
        menu4(Agenda,values)
    elif opcao ==5:
        menu5(Agenda,values)
    elif opcao ==6:
        menu6(Agenda,values)
    elif opcao ==7:
        menu7()
    elif opcao ==8:
        menu8()
    else:
        print("Thank your come again!")

def menu1(Agenda,values):
    contactos=[]
    NomeCliente = input("Diga o nome do Cliente")
    Agenda[NomeCliente]= contactos
    contacto = int(input("Diga o contacto do Cliente"))
    contactos.append(contacto)
    x = True
    while x:
        contacto = int(input("Diga o contacto do Cliente"))

        if contacto != 0:
            contactos.append(contacto)
            Agenda[NomeCliente] = contactos
        else:
            x = False
    values.append(contactos)
    print(Agenda)
    MenuPrincipal(Agenda,values)

def menu2(Agenda,values):
    contactos=[]
    if Agenda == {}:
        menu1(Agenda, contactos, values)
    else:
        NomeCliente = input("Diga o nome do cliente para adicionar--")
        if Agenda[NomeCliente]:
            contacto = int(input("Diga o contacto do Cliente"))
            contactos.append(contacto)
            x = True
            while x:
                contacto = int(input("Diga o contacto do Cliente"))

                if contacto != 0:
                    contactos.append(contacto)
                    Agenda[NomeCliente] = contactos
                else:
                    x = False
            values.append(contactos)
            Agenda[NomeCliente]=values
    print(Agenda)
    MenuPrincipal(Agenda, values)


def menu3(Agenda,values,):
    values=[]
    DNA=[]
    aminoacidos=['A','T','G','C']
    if Agenda == {}:
        menu1(Agenda, values)
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
                    menu3(Agenda,values)

            DNA = "".join(DNA)
            values=values.append(DNA)
            Agenda[NomeCliente]=DNA
        else:
            print("Contacto nao encontrado")
            MenuPrincipal(Agenda, values)

    print(Agenda)
    MenuPrincipal(Agenda,values)


def menu4(Agenda,values,):
    if Agenda == {}:
        menu1(Agenda,values)
    else:
        NomeCliente = input("Diga o nome do cliente para teste do seu DNA")
        if NomeCliente in Agenda.keys():
            DNA= Agenda.get(NomeCliente)
            if DNA[0:3] == "ATG" and len(DNA) % 3 == 0:
                if DNA[-3:] == "TAG" or "TAA" or "TGA":
                    print("O gene é XPT")

            else:
                print("O gene nao é XPT")

def menu6 (Agenda,values):
    NomeCliente = input("Diga o nome do cliente")
    if NomeCliente in Agenda.keys():
        print("Contacto", values(NomeCliente))
def menu5(Agenda,values):
    NomeCliente = input("Diga o nome do cliente")
    if NomeCliente in Agenda.keys():
        Agenda.pop(NomeCliente)
    MenuPrincipal(Agenda,values)

if __name__ == '__main__':
    MenuPrincipal(Agenda,values)


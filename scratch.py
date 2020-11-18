global Agenda,contactos,DNA,values
values = []
Agenda = {}
contactos = []
DNA = []

def MenuPrincipal():
    global agenda1
    print("1 - Introduzir novo cliente")
    print("2 - Associar um contacto de um cliente")
    print("3 - Associar um DNA de um cliente")
    print("4 - Testar gene de um DNA")
    print("5 - Excluir um contacto de um cliente ")
    print("6 - Consultar Agenda")
    print("7 - Gravar dados para um ficheiro")
    print("8 - Ler dados de um ficheiro \n ")
    print("0 - Sair do programa")
    opcao =(input("Escolha uma opção"))
    if opcao.isdigit():
        menu(opcao,Agenda,contactos,values)
    else:
        print("Erro.Introduzir opção válida")
        MenuPrincipal()
def menu(opcao,Agenda,contactos,values):

    def menu1(Agenda,contactos,values):
        NomeCliente = input("Diga o nome do Cliente")
        Agenda[NomeCliente]= contactos
        contacto = int(input("Diga o contacto do Cliente"))
        contactos.append(contacto)
        x = True
        while x:
            contacto = int(input("Diga o contacto do Cliente"))
            contactos.append(contacto)
            if contacto != 0:
                Agenda[NomeCliente] = contactos

            else:
                x = False
        values.append(contactos)
        a = Agenda[NomeCliente]
        a.remove(0)
        print(Agenda)
        return Agenda,contactos,values


    def menu2(Agenda,contactos,lista):
        if Agenda == {}:
            menu1(Agenda, contactos, values)
        else:
            NomeCliente = input("Diga o nome do cliente para adicionar--")
            if Agenda[NomeCliente]:
                Agenda.values()
                #contactos.append(Agenda[NomeCliente].values())
                values.append(contactos)
                Agenda[NomeCliente]=lista
        print(Agenda)
        return Agenda,contactos,lista


    def menu3(Agenda,DNA,values,contactos):
        if Agenda == {}:
            NomeCliente = input("Diga o nome do Cliente:")
            sequencia =str(input("Diga a sequencia DNA do Cliente:"))
            DNA.append(sequencia)
            values.append(DNA)
            values.append(contactos)
            Agenda[NomeCliente] = values
            print(Agenda)
        else:
            NomeCliente = input("Diga o nome do cliente para adicionar")
            if Agenda[NomeCliente]:
                values.append(zip(Agenda[NomeCliente].values(),DNA))
                values.append(DNA)
                values.append(contactos)
                Agenda[NomeCliente]=values

        return Agenda,DNA,values


    if opcao == "1":
        Agenda,contactos,values=menu1(Agenda,contactos,values)
        MenuPrincipal()
    elif opcao == "2":
        Agenda,contactos,values=menu2(Agenda,contactos,values)
        MenuPrincipal()
    elif opcao == "3":
        Agenda,DNA,values=menu3(Agenda,DNA,values,contactos)
        MenuPrincipal()
MenuPrincipal()










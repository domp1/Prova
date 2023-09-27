#PABLO HENRIQUE VIEIRA DA SILVA
import os
from time import sleep
inventario=[]
u=False
while(u==False):
    def add():
        dicionario={}
        n=int(len(inventario)+1) 
        name=input("Insira o nome do produto: ")
        p=int(input("Insira o preço do produto: "))
        q=int(input("Insira a quantidade em estoque: "))
        qm=int(input("Insira a quantidade mínima: "))
        dicionario.update({'id':n,'nome':name,'preço':p,'quantidade':q,'quantidade_minima':qm})
        inventario.append(dicionario)
        print("Item adicionado com sucesso!")
        sleep(3)

    def remove():
        os.system("cls")
        print("------ Produtos ------")
        for i in inventario:
            print("Nome:",i['nome'],"    ID:",i['id'])
        s=int(input("Insira o ID do produto que deseja remover: "))
        for j in inventario:
            if s == j['id']:
                inventario.remove(j)
                print("Item removido com sucesso! ")    
        x=1
        for n in inventario:
            n['id']=x
            x+=1
        sleep(4)
    
    def calcy():
        v=0
        for i in inventario:
            v=v+i['quantidade']*i['preço']
        print("Valor encontrado: R$",float(v))
        sleep(4)

    def listar():
        os.system("cls")
        print("----- Produtos abaixo da quantidade mínima ------")
        for i in inventario:
            if i['quantidade']<i['quantidade_minima']:
                print("ID:",i['id'],"  Nome:",i['nome'],"   Quantidade:",i['quantidade'],"    Q mínima:",i['quantidade_minima'])
        sleep(5)
    
    def busca():
        n=input("Insira o nome do produto que deseja achar: ")
        for i in inventario:
            if i['nome']==n:
                print("Produto encontrado!")
                sleep(1)
                os.system("cls")
                print("ID:",i['id'],"  Nome:",i['nome'],"    Preço:",i['preço'],"   Quantidade:",i['quantidade'],"    Q mínima:",i['quantidade_minima'])
                sleep(4)
            else: 
                print("Produto não encontrado! ")
                sleep(4)

    os.system("cls")
    print("------- Gerenciador de Inventário de Produtos ---------\n1 - Adicionar um novo produto ao estoque\n2 - Remover um produto do estoque usando o ID")
    print("3 - Calcular o valor total em estoque \n4 - Listar todos os produtos com quantidade em estoque menor que o mínimo \n5 - Busca de produtos por nome \n6 - Sair")
    op=int(input("Escolha uma opção: "))

    match op:
        case 1: add()
        case 2: remove()
        case 3: calcy()
        case 4: listar()
        case 5: busca()
        case 6: break
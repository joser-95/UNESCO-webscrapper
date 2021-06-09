#importação de pacotes

#importação de ficheiros
import procura_termo

def main():

    termo = termo_de_pesquisa()
    lista_termos = procura_termo.get_page(termo)
    for el in range(len(lista_termos)):
        print(lista_termos[el])
    print("This dataset contains information from The UNESCO Thesaurus which is made available by UNESCO under the CC-BY-SA 3.0 IGO license.")
    #eventualmente pode se melhorar a atribuição



def termo_de_pesquisa():
    """
    recebe uma string como input, esta vai ser usada como termo de pesquisa para criar o URL para o tésauro da UNESCO
    :return: string
    """
    termo = input("escolha um termo que define a sua empresa")
    return termo


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()



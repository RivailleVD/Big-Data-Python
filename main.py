from funcoes  import *

def main():
    while True:
        exibir_menu()
        opcao = obter_opcao()
        
        if opcao == 1:
            print(mostrar_colunas())
        
        elif opcao == 2:
            print(mostrar_municipios())
            
        elif opcao == 3:
            print(graficos_genero())
        
        elif opcao == 4:
            consulta = str(input("Pesquise O Municipio Cearence Desejado: "))
            print(pesquisar_cidade(consulta))
        
        else:
            print("\n\n\33[41;1mOpção inválida!, tente novamente!\33[m\n\n")

if __name__ == "__main__":
    main()
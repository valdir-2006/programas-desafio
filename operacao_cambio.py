'''
    Um programa criado para atender ao desafio Havan.
    Trata-se de uma gerenciador de operações de uma casa de cambio.
    Ctba, 22/05/21.  -  Versão 1.0
    Autor: Valdir B. de Souza
'''
# -----------------------------------------------------------------------------
''' importação das bibliotecas.'''
# -----------------------------------------------------------------------------
from datetime import date
from lib_cal import moedas, atualiza, cadastrar, relatorioClientes
from lib_cal import relatorioGeral, relatorioOperacaoes, relatorioTaxas

# -----------------------------------------------------------------------------
''' função main - função principal, ponto inicial do sistema.'''
# -----------------------------------------------------------------------------
def main():
    cadastro = []
    tx_total = 0
    op_total = 0

    # -------------------------------------------------------------------------
    ''' inicio da laço principal '''
    # -------------------------------------------------------------------------
    while True:
        print('===============================================================')
        print('           GERENCIAMENTO DE OPERAÇÕES DE CÂMBIO                ')
        print('===============================================================')

        print('===============================================================')
        print('=====================  MENU PRINCIPAL  ========================')
        print('     [1] - Cadastrar nova operação')
        print('     [2] - Gerar relatórios')
        print('     [3] - Sair')
        print('===============================================================')
        # ----------------------------------------------------------------------
        ''' tratamento de erros e exceções, para não travar caso não seja 
        digitado um nº inteiro. '''
        # ----------------------------------------------------------------------
        try:
            opcao = int((input('     Selecione uma opção: ')))
        except:
            print('\n >> ATENÇÃO: só aceita número inteiro. <<')
            continue

        # -----------------------------------------------------------------------
        ''' condições que direcionam para as opções do menu principal.'''
        # -----------------------------------------------------------------------
        if opcao == 1:
            print('')
            moedas()
            atualiza()
            cad_tx_op = cadastrar(cadastro, tx_total, op_total)
            cadastro = cad_tx_op[0]
            tx_total = cad_tx_op[1]
            op_total = cad_tx_op[2]

        elif opcao == 2:
            # -----------------------------------------------------------------------
            ''' inicio do laço dos relatórios.'''
            # -----------------------------------------------------------------------
            while True:
                print('')
                print('===============================================================')
                print('=====================  MENU RELATÓRIOS  =======================')
                print('     [1] - Relatório geral')
                print('     [2] - Relatório por clientes')
                print('     [3] - Total de taxa cobrada')
                print('     [4] - Quantidade de operações')
                print('     [5] - Retornar ao menu principal')
                print('===============================================================')
                # ----------------------------------------------------------------------
                ''' tratamento de erros e exceções, para não travar caso não seja 
                digitado um nº inteiro.'''
                # ----------------------------------------------------------------------
                try:
                    opcao = int((input('     Selecione uma opção: ')))
                except:
                    print('\n >> ATENÇÃO: só aceita número inteiro. <<')
                    continue
                
                # ----------------------------------------------------------------------
                ''' condições que direcionam para as opções do menu relatórios.'''
                # ----------------------------------------------------------------------
                if opcao == 1:
                    relatorioGeral(cadastro)

                elif opcao == 2:
                    nome = input('\nInforme o nome do cliente: ').title()
                    relatorioClientes(cadastro, nome)

                elif opcao == 3:
                    relatorioTaxas(tx_total)

                elif opcao == 4:
                    relatorioOperacaoes(op_total)
                
                elif opcao == 5:
                    print('')
                    break

                else:
                    print('\n Opção inválida, selecione novamente.\n')

        elif opcao == 3:
            print('')
            break

        else:
            print('\n Opção inválida, selecione novamente.')
           
        print('')
                
# --------------------------------------------------------------------------------------
''' condição que define a função principal e o ponto de inicialização do programa. '''
# --------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
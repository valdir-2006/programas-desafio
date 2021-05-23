'''
    Biblioteca com as funções do gerenciador de operações de cambio.
''' 
# -----------------------------------------------------------------------------
''' importação das bibliotecas.'''
# -----------------------------------------------------------------------------   
from datetime import date

# -----------------------------------------------------------------------------
''' variáveis com informações estruturais do programa. 
    caso queira alterar os valores da cotação fixa do real, pode ser feito 
diretamente substituído os valores do dicionário m_val.'''
# -----------------------------------------------------------------------------
data_atual = date.today()
m_cod = ['BRL','USD','EUR','JPY','GBP','CAD']
m_val = {'USD':5.3027,'EUR':6.4558,'JPY':0.04867,'GBP':7.5057,'CAD':4.3913}
m_simbolos = {'BRL': 'R$','USD':'$','EUR':'€','JPY':'¥','GBP':'£','CAD':'$C'}
data_cotacao = '2021-05-21'
#print(data_cotacao)

# -----------------------------------------------------------------------------
''' função que dá a informativa com o código das moedas cadastradas.'''
# -----------------------------------------------------------------------------
def moedas():
    print('\n--------------------------------------------------------------')
    print('########### ATENÇÃO LEIA - INFORMAÇÕES IMPORTANTES ###########')
    print('\nCódigo das moedas internacionais que podem ter convertidas:\n')
    print ('( Real /',m_cod[0],')','- ' '( Dolar /',m_cod[1],')','- '
            '( Euro /',m_cod[2],')','- ' '( IENE /',m_cod[3],')','- ') 
    print('(Libra Esterlina /',m_cod[4],')','- ' '( Dolar Canadense /',m_cod[5],')''\n')

# -----------------------------------------------------------------------------
''' função que solicita se quer que os valores das moedas sejam atualizados 
para a data de execução do programa.'''
# -----------------------------------------------------------------------------
def atualiza():
    print('--------------------------------------------------------------')
    print('Como referência, os valores das moedas são em relaçao ao Real.\n')
    print('Os valores das moedas foram atualizados em: {}\n'.format(data_cotacao))
    print('Deseja fazer a atualização dos valores para a data de [ {} ]'.format(data_atual))
    x = input('S/N? ')
    x = x.upper()

    # -------------------------------------------------------------------------
    ''' condição que será executada caso a resposta anterior seja "s", em seguida,
    é feito tratamento de erro e exceções para entrada correta dos valores.'''
    # -------------------------------------------------------------------------
    if x == 'S':
        for i in m_val:
            while True:
                try:
                    m_val[i] = float(input('Digite o valor do Real em {} '.format(i)))
                    break
                except:
                    print('>> Erro na digitação, só aceita números e ponto no lugar da virgula. <<')

        print('\nValor do Real em relação as moedas estranjeiras atualizado.\nn')
        print(m_val,'\n')  
    else:
        print('\nValor do Real em relação as moedas estranjeiras não atualizado.\n')
        print(m_val,'\n')

# -----------------------------------------------------------------------------
''' função que recebe a entrada das informações que serão processadas pelo
programa.'''
# -----------------------------------------------------------------------------
def cadastrar(cadastro, tx_total, op_total):
    cadastro = cadastro
    tx_total = tx_total
    op_total = op_total
    
    # -----------------------------------------------------------------------------
    ''' rotina que é executada até a finalização do programa pelo usuário.'''
    # -----------------------------------------------------------------------------
    while True:
        
        # -------------------------------------------------------------------------
        ''' aqui são coletadas as informações que serão processadas pelas funções 
        das bibliotecas.'''
        # --------------------------------------------------------------------------
        nome = (input('Nome do Cliente: \n')).title()
        m_origem = origem()
        m_destino = destino(m_origem)
        data_operacao = date.today()

        # --------------------------------------------------------------------------
        ''' envia os dados coletas para função operacao e recebe os resultados.'''
        # --------------------------------------------------------------------------        
        resultado = operacao(m_origem,m_destino)
        vl_original = resultado[0]
        vl_convertido = resultado[1]
        tx_cobrada = resultado[2]

        # --------------------------------------------------------------------------
        ''' soma as taxas cobradas e armazena na variável.'''
        # --------------------------------------------------------------------------        
        tx_total = tx_total + tx_cobrada

        # --------------------------------------------------------------------------
        ''' recebe da função relatorio os dados concatenados e amazena em um 
        dicionário.'''        
        # --------------------------------------------------------------------------
        cliente = relatorio(vl_original, vl_convertido, tx_cobrada, nome, 
                                    m_origem, m_destino, data_operacao)

        # --------------------------------------------------------------------------
        ''' cria um dicionário vazio a cada execução.
            insere no dicionário o dicionário cliente como valor e o nome como chave.
            transfere os dados criados a cada execução para uma lista.'''
        # --------------------------------------------------------------------------
        cliente2 = {}
        cliente2[nome] = cliente
        cadastro.append(cliente2)

        # --------------------------------------------------------------------------
        ''' verifica se haverá novas inclusões.'''
        # -------------------------------------------------------------------------- 
        x = input('\nDeseja incluir nova operação. S/N?\n').upper()

        # --------------------------------------------------------------------------
        ''' registra a quandidade de operações executadas.'''
        # --------------------------------------------------------------------------
        op_total = op_total + 1

        # --------------------------------------------------------------------------
        '''finaliza a rotina de inclusões do programa.'''
        # --------------------------------------------------------------------------
        if x == 'N':
            break

    # ------------------------------------------------------------------------------
    ''' retorno dos dados que serão enviados aos relatórios.'''
    # ------------------------------------------------------------------------------
    return (cadastro, tx_total, op_total)

    print('')

# ----------------------------------------------------------------------------------
''' função que recebe e valida a moeda de entrada.'''
# ----------------------------------------------------------------------------------
def origem():
    while True:
        entrada = input('\nDigite a moeda de origem: ')
        entrada = entrada.upper()
        a = entrada in m_cod
        if a == True:
            break
        else:
            print('Código inválido, moeda não cadastrada, digite novamente.')
    return entrada    

# ----------------------------------------------------------------------------------
''' função que recebe e valida a moeda de saída.'''
# ---------------------------------------------------------------------------------- 
def destino(entrada):
    entrada = entrada
    while True:
        saida = input('\nDigite a moeda de destino: ')
        saida = saida.upper()
        b = saida in m_cod
        if b == True and saida != entrada:
            break
        else:
            print('\nCódigo inválido, moeda não cadastrada ou repetida, digite novamente.')
    return saida

# ----------------------------------------------------------------------------------
''' função executada através da função cadastrar, recebe os tipos de moedas, solicita
a quantidade a ser convertida, faz a validação desse dado, faz a conversão e retorna 
os resultados para a função que a chamou.'''
# ----------------------------------------------------------------------------------
def operacao(entrada, saida):
    while True:
        try:
            m_quant = float(input('\nQual o valor a ser convertido?\n'))
            break
        except:
            print('>> Erro na digitação, só aceita números e ponto no lugar da virgula. <<')
    tx_cobrada =  m_quant * 0.1

    if entrada == 'BRL':
        vl_convertido = m_val[saida]
        vl_convertido = 1 / vl_convertido * (m_quant - tx_cobrada)
        vl_taxa = tx_cobrada

    elif saida == 'BRL':
        vl_convertido = m_val[entrada]
        vl_convertido = vl_convertido * m_quant
        vl_taxa = vl_convertido * 0.1
        vl_convertido = vl_convertido - vl_taxa

    else:
        vl_entrada = m_val[entrada]
        vl_entrada = 1 / vl_entrada
        vl_convertido = m_val[saida]
        vl_convertido = 1 / vl_convertido
        vl_convertido = vl_convertido / vl_entrada * (m_quant - tx_cobrada)
        vl_taxa = tx_cobrada * m_val[entrada]
    return (m_quant, vl_convertido, vl_taxa)

# ----------------------------------------------------------------------------------
''' função que é chamada e recebe os dados da função cadastrar, formata os valores 
de moedas para o padrão brasileiro, concatena os dados com as chaves, gera um 
dicionário e retorna-o a função que a chamou. Esse relatório é o que é apresentado
assim que é feito uma nova solicitação de conversão. '''
# ----------------------------------------------------------------------------------
def relatorio(vl_original, vl_convertido, tx_cobrada, nome, m_origem, m_destino, data_operacao):
    vl_original = f'{vl_original:_.2f}'
    vl_original = vl_original.replace('.',',').replace('_','.')
    vl_convertido = f'{vl_convertido:_.2f}'
    vl_convertido = vl_convertido.replace('.',',').replace('_','.')
    tx_cobrada = f'{tx_cobrada:_.2f}'
    tx_cobrada = tx_cobrada.replace('.',',').replace('_','.')

    cliente = {'Nome':nome,'Moeda_Origem':m_origem,
                'Moeda_Destino':m_destino,'Data_Operação':data_operacao,
                'Valor_Original':(m_simbolos[m_origem] + ' ' + vl_original),
                'Valor_Convertido':(m_simbolos[m_destino] + ' ' + vl_convertido),
                'Taxa_Cobrada':(m_simbolos['BRL'] + ' ' + tx_cobrada)}
    
    print('')
    print(cliente)
    return cliente

# ----------------------------------------------------------------------------------
''' função que é chamada através do menu relatórios, recebe os dados da lista 
cadastro com todas as operações aglutinadas, e exibe as operações separadas por
clientes.'''
# ----------------------------------------------------------------------------------
def relatorioGeral (cadastro):
    for i in cadastro:
        for tipo, tipo2 in i.items():
            print('\nCliente: '+ tipo)
            tudo_qtd = 'Nome: '+str(tipo2['Nome']) + " - "
            tudo_qtd += 'Moeda_Origem: '+str(tipo2['Moeda_Origem']) + " - "
            tudo_qtd += 'Moeda_Destino: '+str(tipo2['Moeda_Destino']) + " - "
            tudo_qtd += 'Data_Operação: '+str(tipo2['Data_Operação']) + " - "
            tudo_qtd += 'Valor_Original: '+str(tipo2['Valor_Original']) + " - "
            tudo_qtd += 'Valor_Convertido: '+str(tipo2['Valor_Convertido']) + " - "
            tudo_qtd += 'Taxa_Cobrada: '+str(tipo2['Taxa_Cobrada'])
            print('Dados da operação: '+tudo_qtd)

# ----------------------------------------------------------------------------------
''' função que é chamada através do menu relatórios, recebe os dados da lista 
cadastro com todas as operações aglutinadas, e exibe as operações conforme o nome do
clientes indicado caso o mesmo exista.'''
# ----------------------------------------------------------------------------------
def relatorioClientes (cadastro, nome):
    x = False
    for i in cadastro:
        for tipo, tipo2 in i.items():
            if tipo == nome:
                print('\nCliente: '+ tipo)
                tudo_qtd = 'Nome: '+str(tipo2['Nome']) + " - "
                tudo_qtd += 'Moeda_Origem: '+str(tipo2['Moeda_Origem']) + " - "
                tudo_qtd += 'Moeda_Destino: '+str(tipo2['Moeda_Destino']) + " - "
                tudo_qtd += 'Data_Operação: '+str(tipo2['Data_Operação']) + " - "
                tudo_qtd += 'Valor_Original: '+str(tipo2['Valor_Original']) + " - "
                tudo_qtd += 'Valor_Convertido: '+str(tipo2['Valor_Convertido']) + " - "
                tudo_qtd += 'Taxa_Cobrada: '+str(tipo2['Taxa_Cobrada'])
                print('Dados da operação: '+tudo_qtd)
                x = True
    if x == False:
        print('\nNome não encontrado, verfique a grafia correta pelo relatório geral.')

# ----------------------------------------------------------------------------------
''' função que é chamada através do menu relatórios, recebe os dados do valor total 
de taxas cobradas formata para o padrão de acentuação brasileiro e exibe o valor.
OBS.: os valores já estão em real.'''
# ----------------------------------------------------------------------------------
def relatorioTaxas(tx_total):
    tx_total = f'{tx_total:_.2f}'
    tx_total = tx_total.replace('.',',').replace('_','.')
    print('\nO valor total de taxas cobrado foi de: R$ {}'.format(tx_total))
    print('\nA taxa especificada é de 10%, esse valor inside sobre a moeda de')
    print('origem, então é convertido para real em cada operação.')

# ----------------------------------------------------------------------------------
''' função que é chamada através do menu relatórios, recebe os dados do total 
de operações realizadas e exibe esse valor.'''
# ----------------------------------------------------------------------------------
def relatorioOperacaoes(op_total):
    print('\nO número de operações realizadas foi de: {}'.format(op_total))   
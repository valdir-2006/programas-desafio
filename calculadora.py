'''
    Um programa criado para atender ao desafio Havan.
    Trata-se de uma calculadora que converte moedas.
    Ctba, 14/05/21. - Versão 1.0
    Autor: Valdir Botan de Souza
'''
# -----------------------------------------------------------------------------
''' importa a biblioteca date.'''
# -----------------------------------------------------------------------------
from datetime import date

# -----------------------------------------------------------------------------
''' inicializa variáves, tupla e dicionários com valores.'''
# -----------------------------------------------------------------------------
class Conversor:
    data_atual = date.today()
    m_cod = ['BRL','USD','EUR','JPY','GBP','CAD']
    m_val = {'USD':5.2695,'EUR':6.3961,'JPY':0.04819,'GBP':7.4268,'CAD':4.3496}
    m_simbolos = {'BRL': 'R$','USD':'$','EUR':'€','JPY':'¥','GBP':'£','CAD':'$C'}
    data_cotacao = '2021-05-14'
    print(data_cotacao)
    
    # --------------------------------------------------------------------------    
    ''' construtor que chama as funções.'''
    # --------------------------------------------------------------------------
    def __init__(self):
        self.moedas()
        self.atualiza()
        self.origem()
        self.destino()
        self.operacao()

    # --------------------------------------------------------------------------
    ''' função moedas - indica o código das moedas cadastradas no sistema.'''
    # --------------------------------------------------------------------------    
    def moedas(self):
        print('\n\n==========================================================')
        print('Código das moedas internacionais que podem ter convertidas.\n')
        print('( Real /',self.m_cod[0],')','- ' '( Dolar /',self.m_cod[1],')','- '
                '( Euro /',self.m_cod[2],')','- ' '( IENE /',self.m_cod[3],')','- ') 
        print('(Libra Esterlina /',self.m_cod[4],')''- ' '( Dolar Canadense /',self.m_cod[5],')''\n')
 
    # --------------------------------------------------------------------------
    ''' função atualiza - informa a data da cotação das moedas que será a base 
                        da conversão.
                        - solicita a atualização para a data atual do sistema.
                        - caso positivo, será solicitado informar o valor em 
                        real das moedas cadastradas.'''
    # --------------------------------------------------------------------------
    def atualiza(self):
        print('Como referência, os valores das moedas são em relaçao ao Real.\n')
        print('Os valores das moedas foram atualizados em: {}\n'.format(self.data_cotacao))
        print('Deseja fazer a atualização dos valores para a data de [ {} ]'.format(self.data_atual))
        x = input('S/N? ')
        x = x.upper()

        if x == 'S':
            for i in self.m_val:
                self.m_val[i] = float(input('\nDigite o valor do Real em {} '.format(i)))
            print('\nValor do Real em relação as moedas estranjeiras atualizado.\nn')
            print(self.m_val,'\n')  
        else:
            print('\nValor do Real em relação as moedas estranjeiras não atualizado.\n')
            print(self.m_val,'\n')

    # --------------------------------------------------------------------------
    ''' função origem - solicita e valida o código da moeda de origem.'''
    # --------------------------------------------------------------------------
    def origem(self):
        while True:
            self.entrada = input('Digite a moeda de origem: ')
            self.entrada = self.entrada.upper()
            a = self.entrada in self.m_cod
            if a == True:
                break
            else:
                print('Código inválido, moeda não cadastrada, digite novamente.')

    # --------------------------------------------------------------------------
    ''' função destino - solicita e valida o código da moeda de destino.'''
    # --------------------------------------------------------------------------
    def destino(self):
        while True:
            self.saida = input('\nDigite a moeda de destino: ')
            self.saida = self.saida.upper()
            b = self.saida in self.m_cod
            if b == True:
                break
            else:
                print('\nCódigo inválido, moeda não cadastrada, digite novamente.')

    # --------------------------------------------------------------------------
    ''' função operacao - responsável por realizar a conversão das moedas.
                        - a conversão é baseado no valor em real das demais moedas.
                        - a primeira condição é quando a conversão é do real para 
                        outra moeda.
                        - a segunda condição é quando a conversão é de outra moeda 
                        para o real.
                        - a terceira condição é quando a conversão é entre moedas 
                        estrangeiras.'''
    # --------------------------------------------------------------------------
    def operacao(self):
        m_quant = float(input('\nQual o valor a ser convertido?\n'))

        if self.entrada == 'BRL':
            vl_saida = self.m_val[self.saida]
            vl_saida = 1 / vl_saida * m_quant

        elif self.saida == 'BRL':
            vl_saida = self.m_val[self.entrada]
            vl_saida = vl_saida * m_quant

        else:
            vl_entrada = self.m_val[self.entrada]
            vl_entrada = 1 / vl_entrada
            vl_saida = self.m_val[self.saida]
            vl_saida = 1 / vl_saida
            vl_saida = vl_saida / vl_entrada * m_quant

        # -----------------------------------------------------------------------
        ''' comandos para fazer a formatação das casas decimais e a pontuação no 
        padrão brasileiro.'''
        # -----------------------------------------------------------------------
        m_quant = f'{m_quant:_.2f}'
        m_quant = m_quant.replace('.',',').replace('_','.')
        vl_saida = f'{vl_saida:_.3f}'
        vl_saida = vl_saida.replace('.',',').replace('_','.')

        print('\n{} {} equivale a {} {}\n'.format(self.m_simbolos[self.entrada],
                                                m_quant,self.m_simbolos[self.saida],vl_saida))

# -------------------------------------------------------------------------------
''' função main - função que executa o programa principal.'''
# -------------------------------------------------------------------------------
def main():
    a = Conversor()

# -------------------------------------------------------------------------------
''' condição que define a função principal e o ponto de inicialização do programa.'''
# -------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
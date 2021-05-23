# programas-desafio
Um programa criado para atender ao desafio Havan.
Trata-se de uma gerenciador de operações de uma casa de cambio.
Ctba, 22/05/21.  -  Versão 1.0
Autor: Valdir B. de Souza

O programa é bem simples e de fácil entendimento e execução.
Possui cadastradas 5 códigos de moedas internacionais que permite a conversão para o real e entre ela, os valores são referenciado no real, ou seja o valor em real de cada uma das moedas.
No início do programa é solicitado se deseja fazer a atualização para a data atual.
Em seguida é só informar  o nome, moeda de origem, moeda de destino e a quantidade, a conversão é feita e é apresentado o relatório preliminar da operação, caso não acha interesse em nova conversão é retornado ao menu principal e deste pode-se ir ao menu relatórios que dá acesso as opções de relatórios.

-------------------------------------------------------------------------------------------------------
O programa foi desenvolvido em python e é composto por 02 arquivos, um com os menus e a função main e o outro com a biblioteca de funções.

---------------------------------------------------------------------------------------------------------
Para gerar o executável pode ser através do pyinstaller.

Para instalar é só digitar na linha de comando do windows:
pip install pyinstaller
Para gerar o executável, é só estando no diretório para onde foram baixados os arquivos e digitar na linha de comando do windows:
pyinstaller operacao_cambio.py
o arquivo executável vai estar na pasta que será criada: 
 \dist\operacao_cambio\operacao_cambio.exe


#Aqui serão calculados os diodos
def processarDiodo(diodotype):
    if diodotype == 'silicio':
        slc = 0.7
        tt = int(input('qual a tensão de entrada do circuito?: '))
        vo = tt - slc
        print(f'A saída do diodo de Silício é: {vo}')
    elif diodotype == 'germanio':
        gmn = 0.3
        it = float(input(f'Qual a tensão de entrada do circuito?: '))
        vi = it - gmn
        print(f'A tensão no final do circuito será: {vi}')

#A partir daqui é a parte dos op-amp ou amplificadores operacionais

    elif diodotype == 'inversor':
        errium = float(input('Quantidade de resistencia do resistor 1: '))
        erridois = float(input('Quantidade de resistencia do resistor 2: '))
        tens = float(input('Tensão na entrada do circuito: '))
        av = - erridois/errium
        vu = av * tens
        print(f'A tensão de saída é: {vu}V')
    elif diodotype == 'não-inversor':
        resistorum = float(input('Quantidade resistiva do resistor 1: '))
        resistordois = float(input('Quantidade resistiva do capacitor 2: '))
        entradasinal = float(input('Tensão na entrada de sinal: ')) 
        Av = 1 + (resistordois/resistorum)
        tensãoex = Av * entradasinal
        print(f'A tensão na saída do amplificador não-inversor será: {tensãoex}v')
def start():
    print('Calculadora de Diodos e Amplificadores operacionais')
    while True:
        diodotype = input('Qual Diodo você deseja calcular? [Germânio] ou [Silício] ou gostaria de calcular op-amps: [Inversor] ou [Não-inversor]? ')
        processarDiodo(diodotype) 
        if diodotype == ' ':
            break
if __name__ == '__main__':





    start()

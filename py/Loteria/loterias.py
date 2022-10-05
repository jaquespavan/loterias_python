import random
import os

while True:

    os.system('cls')

    print('------------------------')
    print('### LOTERIAS ###')
    print('1: MEGASENA')
    print('2: LOTOFÁCIL')
    print('3: DIA DE SORTE')
    print('4: QUINA')
    print('5: LOTOMANIA')
    print('6: DUPLA-SENA\n')


    v_valida_lot_des = False
    while v_valida_lot_des == False:
        v_lot = input('Loteria desejada:')
        try:
            v_lot = int(v_lot)
            if v_lot <=0 or v_lot >6:
                print('Escolha inválida!\n')
            else:
                v_valida_lot_des = True
                v_lot = str(v_lot)
        except:
            print('Formato inválido!\n')

    v_valida_qtd_des = False
    while v_valida_qtd_des == False:
        v_qtd_j_des = input('Qtdade de jogos desejados (1 a 20):')
        try:
            v_qtd_j_des = int(v_qtd_j_des)
            if v_qtd_j_des <=0 or v_qtd_j_des >20:
                print('Escolha inválida!\n')
            else:
                v_valida_qtd_des = True
                #v_qtd_j_des = str(v_qtd_j_des)
        except:
            print('Formato inválido!\n')

    def loteria(num_ini, num_fim, nbolas, mes_i, mes_f):
        v_jogo = []
        while len(v_jogo) < nbolas:
            v_num = random.randint(num_ini, num_fim)
            #num = '%02d' % num #formatar número com 2 dígitos, para numeros < 10
            v_num = '%02d' % v_num
            if v_num in v_jogo:
                continue #(continue: volta para o loop)
            else:
                v_jogo.append(v_num)
        if mes_i == 0:
            return v_jogo
        else:
            v_mes = random.randint(mes_i, mes_f)
            return v_jogo, v_mes

    print('')

    v_loterias = {'1': 'MEGASENA', '2': 'LOTOFÁCIL', '3': 'DIA DE SORTE', '4': 'QUINA', '5': 'LOTOMANIA', '6': 'DUPLA-SENA'}

    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print(v_loterias.get(v_lot))
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('QTDADE JOGOS:', v_qtd_j_des)
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('NÚMEROS GERADOS:')
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')

    for i in range(v_qtd_j_des):
        if v_lot == '1':
            v_sorteio = loteria(1, 60, 6, 0, 0)
        elif v_lot == '2':
            v_sorteio = loteria(1, 25, 15, 0, 0)
        elif v_lot == '3':
            v_sorteio = loteria(1, 31, 7, 1, 12)
        elif v_lot == '4':
            v_sorteio = loteria(1, 80, 5, 0, 0)
        elif v_lot == '5':
            v_sorteio = loteria(0, 99, 50, 0, 0)
        elif v_lot == '6':
            v_sorteio = loteria(1, 50, 6, 0, 0)

        #print(sorted(sorteio))

        if v_lot == '3':
            v_meses = ('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO')
            v_sorteio_ordem_num = sorted(v_sorteio[0])
            print(v_sorteio_ordem_num)
            v_sorteio_ordem_mes = v_sorteio[1]
            print('Mês:', v_meses[int(v_sorteio_ordem_mes - 1)], '\n')
        else:
            v_sorteio_ordem = sorted(v_sorteio)
            print(v_sorteio_ordem, '\n')

    v_valida_saida = False
    while v_valida_saida == False:
        v_sair = input('Deseja jogar novamente? (S/N):').lower()
        if v_sair == 's':
            v_valida_saida = True
        elif v_sair == 'n':
            v_valida_saida = True
        else:
            print('Inválido!')

    if v_sair == 'n':
        break

os.system("cls")
print('Obrigado por ter utilizado meu gerador de loterias!\n')
print('1º projeto de conclusão do curso básico de Python "Aprenda Programação em Python 3 do Zero com Facilidade", do professor Ivan Lourenço Gomes, na plataforma UDEMY.\n')
print('Contato: jaques.pavan@gmail.com')

from game import *
from helper.helper import *

START = True
SELECTED = 0

menu()

while START:
    SELECTED = input('\nEscolha a opção desejada: ')

    if SELECTED == 'ajuda':
        system_help()

    if SELECTED == '1':
        print(game(number_of_players=4,
                   max_matches=1000,
                   number_of_rounds=300,
                   board_size=20,
                   initial_value=300,
                   dice_side=6,
                   min_sell_value_per_property=100,
                   max_sell_value_per_propertye=150,
                   percentage_rent_value_per_property=0.2,
                   modality='default'))
        START = False

    if SELECTED == '2':
        NUMBER_OF_PLAYERS = input('Insira o número de jogadores: ')
        INITIAL_VALUE = input('Insira o saldo inicial: ')

        while int(NUMBER_OF_PLAYERS) < 2:
            print('O número mínimo de jogadores é 2')
            NUMBER_OF_PLAYERS = input('Insira o número de jogadores: ')

        MAX_MATCHES = input('Insira o número máximo de partidas: ')
        NUMBER_OF_ROUNDS = input('Insira o número de jogos: ')
        BOARD_SIZE = input('Insira o tamanho do tabuleiro: ')
        MIN_SELL_VALUE_PER_PROPERTY = input(
            'Insira o valor mínimo de venda de propriedade: ')
        MAX_SELL_VALUE_PER_PROPERTY = input(
            'Insira o valor máximo de venda de propriedade: ')
        PERCENTAGE_RENT_VALUE_PER_PROPERTY = input(
            'Insira o percentual de aluguel de propriedade: ')
        DICE_SIDE = input('Insira o número de lados do dado: ')

        print(
            game(
                number_of_players=int(NUMBER_OF_PLAYERS),
                max_matches=int(MAX_MATCHES),
                number_of_rounds=int(NUMBER_OF_ROUNDS),
                board_size=int(BOARD_SIZE),
                initial_value=int(INITIAL_VALUE),
                dice_side=int(DICE_SIDE),
                min_sell_value_per_property=int(MIN_SELL_VALUE_PER_PROPERTY),
                max_sell_value_per_propertye=int(MAX_SELL_VALUE_PER_PROPERTY),
                percentage_rent_value_per_property=float(PERCENTAGE_RENT_VALUE_PER_PROPERTY),
                modality='config'))
        START = False

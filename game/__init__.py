import random
import collections

from dice.dice import Dice
from board.board import Board
from player.player import Player
from player.names import NAMES


def game(
        number_of_players,
        max_matches,
        number_of_rounds,
        board_size,
        min_sell_value_per_property,
        max_sell_value_per_propertye,
        percentage_rent_value_per_property,
        dice_side,
        initial_value,
        modality):
    """Function that create the game"""
    dice = Dice(dice_side)
    board = Board(
        board_size,
        min_sell_value_per_property,
        max_sell_value_per_propertye,
        percentage_rent_value_per_property)

    winners = list()
    number_of_matches = list()
    finished_by_time_out = 0

    players = []
    positions = [item for item in range(0, number_of_players)]
    random.shuffle(positions)

    if modality == 'default':
        players = default_players(initial_value, positions)

    else:
        for player in range(0, number_of_players):
            player_name = input(
                'Escreva o nome do player_' + str(player) + ': ')
            player_conduct = input(
                'Escreva o perfil do player_' + str(player) + ': ')
            while player_conduct not in [
                    'impulsive', 'demanding', 'cautious', 'random']:
                print(
                    'Os perfis disponíveis são: impulsive, demanding, cautious e random')
                player_conduct = input(
                    'Escreva o perfil do player_' + str(player) + ': ')

            players.append(
                Player(
                    player_name,
                    player_conduct,
                    initial_value,
                    positions[player]))
            print('Jogador adicionado')

    for round_of_play in range(0, number_of_rounds):

        board.reset()

        for num, player in enumerate(players, start=0):
            player.reset(initial_value, positions[num])

        players = sorted(players, key=lambda i: i.position)

        for match in range(0, max_matches):
            default_match(players, board, dice)

            if len(
                    list(
                        filter(
                            lambda player: player.status == 'lost',
                            players))) == 3:
                break

        if match == (max_matches - 1):
            finished_by_time_out += 1

        number_of_matches.append(match)
        winners.append(set_winner(players).conduct)

    return report(number_of_matches, winners, finished_by_time_out)


def default_players(initial_value, positions):
    """Function that create the default players"""
    return [Player(NAMES[random.randint(0, 4500)], 'impulsive', initial_value, positions[0]),
            Player(NAMES[random.randint(0, 4500)], 'demanding', initial_value, positions[1]),
            Player(NAMES[random.randint(0, 4500)], 'cautious', initial_value, positions[2]),
            Player(NAMES[random.randint(0, 4500)], 'random', initial_value, positions[3])]


def default_match(players, board, dice):
    """Function that create the match"""
    for player in players:
        if player.status != 'lost':
            player.dafault_move(board, dice)


def set_winner(players):
    """Function that validates the winner"""
    if len(
            list(
                filter(
                    lambda player: player.status == 'active',
                    players))) > 1:
        player_lenght = len(
            list(
                filter(
                    lambda player: player.status == 'active',
                    players)))
        winner = sorted(players, key=lambda i: i.balance)[player_lenght - 1]
    else:
        winner = list(
            filter(
                lambda player: player.status == 'active',
                players))[0]

    return winner


def report(number_of_matches, winners, finished_by_time_out):
    """Function that creates a simple report"""
    return {
        'Média de partidas': sum(number_of_matches) / len(number_of_matches),
        'Ganhadores impulsivos (%)': str(
            (collections.Counter(winners)['impulsive'] / len(winners)) * 100) + '%',
        'Ganhadores exigentes (%)': str(
            (collections.Counter(winners)['demanding'] / len(winners)) * 100) + '%',
        'Ganhadores cautelosos (%)': str(
            (collections.Counter(winners)['cautious'] / len(winners)) * 100) + '%',
        'Ganhadores aleatórios (%)': str(
            (collections.Counter(winners)['random'] / len(winners)) * 100) + '%',
        'Jogos finalizados por timed out': finished_by_time_out}

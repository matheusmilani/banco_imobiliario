import random

CONDUCT = ['impulsive', 'demanding', 'cautious', 'random']


class Player():
    """Initializes a player with:
    \n - name \n - conduct \n - balance
    \n - position \n - board_step \n - status"""
    def __init__(self, name, conduct, balance, position):
        self.name = name
        self.conduct = conduct
        self.balance = balance
        self.position = position
        self.board_step = 0
        if balance > 0:
            self.status = 'active'

    def reset(self, balance, position):
        """Reset the player to initial state"""
        self.balance = balance
        self.position = position
        self.board_step = 0
        if balance > 0:
            self.status = 'active'

        return self

    def check_status(self):
        """Check and change the status from player to 'lost' if necesairy"""
        self.status = 'lost' if self.balance <= 0 else 'active'
        return self

    def move(self, dice, board):
        """Moves the player across the board"""

        dice_play = dice.play()
        board_step = self.board_step + dice_play
        if board_step > (board.size - 1):
            board_step = board_step - board.size
            self.balance += 100
        self.board_step = board_step

    def dafault_move(self, board, dice):
        """Moves the player across the board according to his conduct"""

        self.move(dice, board)

        if self.conduct == 'impulsive':
            self.impulsive_move(board.property[self.board_step])
        elif self.conduct == 'demanding':
            self.demanding_move(board.property[self.board_step])
        elif self.conduct == 'cautious':
            self.cautious_move(board.property[self.board_step])
        elif self.conduct == 'random':
            self.random_move(board.property[self.board_step])

        self.check_status()

        if self.status == 'lost':
            for board_property in board.property:
                if board_property.owner == self:
                    board_property.return_to_board()

        return self

    def impulsive_move(self, board_property):
        """The impulsive conduct buys every property if it has money"""

        if not board_property.buyed:
            if self.balance >= board_property.sell_value:
                board_property.buy(self)
                self.balance -= board_property.sell_value
        else:
            board_property.pay_rent(self)

        return self

    def demanding_move(self, board_property):
        """The demanding conduct buys every property if the rent value is upper then 50"""
        if not board_property.buyed:
            if board_property.rent_value > 50:
                if self.balance >= board_property.sell_value:
                    board_property.buy(self)
                    self.balance -= board_property.sell_value
        else:
            board_property.pay_rent(self)

        return self

    def cautious_move(self, board_property):
        """The cautious conduct buys every property if his final balance is upper than 80"""
        if not board_property.buyed:
            future_balance = self.balance - board_property.sell_value
            if future_balance > 80:
                board_property.buy(self)
                self.balance -= board_property.sell_value
        else:
            board_property.pay_rent(self)
        return self

    def random_move(self, board_property):
        """The random conduct buys a property if the random is 1"""
        rand = random.randint(0, 1)
        if not board_property.buyed:
            if rand == 0:
                if self.balance >= board_property.sell_value:
                    board_property.buy(self)
                    self.balance -= board_property.sell_value
        else:
            board_property.pay_rent(self)
        return self

from board.property import Property


class Board():
    """Initializes the board"""
    def __init__(
            self,
            size,
            min_sell_value_per_property,
            max_sell_value_per_property,
            percentage_rent_value_per_property):
        self.size = size
        self.property = [Property(
            min_sell_value_per_property,
            max_sell_value_per_property,
            percentage_rent_value_per_property) for i in range(0, size)]


    def reset(self):
        """Reset the board to default and his properties"""
        for board_property in self.property:
            board_property.buyed = False
            board_property.owner = None

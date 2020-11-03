from abc import ABC, abstractmethod

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
SELECT = "select"
ALL_COMMANDS = [UP, DOWN, LEFT, RIGHT, SELECT]


class Controller(ABC):

    @abstractmethod
    def get_input(self):
        pass

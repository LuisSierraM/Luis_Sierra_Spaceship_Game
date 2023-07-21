from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE


class Shield(PowerUp): #Clase escudo que hereda de la clase PowerUP

    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)

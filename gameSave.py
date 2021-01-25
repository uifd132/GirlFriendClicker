from girl_generator import girlGen
import numpy as np
        
class gameState:
    def __init__(self):
        self.affectionMultiplier = 1
        self.affection = 0
        self.toy_tab = False
        self.girl_cost = 100
        self.girl_bought = 0
        self.auto_clicker = 0
        self.auto_like = [0]
        self.auto_like_price = [20]
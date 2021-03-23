class Enemy():
    def __init__(self):
        self.map = 'assets/testmap.png'
        self.hp = 1
        self.xp = 1
        self.asset = "assets/L1E.png"
        self.x = 55
        self.y = 55
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def hit(self):  # This will display when the enemy is hit
        print('hit')

goblin = Enemy()
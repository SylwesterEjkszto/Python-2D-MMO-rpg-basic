class Attack():
    def __init__(self,name,dmg,texture):
        self.hitbox = 400
        self.name = name
        self.dmg = dmg
        self.description = ""
        self.texture = texture

Jiba = Attack("Jiba",1,"assets/jiba1.png")
Howa = Attack("Hōwa",0,"assets/jiba.png")
attacks_list = [Jiba,Howa]

class Attack():
    def __init__(self,name,dmg,texture):
        self.hitbox = 40
        self.name = name
        self.dmg = dmg
        self.description = ""
        self.texture = texture
# Podczas rysowania ataków dodaj hitbox to x i y postaci, np odpalasz postać w programie graficznym, najeżdzasz na stope masz koordynaty 43,63
# Jeżeli jiba ma hitbox 40 to robisz grafike 64+40 x 64+40 a postać stawiasz na 43+40, 63+40
Jiba = Attack("Jiba",1,"assets/jiba1.png")
Howa = Attack("Hōwa",0,"assets/jiba.png")
attacks_list = [Jiba,Howa]

class Monster:
    def __init__(self, hp, name, attack_power, heal_power):
        self.__hp = hp
        self.name = name
        self.attack_power = attack_power
        self.heal_power = heal_power

    def get_hp(self):
        return self.__hp

    def take_damage(self, damage):
        self.__hp -= damage

    def heal(self):
        self.__hp += self.heal_power

    def attack(self, enemy):
        enemy.take_damage(self.attack_power)

class Dragon(Monster):
    def __init__(self):
        super().__init__(50, "Dragon", 10, 5)

    def attack(self, enemy):
        enemy.take_damage(self.attack_power)

class Slime(Monster):
    def __init__(self):
        super().__init__(100, "Slime", 5, 10)

    def attack(self, enemy):
        enemy.take_damage(self.attack_power)

class Player:
    def __init__(self, monster):
        self.monster = monster

dragon = Dragon()
slime = Slime()

while True:
    chosen_monster = input("Välj ett monster, (D)ragon eller (S)lime: ").lower().strip()

    if chosen_monster == "d" or chosen_monster == "dragon":
        player = Player(dragon)
        enemy = slime
        print("Du valde Dragon!🐲")
        break

    elif chosen_monster == "s" or chosen_monster == "slime":
        player = Player(slime)
        enemy = dragon
        print("Du valde Slime!🟩")
        break

    else:
        print("Ange ett giltigt val!⚠️")

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        while True:
            
            print()
            print(self.player.monster.name, "HP:", self.player.monster.get_hp(),"❤️")
            print(self.enemy.name, "HP:", self.enemy.get_hp(),"❤️")
            
            choice = input("Välj (A)ttack eller (H)eal: ").lower().strip()

            if choice == "a" or choice == "attack":
                self.player.monster.attack(self.enemy)
                print()
                print(self.player.monster.name, "attackerade", self.enemy.name, "med", self.player.monster.attack_power, "damage!⚔️")

            elif choice == "h" or choice == "heal":
                self.player.monster.heal()
                print()
                print(self.player.monster.name, "healade sig själv med", self.player.monster.heal_power, "HP!🩹")

            else:
                print("Ange ett giltigt val!⚠️")
                continue

            if self.enemy.get_hp() <= 0:
                print("Du vann!🏆")
                break

            self.enemy.attack(self.player.monster)
            print()
            print(self.enemy.name, "attackerade", self.player.monster.name, "med", self.enemy.attack_power, "damage!⚔️")

            if self.player.monster.get_hp() <= 0:
                print("Du förlorade!💀")
                break

battle = Battle(player, enemy)
battle.start()
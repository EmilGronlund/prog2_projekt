SKAPA klass Monster
    ha privat HP
    ha namn
    ha attack_power
    ha heal_power

    METOD attack()
        attackera motståndaren

    METOD take_damage(skada)
        minska HP

    METOD heal()
        öka HP

    METOD get_hp()
        returnera privat HP


SKAPA klass Dragon som ärver Monster
    METOD attack()
        gör mycket skada


SKAPA klass Slime som ärver Monster
    METOD attack()
        gör lite skada


SKAPA klass Player
    ha ett Monster


SKAPA klass Battle
    ha två Monster

    STARTA strid

    SÅ LÄNGE båda monstren lever
        monster 1 attackerar monster 2
        OM monster 2 har 0 HP
            avsluta striden

        monster 2 attackerar monster 1
        OM monster 1 har 0 HP
            avsluta striden

    VISA vilket monster som vann
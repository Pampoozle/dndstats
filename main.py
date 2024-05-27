from random import randint

def main():
    strenght = roll_stats()
    dexterity = roll_stats()
    constitution = roll_stats()
    intelligence = roll_stats()
    wisdom = roll_stats()
    charisma = roll_stats()
    
    print("******** Here are your stats********")
    print("Strenght:")
    print(strenght)
    print("Dexterity:")
    print(dexterity)
    print("Constitution:")
    print(constitution)
    print("Intelligence:")
    print(intelligence)
    print("Wisdom:")
    print(wisdom)
    print("Charisma:")
    print(charisma)


def roll_stats():
    rolls = [randint(1,6)] + [randint(1,6)] + [randint(1,6)] + [randint(1,6)]
    rolls.sort(reverse=True, key=None)
    print(f"You rolled {rolls}")
    rolls.pop()
    stat = rolls[0] + rolls[1] + rolls[2]
    return stat



main()


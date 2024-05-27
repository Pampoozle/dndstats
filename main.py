from random import randint

def main():
    strenght = roll()
    dexterity = roll()
    constitution = roll()
    intelligence = roll()
    wisdom = roll()
    charisma = roll()
    all_stats = {"Strenght": strenght,"Dexterity": dexterity,"Constitution": constitution,"Intelligence": intelligence,"Wisdom": wisdom,"Charisma": charisma}
    
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

# Working on best_stat right now
    best_stat(all_stats)


def roll():
    rolls = [randint(1,6)] + [randint(1,6)] + [randint(1,6)] + [randint(1,6)]
    rolls.sort(reverse=True, key=None)
    print(f"You rolled {rolls}")
    rolls.pop()
    stat = rolls[0] + rolls[1] + rolls[2]
    return stat

def best_stat(all_stats):
    highest = float('-inf')
    best_stat = {}
    for i in all_stats:
        if all_stats[i] >= highest:
            highest = all_stats[i]

    best_stat = {i for i in all_stats if all_stats[i] == highest}
    print(f"Your best stat is {best_stat}")
    return best_stat



main()


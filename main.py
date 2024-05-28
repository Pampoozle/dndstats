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

    best_stat(all_stats)
    print("*****************************")
    suggest_class(all_stats)
    


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

def suggest_class(all_stats):
    best_class = {}
    highest = float('-inf')
    class_dict = {
        "barbarian" : 0,
        "bard" : 0,
        "cleric" : 0,
        "druid" : 0,
        "fighter" : 0,
        "monk" : 0,
        "paladin" : 0,
        "ranger" : 0,
        "rogue" : 0,
        "sorcerer" : 0,
        "warlock" : 0,
        "wizard" : 0
        }
    
    if all_stats["Strenght"] >= 14:
        class_dict["barbarian"] += 4
        class_dict["fighter"] += 1
        class_dict["paladin"] += 3

        
    elif all_stats["Dexterity"] >= 14:
        class_dict["rogue"] += 5
        class_dict["monk"] += 4
        class_dict["bard"] += 3
        class_dict["ranger"] += 4
        class_dict["fighter"] += 1
        
        
    elif all_stats["Constitution"] >= 14:
        class_dict["barbarian"] += 4
        class_dict["druid"] += 4
        class_dict["cleric"] += 2
        class_dict["fighter"] += 1
        
        
    elif all_stats["Intelligence"] >= 14:
        class_dict["wizard"] += 8
        class_dict["sorcerer"] +=5
        
        
    elif all_stats["Wisdom"] >= 14:
        class_dict["cleric"] += 7
        class_dict["druid"] += 4
        class_dict["monk"] += 3
        class_dict["paladin"] += 3
        class_dict["ranger"] += 2
        
        
    elif all_stats["Charisma"] >= 14:
        class_dict["bard"] += 3
        class_dict["sorcerer"] += 5
        class_dict["warlock"] += 8
        class_dict["rogue"] += 2
        
        
    else:
        for s in all_stats:
            if all_stats[s] < 10:
                class_dict["fighter"] += 1

    for i in class_dict:
        if class_dict[i] >= highest:
            highest = class_dict[i]
    best_class = {i for i in class_dict if class_dict[i] == highest}
    print(f"You should play {best_class}")
    return best_class



main()


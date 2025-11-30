'''
Create a class Player with:
-> a class variable player_count
-> instance variables name and level
Track how many players were created.
'''

class Player:
    player_count = 0

    def __init__(self,name,level):
        self.name = name
        self.level = level
        Player.player_count += 1


while True:
    name = input("Enter name : ")
    level = int(input("Enter level : "))
    if name == "stop" :
        break
    obj = Player(name, level)


print(f"Total Count of player is = {Player.player_count}")

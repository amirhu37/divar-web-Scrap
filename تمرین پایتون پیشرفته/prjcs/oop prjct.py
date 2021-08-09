import random
class man():
    all_name = list()
    inn = input('input names: ').split(' - ')
    all_name.append(inn)
    def __init__(slef):
        self.tag = tag

class player(man):
    a_team = list()
    b_team = list()
    random.shuffle(man.all_name)
    for x in range(0,11):
        poping = man.all_name[0].pop(random.randrange(len(man.all_name[0])))
        a_team.append(poping)
    for x in range(0,11):
        poping = man.all_name[0].pop(random.randrange(len(man.all_name[0])))
        b_team.append(poping)

print('A team is :')
for i in range(len(player.a_team)):
    print(player.a_team[i] , end = '-')
print('\n')
print('B team is: ')
for i in range(len(player.b_team)):
    print(player.b_team[i] , end = '-')

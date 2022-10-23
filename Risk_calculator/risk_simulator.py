import random as rand

def attack (attacker_no, defender_no):
    while attacker_no > 1 and defender_no > 0:
        attacker_dice = rand.sample (range (1,7),3)
        defender_dice = rand.sample (range (1,7),2)
        
        for i in range (0,(4-attacker_no) * (attacker_no <= 3)): ### Remove the excess dice number if no. of attackers  <=3 
            attacker_dice[i] = 0

        if defender_no == 1: ### Remove excess number if no. of defenders < 2
            defender_dice[0] = 0  
        
        attacker_dice.sort(reverse = True)
        defender_dice.sort(reverse = True)
        #print (attacker_dice, defender_dice)
        
        for i in range (0, min(defender_no,attacker_no-1,2)):
            if attacker_dice[i] <= defender_dice[i]:
                attacker_no -= 1
            else:
                defender_no -= 1
        
        #print (attacker_no, defender_no)
    
    return (attacker_no, defender_no)

attacker_no = 3
defender_no = 1

#print (attack(20,20))
survivor_list = []
defensive_win = 0
for i in range (100000):
    survivor = (attack(attacker_no, defender_no))
    survivor_list. append (survivor[0])
    defensive_win += (survivor[1] > 0)
    
print (sum(survivor_list)/len(survivor_list))
print (f'win_rate = {1-defensive_win/len(survivor_list)}')


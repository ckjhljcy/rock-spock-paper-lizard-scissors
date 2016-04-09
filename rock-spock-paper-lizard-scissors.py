import random
dic = ('rock', 'Spock', 'paper', 'lizard', 'scissors')

def number_to_name(number):
    return dic[number]
    
def name_to_number(guess):
    return dic.index(guess)

def rpsls(guess):
    computer = random.randrange(0,4)
    print('Player choose' + guess)
    print("Computer choose " + number_to_name(computer))
    result = (name_to_number(guess) - computer) % 5
    if(result == 0):
        print("Player and Computer tie!\n")
    elif(result <= 2):
        print("Player wins!\n")
    else:
        print("Computer wins!\n")
        
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

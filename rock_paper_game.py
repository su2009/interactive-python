# -*- coding: utf-8 -*- 

import random

def name_to_number(name):
    if name == 'rock':
       return 0
    if name == 'spock':
       return 1
    if name == 'paper':
       return 2
    if name == 'lizard':
       return 3
    if name == 'scissors':
       return 4
      
      
      
def number_to_name(number):
    if number == 0:
def name_to_number(name):
    if name == 'rock':
       return 0
    if name == 'spock':
       return 1
    if name == 'paper':
       return 2
    if name == 'lizard':
       return 3
    if name == 'scissors':
       return 4
      
      
      
def number_to_name(number):
    if number == 0:
       return 'rock'
    if number == 1:
       return 'spock'
    if number == 2:
       return 'paper'
    if number == 3:
       return 'lizard'
    if number == 4:
       return 'scissors'


def rpsls(choice):
    user_num = name_to_number(choice)
    pc_num = random.randrange(0,5)
    pc_name = number_to_name(pc_num)
    dif = user_num - pc_num
        
    if dif == 0:
       print "equal"
    elif 0 < dif <= 2:
       print "Player chooses %s" %choice
       print "Computer chooses %s" %pc_name
       print "Player wins!"
    elif dif<= -3:
       print "Player chooses %s" %choice
       print "Computer chooses %s" %pc_name
       print "Player wins!"
    else:
       print "Player chooses %s" %choice
       print "Computer chooses %s" %pc_name
       print "Computer wins!"


print "Let's play the rpsls game. Please input your choice - rock, spock, paper, lizard,or scissors?"
user_name = raw_input(">")
print user_name
list = ['rock','spock','paper','lizard','scissors']
while user_name not in list:
    print "You input is %s, not in our lists." %user_name
    print "Please input your choice - rock, spock, paper, lizard,or scissors?"
    user_name = raw_input(">")
else: 
    rpsls(user_name)
    exit()
        
    
    
    
# note: better way to do the number comparison: use module number

if (comp_number + 1) % 5 == player_number:
        print "Player wins!"
    elif (comp_number + 2) % 5 == player_number:
        print "Player wins!"
    elif comp_number == player_number:
        print "Player and computer tie!"
    else:
        print "Computer wins!"
    print ""    

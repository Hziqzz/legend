print("*******************************") 
print("*Welcome to the Caveman Battle*") 
print("*******************************")

#Ask player 1 for their name 
player1_name = input("Player 1, what is your name?") 
 
player2_name = input("Player 2, what is your name?") 
 
#set the initial health,ammo and damages 
player1_health = 90 
player1_ammo = 55 
player1_damage = 33 
 
player2_health = 122 
player2_ammo = 52 
player2_damage = 22 
 
print("\n" + player1_name + "has " + str(player1_health) + " health" + str(player1_ammo) + " rounds of ammo" + str(player1_damage) + " damage") 
print("\n" + player2_name + "has " + str(player2_health) + " health" + str(player2_ammo) + " rounds of ammo" + str(player2_damage) + " damage") 
 
print('\n Your cave suddenly is attacked by wild animals. What do you do?') 
print('1. Fight') 
print('2. Run') 
print('3. Search for supplies')

player1_choice = int(input(player1_name + " , enter 1,2 or 3:")) 
player2_choice = int(input(player2_name + " , enter 1,2 or 3:")) 
 
if player1_choice == 1: 
    print('\n '+ player1_name + 'decides to fight the intruders and does ' + str(player1_damage)+ " damage per shot! ") 
    player1_ammo -= 10 
    if player1_ammo > 0: 
        print('\n ' + player1_name + 'defeated the animals!!They have' + str(player1_ammo) + "rounds of ammo left") 
elif player1_choice == 2: 
    print('lived to fight another day')
    print('animals bitten player 2')
    print('animals does some damage to player 1')
    player2_health -= 28
    player1_health -= 11
    print(player2_name + ',current health is ' + str(player2_health))
    print(player1_name + ',current health is ' + str(player1_health))
    #animals bitten player 2
    #display player 2 health
    #animals does some damage to player 1
    #display player 1 name and health
elif player1_choice == 3: 
    print('the animals manage to chase them out') 
else: 
    print('Invalid input, sad day for the caveman')
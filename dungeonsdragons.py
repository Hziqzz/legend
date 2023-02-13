print("""

  _____  _    _ _   _  _____ ______ ____  _   _  _____            _____  _____            _____  ____  _   _  _____ 
 |  __ \| |  | | \ | |/ ____|  ____/ __ \| \ | |/ ____|   ___    |  __ \|  __ \     /\   / ____|/ __ \| \ | |/ ____|
 | |  | | |  | |  \| | |  __| |__ | |  | |  \| | (___    ( _ )   | |  | | |__) |   /  \ | |  __| |  | |  \| | (___  
 | |  | | |  | | . ` | | |_ |  __|| |  | | . ` |\___ \   / _ \/\ | |  | |  _  /   / /\ \| | |_ | |  | | . ` |\___ \ 
 | |__| | |__| | |\  | |__| | |___| |__| | |\  |____) | | (_>  < | |__| | | \ \  / ____ \ |__| | |__| | |\  |____) |
 |_____/ \____/|_| \_|\_____|______\____/|_| \_|_____/   \___/\/ |_____/|_|  \_\/_/    \_\_____|\____/|_| \_|_____/ 
                                                                                                                    

""")
print('Welcome to Dungeons & Dragons') 
 
player_name = input('What is your name, adventurer\n') 
 
health = 100 
damage = 20 
 
print('\nwelcome, ' + player_name + ' !you have ' + str(health) + ' health and can do damage ' + str(damage))
print('You came acress a dragon!! What will you do??') 
print('1. Fight') 
print('2. Run') 
 
choice = int(input('Enter either 1 or 2: ')) 
if choice == 1: 
    print("You attack the dragon and do " + str(damage) + ' damage') 
    print('the dragon back off, spit some acid and does 10 damage') 
    health -= 10 
    print('Your current health is ' + str(health)) 
elif choice== 2: 
    print('You run away from the dragon') 
    print('Dragon manage to throw rocks at you, deals with twice the damage you infict')
    health -= (10*2) 
    print('Your current health is ' + str(health))
    #Dragon manage to throw rocks at you deals with twice the damage you infict
    #Print your current health
else: 
    print('\nInvalid choice, the dragon get to eat you alive!!!') 
print("Thanks for playing!")

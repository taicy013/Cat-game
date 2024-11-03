from random import randint
import time 

def valid_task(entry):
    while entry.lower() not in ['play','sleep','train','show_stats','stats','showstats','show','quit']:
          entry = input("Invalid, choose from [Train, Play, Sleep, Show_Stats, Quit]: ")
    return entry.lower()

def play(car):
    car['energy']['level'] -= 5
    increase = randint(1,10)
    car['energy']['capacity'] += increase
    time.sleep(2)
    print("%s's energy capacity has increased by %d!" %(car['name'], increase))
    pick = randint(0,50)

    if 'hunting' in car.keys():
            print("%s's hunting skill has increased by %d!" %(car['name'], increase//2))
            car['hunting'] += increase//2
    elif pick >= 45:
        if 'hunting' not in car.keys():
            car['hunting'] = 5
            time.sleep(2)
            print("----- ANNOUNCEMENT!")
            time.sleep(2)
            print("New skill acquired!:- 'HUNTING'")
    print("%s's energy level: %s/%s" %(car['name'], car['energy']['level'], car['energy']['capacity']))
    
def train(car):
    car['energy']['level'] -= 4
    increase = randint(1,10)
    car['intelligence'] += increase
    time.sleep(2)
    print("%s's intelligence has increased by %d!" %(car['name'], increase))
    pick = randint(1,100)

    if 'wisdom' in car.keys():
            print("%s's wisdom has increased by %d!" %(car['name'], increase//2))
            car['wisdom'] += increase//2
    elif pick >= 80:
        if 'wisdom' not in car.keys():
            car['wisdom'] = 5
            time.sleep(2)
            print("----- ANNOUNCEMENT!")
            print("New skill acquired!:- 'WISDOM'")
            time.sleep(1)
    print("%s's energy level: %s/%s" %(car['name'], car['energy']['level'], car['energy']['capacity']))

def sleep(car):
    for i in range(randint(1,9)):
        print('s n o o z e . . .')
        time.sleep(2)
    car['energy']['level'] = car['energy']['capacity']
    print("Energy level now at max capacity!")

def show_stats(car):
    print("-----------  %s's STATS:  -----------" %(cat['name'].upper()))
    time.sleep(2)
    for k,v in car.items():
        print("%s: %s" %(k.upper(),v))

def end(entry):
    if entry.lower() in ['yes','yeah','ya','yas','yea','ye']:
        print("Quitting game...")
        time.sleep(2)
        return True
    else:
        print("Returning to game...")
    return False

cat = {'name':'',
        'colour': '',
        'intelligence': 10,
        'energy': {'level':50,'capacity':50},
        'weight': 10
    }

cat['name'] = input("Enter cat's name: \n")
cat['colour'] = input("Choose %s's colour: \n" %(cat['name']))
print('\n')
show_stats(cat)

quit = False
while not quit:
    print('\n')
    do = input("Tasks: [Train, Play, Sleep, Show_Stats, Quit]. What would you like to do? ")
    do = valid_task(do)

    if do == 'play':
        if cat['energy']['level'] >= 6:
            play(cat)
        else:
            print("%s's energy is too low! Rest first before playing :)" %(cat['name']))
    elif do == 'train':
        if cat['energy']['level'] > 5:
            train(cat)
        else:
            print("%s's energy is too low! Rest first before training :)" %(cat['name']))
    elif do == 'sleep':
        sleep(cat)
    elif do in ['show_stats','show','showstats','stats']:
        show_stats(cat)
    elif do == 'quit':
        user = input("Sure to quit?:\n")
        quit = end(user)



from random import randint

def play(car):
    car['energy'][0] -= 5
    car['energy'][1] += 3
    pick = randint(57,3065)
    if pick > 3000:
        if 'hunting' in car.keys():
            car['hunting'] += 3
        else: 
            car['hunting'] = 5
            print("New skill acqired!:- 'HUNTING'")
    



cat = {'name':'',
        'colour': '',
        'intelligence': 10,
        'energy': [50,50],
        'weight': 10
    }

cat['name'] = input("Enter cat's name: ")
cat['colour'] = input("Enter cat's colour: ")



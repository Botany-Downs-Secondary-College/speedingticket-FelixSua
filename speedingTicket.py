#speeding ticket
#Calculating speeding fine
#Felix S., Feb 2021

#variables & lists
wanted_names = ['dylan', 'chris']

#functions
def name():
    global name
    while True:
        try:
            name = input("What is your name?")
            name = name.lower()
            break
        except ValueError:
            print("Please enter a valid name")
    return name

def fineCalc():
    global fine
    fine = 0
    if 1 <= speedOver <= 10:
        fine += 30
    elif 10 <= speedOver <= 14:
        fine += 80
    elif 15 <= speedOver <= 19:
        fine += 120
    elif 20 <= speedOver <= 24:
        fine += 170
    elif 25 <= speedOver <= 29:
        fine += 230
    elif 30 <= speedOver <= 34:
        fine += 300
    elif 35 <= speedOver <= 39:
        fine += 400
    elif 40 <= speedOver <= 44:
        fine += 510
    elif 45 <= speedOver:
        fine += 630
    return fine

def speedLimit():
    global speedLimit
    while True:
        try:
            speedLimit = int(input("Please input the speed limit: "))
            break
        except ValueError:
            print("No algebra")
    return speedLimit

def speed():
    global speed
    while True:
        try:
            speed = int(input("Please input your speed: "))
            break
        except ValueError:
            print("We aren't doing algebra.")
    return speed

def fineSummary():
    if speedLimit <= speed:
        print(f"{name} went {speedOver}kmph over the speed limit,\nThis results in a ${fine} fine,")
    else:
        print("No charges are needed")

#Main routine
name()
if name in wanted_names:
    print('Go to jail')
else:
    speedLimit()
    speed()
    speedOver = speed - speedLimit
    fineCalc()
    fineSummary()



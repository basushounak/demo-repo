print("Hello World")

def basicfunc(s):
    if s == "y":
        print("Eat something")

    else:
        print("Go to sleep")
def sleepcyc(sleep):
    if sleep == 8:
        print("Complete Sleep")
    elif sleep < 8:
        print("Take Caffeine before work")
    else:
        print("You Dont need naps")
def calorieintake(cal):
    if cal == 3000:
        print("Consume within maintenance")
    elif (cal >= 2500) and (cal <= 2900):
        print("Bulk phase")
    else:
        print("Maintenance is reached")

s = input("Are you hungry?(y/n) : ")
sleep = int(input("How many hours of sleep are you on ? : "))
cal = int(input("What is your caloric intake? : "))
basicfunc(s)
sleepcyc(sleep)
calorieintake(cal)


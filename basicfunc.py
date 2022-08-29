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


s = input("Are you hungry?(y/n) : ")
sleep = int(input("How many hours of sleep are you on ? : "))
basicfunc(s)
sleepcyc(sleep)


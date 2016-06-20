import time
shipname = "onaple"
captain = "wallace"
location = "earth"
password = "wx131410"

pattempt = raw_input("Enter the password:  ")
while pattempt != password:
    print "password incorrect"
    pattempt = raw_input("Enter the password ")
print "Password correct. wellcome to the " + shipname
print ""
print "The spaceship " + shipname + " is currently visiting" + location + "."

choice = ""
while choice != "/exit":
    print "what would you like to do, " + captain + "?"
    print ""
    print "a. travel to another planet"
    print "b. fire cannons"
    print "c. open the airlock"
    print "d. self destory"
    print "/exit to exit"
    print ""
    choice = raw_input("enter your choice: ")
    
    if choice == "a":
        destination = raw_input("where would you like to go?")
        print "leaving " + location
        print "travellint to " + destination
        time.sleep(5)
        print "arrived at " + destination
        location = destination
    elif choice == "b":
        print "FIring cannons"
        time.sleep(1)
        print "bang"
        time.sleep(1)
    elif choice == "c":
        print "oopening airlock"
        time.sleep(3)
        print "airlock open"
        time.sleep(1)
    elif  choice == "d":
        confirm = raw_input("are you sure you want the ship to self destruct?(y/n)")
        if confirm == "y":
            print "ship will self destory in"
            print "3"
            time.sleep(1)
            print "2"
            time.sleep(1)
            print "1"
            time.sleep(1)
            print "goobye"
            print "boom"
            choice = "/exit"
    elif choice == "/exit":
        print "goodbye"
    else:
        print "invalid input. please select a, b, c, d, /exit to exit"

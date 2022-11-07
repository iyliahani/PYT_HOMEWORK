angry = True
bored = True
hungry = False
tired = False
happy = True

if tired and angry:
    print("He will eat the Iguanadon")
elif hungry and bored:
    print("He will eat the Iguanadon")
elif tired:
    print("He goes to sleep")
elif angry and bored:
    print ("He will fight with the Velociraptor.")
elif angry or bored:
    print("T-Rex roars! Rawr!")
else:
    print("Toothy smile")

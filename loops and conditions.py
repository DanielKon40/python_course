#new file for new subject

x = 0
my_bool = True

while(True):
    print("."*x, "$")

    if(my_bool):
        x += 1
        if(x > 10):
            my_bool = False
    else:
        x -= 1
        if(x < 1):
            my_bool = True

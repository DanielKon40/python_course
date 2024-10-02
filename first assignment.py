# פונקציה שמקבלת מספר ומדפיסה את כל המספרים הראשוניים עד אותו מספר שקיבל

def prime_num_printer():
    # asking for input
    num = int(input("Enter a number: \n"))
    # creating the loop
    for i in range(1, num+1):
        # setting the condition
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


if __name__ == '__main__':
    prime_num_printer()

# פונקציה שמבקשת שם פרטי, אם יש יותר מ5 אותיות היא מבקשת שם שני ואז משפחה, אם לא אז מבקשת שם משפחה ישר

# asking for input
first_name = input("Enter your first name: \n")
# counting the letters
char_count = len(first_name)
# setting the condition
if char_count > 5:
    second_name = input("Enter your second name: \n")
    last_name = input("Enter your last name: \n")
else:
    last_name = input("Enter your last name: \n")
# פונקציה שמקבלת 2 רישמות של מספרים ומחזירה רשימה אחת ממוינת

def merge_lists():
    # asking for input
    list_1 = input("Enter the first list: (Mind you use this format: X, Y, Z...) \n")
    list_2 = input("Enter the second list: \n")
    list_3 = []

    # splitting the lists
    split_list_1 = list_1.split(", ")
    split_list_2 = list_2.split(", ")

    # creating the new list
    for x in split_list_1:
      list_3.append(x)

    for x in split_list_2:
      list_3.append(x)

    # sorting with the new order
    list_3.sort()

    print(list_3)

if __name__ == '__main__':
    merge_lists()

"""list_a = ["banana", "tapuz", "melon"]
list_b = [1, 2, 3]

print(list_a[0])

list_a[0] = "tzabar"
print(list_a[0])

newlist = list_a + list_b
print(newlist)

list_b.extend(list_a)

print(list_b)
"""
"""
list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_a[3:6])
print(list_a[3:6:2])

listfromrange = list(range(20))
print(listfromrange)
listfromrange = list(range(5, 20))
print(listfromrange)
listfromrange = list(range(5, 30, 3))"""

"""
class mynewclass:
    def __init__(self, num):
        self.num = num
    def printnum(self):
        print(f"my num is: ({self.num})")
    def __repr__(self):
        return f"mynewclass({self.num})"

listofobj = []

for i in range (0, 20):
    listofobj.append(mynewclass(i))

print(listofobj)

for i in listofobj:
    i.printnum()

print("\n")
"""

list_a = [0, 1, 2, 3, 4]
print(list_a)
list_a.insert(0, "banana")
print(list_a)
"""list_a.remove(1)
print(list_a)
index = 2
x = list_a.pop(index)
print(x)
print(list_a)"""
del list_a[-1]
print(list_a)

anim_list = ["bear", "cat", "horse", "pig", "dog", "dog"]
"""print(anim_list.index("cat"))
print(anim_list.count("dog"))"""

list_a = [1, 5, 2, 5, 66, 600, 450]
list_a.sort(reverse = True)
print(list_a)

anim_list.sort(key=len)
print(anim_list)

list_b = list_a
list_c = list_a.copy()
list_a.append(99)

print(list_a)
print(list_b)
print(list_c)

mystr = "this is a long string, it has many words"
newlist = mystr.split(" ")
print(newlist)
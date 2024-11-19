"""set_a = {5, 6, 7, 8, 9, 10}
set_b = {7, 8, 9, 10, 3, 45}"""

"""print(set_a)
print(set_b)"""

set_a = {1, 2, 3}
set_b = {4, 5, 6}

print(set_a.isdisjoint(set_b))
set_a.add(6)
print(set_a.isdisjoint(set_b))

print(set_a.issubset(set_b))
print(set_a.issuperset(set_b))

"""print(len(set_a))"""
print(min(set_b))

print(sum(set_b))
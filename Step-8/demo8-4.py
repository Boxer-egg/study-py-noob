# demo8-4.py

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)  # 交集intersection()
s3 = (s1 | s2)  # 并集 union()
print(s1, s3)

print(s1-s2, s2-s1)  # 差集  difference()

print(s1 ^ s2)  # 对称差集  symmetric_difference()

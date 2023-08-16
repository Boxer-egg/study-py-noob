friends = ["小红", "小明", "小华", "小丽", "小王"]
for friend in friends:
    print(f"给{friend}分发了一块巧克力.")

for i in range(5):  # 这会执行5次，从0到4
    print("这是第", i + 1, "次循环")


water_level = 0
while water_level < 6:
    water_level += 1
    print("正在灌水，水位现在是:", water_level)


# test
# 假设您有一个空糖果罐，每次您可以加入2颗糖果。
# 请写一个while循环，当糖果少于10颗时，继续加糖果，并打印出当前糖果的数量。
suger = 0
while suger < 10:
    suger += 2
    print(f"现在有 {suger} 个糖果了")


frds = ["李雷", "韩梅梅", "Jim", "Tom"]
for frd1 in frds:
    print(f"你好，{frd1}")

for i in range(1, 6):
    print(i)

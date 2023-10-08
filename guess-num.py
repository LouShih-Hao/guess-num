# 產生一個隨機整數1~100（不要印出來）
# 讓使用者重複輸入數字去猜
# 猜對的話  印出＂終於猜對了！＂
# 猜錯的話  要告訴他  比答案大/小
# 延伸1：印出猜了幾次
# 延伸2：讓使用者決定隨機變數範圍

import random

# 決定範圍
start = int(input("請輸入隨機數字範圍的最小值："))
end = int(input("請輸入隨機數字範圍的最大值："))

num = random.randint(start,end)
count = 0 # 計次用

while True:
	count += 1
	guess = int(input("請輸入您所猜的數字："))
	if guess < num:
		print("比答案小")
	elif guess > num:
		print("比答案大")
	else:
		print("終於猜對了！")
		print("你已經猜", count, "次")
		break
	print("你已經猜", count, "次")

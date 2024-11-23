# 01 Date Types Nuber --> ตัวเลข (1.1 Integer, 1.2 Fleat, 1.3 Decimal)

# 1.1 Integer --> เลขจำนวนเต็มบวก
#     1.1.1 positive Number --> เลขจำนวนเต็มบวก --> 10, 20, 56, 32
#     1,1,2 negative Number --> เลขจำนวนเต็มลบ --> -10, -28, -56, -32
#     1,1,3 Zero  Number --> 0
#
# use case
# กำหนดข้อมูลขาเข้า --> int
# กำหนดข้อมูลขาออก --> %d


# 1.2 Flost --> เลขทศยิยม --> 1.15, 2.23. 5.23. 98.789654321

# use case
# กำหนดข้อมูลขาเข้า --> fioat
# กำหนดข้อมูลขาออก --> %.2f


#1.3 Decimal --> เลขฐาน 1e
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 1.1.1 Positive  Number
# Use case Same Integer --> Positive


import math

num_01 = 1 # Number --> Integer --> Positive
num_01 = 2 # Number --> Integer --> Positive
result = num_01 + num_02 # +, -, *, /, ** --> Operater

result = num_01 + num_02 # +, -, *, /, ** --> Operator

print(result) #--> Normal Displsy

print("Sum numl & num2: %d" %result) #Advance Display --> Integer

print("Sum numl & num2: %.2f" %result) #Advance Display --> float
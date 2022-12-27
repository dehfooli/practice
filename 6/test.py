# year = int(input()) 
# if year % 4 == 0:
#    if year % 100 == 0:
#        if year % 400 == 0:
#            print("Leap year")
#        else:
#            print("Not a leap year") 
#    else:
#           print("Leap year") 
# else:
#    print("Not a leap year")

# if (1 == 1) and (2 + 2 > 3):
#   print("true")
# else:
#   print("false")


# p = float(input())
# if p >= 75.0 and p < 83.3:
# 	print('18'+'K')
# elif p >= 83.3 and p < 91.7:
# 	print('20'+'K')
# elif p >= 91.7 and p < 99.9:
# 	print('22'+'K')
# elif p >= 99.9:
# 	print('24'+'K')

# if not True:
#    print("1")
# elif not (1 + 1 == 3):
#    print("2")
# else:
#    print("3")

#    i = 1
# while i <=5:
#    print(i)
#    i = i + 1

# print("Finished!")

# i = 3
# while i>=0:
#    print(i)
#    i = i - 1

# x = 1
# while x < 10:
#   if x%2 == 0:
#     print(str(x) + " is even")
#   else:
#     print(str(x) + " is odd")

#   x += 1

shots = input()
score = input()

while shots > 0:
    result = input()
    if result == "hit":
        score +=10
        shots -=1
    elif result == "miss":
        score -=20
        shots -=1
print(score)
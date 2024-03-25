import random

while True:
   a = random.randint(1,100)
   b = random.randint(1,100)

   ans = a+b
   input_ans = int(input(f"{a} + {b} = "))

   if ans == input_ans:
       print("잘했어요!!")
   else:
       print("틀렸어요. 하지만 다음번에는 잘할 수 있죠?")
       break
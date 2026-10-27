num = int(input())
love = " that I love"
hate = " that I hate"
feeling = love + hate
if num > 1 and num % 2 != 0:
    print(f"I hate{(num//2)*feeling} it")
elif num > 1 and num % 2 == 0:
    print(f"I hate{((num-2)//2)*feeling + love} it")
else:
    print("I hate it")

# Alternate Solution:
# print(*(['I hate','I love']*50)[:int(input())],sep=' that ',end=' it')

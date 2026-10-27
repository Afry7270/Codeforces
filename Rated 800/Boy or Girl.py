user_name = list(input())
no_dupe = list(dict.fromkeys(user_name).keys())
length = len(no_dupe)
if length % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
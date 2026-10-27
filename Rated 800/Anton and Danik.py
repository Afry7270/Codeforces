game_no = int(input())
sequence = input()
anton = sequence.count('A')
danik = sequence.count('D')

if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")

music = list(input().split('WUB'))
for i in music:
    if i == '':
        music.remove(i)
print(*music)

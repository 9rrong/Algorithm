N, game = input().split()
players = dict()

for _ in range(int(N)):
    players[input()] = 0

if game == "Y":
    div = 1
elif game == "F":
    div = 2
elif game == "O":
    div = 3

print(len(players.keys()) // div)

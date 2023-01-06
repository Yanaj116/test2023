#!/data/anaconda3/envs/python38/bin/python
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}x{i}={i*j}\t', end='')
    print()

guess, ans = 0, 100
while guess != ans:
    guess = int(input())
    if guess > ans:
        print("larger than expected")
    if guess < ans:
        print("less than expected")
print('you win')
pages = 148
secretPage = 124
up= pages
down = 0
guess = (up +down) //2
while guess !=secretPage:
    if guess > secretPage:
        up = guess
    elif guess < secretPage:
        down= guess
    guess = (up+down) //2
print(guess)

#It's more efficient than guess and check algorithm

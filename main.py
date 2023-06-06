import random
moves =["rock", "paper", "scissor"]
while True:
    ucount=0
    ccount=0
    uc = int(input('''
    Game Start
    1. Yes
    2. No/Exit
    '''))
    if uc<=1:
        for a in range (1,4):
            userinput = int(input('''
            1. Rock
            2. Scissor
            3. Paper
            '''))
            if userinput == 1:
                un = "Rock"
            elif userinput == 2:
                un = "Scissor"
            elif userinput == 3:
                un = "Paper"
            cn = random.choice(moves)
            if cn == un:
                print("Computer Value", cn)
                print("User Value", un)
                print("Game Draw")
                ucount = ucount+1
                ccount = ccount+1
            elif (un=="rock" and cn=="scissor") or (un=="paper" and cn=="rock") or (un=="scissor" and cn=="paper"):
                print("Computer Value", cn)
                print("User Value", un)
                print("You Win")
                ucount = ucount+1
            else:
                print("Computer Value", cn)
                print("User Value", un)
                print("Computer Win")
                ccount = ccount + 1
        if ucount == ccount:
            print("Final Game Draw")
            print("User Value", ucount)
            print("Computer Value", ccount)
        elif ucount > ccount:
            print("Final You Win")
            print("User Value", ucount)
            print("Computer Value", ccount)
        else:
            print("Final Computer Win")
            print("User Value", ucount)
            print("Computer Value", ccount)
    else:
        break


#Choose number of odds and type of odds in text-based UI
def main():
    print("Welcome to SureBet Calculator")
    print("Choose number of odds:")
    numOdds = int(input("0: Three-way | 1: Two way\n"))
    #check if User inputs valid choice (0 or 1 only)
    while numOdds != 0 and numOdds != 1:
        print("Error: Invalid choice")
        numOdds = int(input("0: Three-way | 1: Two way\n"))

    print("Choose type of odds: ")
    #check if User inputs valid choice (0 or 1 only)
    typeOdds = int(input("0: American (+125,-150) | 1: Decimal (1.33, 3.12)\n"))
    while typeOdds != 0 and typeOdds != 1:
        print("Error: Invalid choice")
        typeOdds = int(input("0: American (+125,-150) | 1: Decimal (1.33, 3.12)\n"))

    print("Enter Odds: ")
    #odds will be converted to dec, so format as float instead of int
    if numOdds == 0:
        oddA = float(input("Enter First odd: "))
        oddB = float(input("Enter Second odd: "))
        oddC = float(input("Enter Third odd: "))
        if typeOdds == 1:
            #Determine if a surebet exists
            if_Arb(oddA, oddB, oddC)
        else:
            if_Arb(American_to_Dec(oddA), American_to_Dec(oddB), American_to_Dec(oddC))
    else:
        oddA = float(input("Enter First odd: "))
        oddB = float(input("Enter Second odd: "))
        if typeOdds == 1:
            if_Arb(oddA, oddB, 0)
        else:
            if_Arb(American_to_Dec(oddA), American_to_Dec(oddB), 0)

#func to convert american odds to decimal
def American_to_Dec(odd):
    if odd > 0:
        odd = float((odd / 100) + 1)
    else:
        odd = float(1 - (100/odd))
    return odd

#func to determine if a surebet exists

def if_Arb(oddA, oddB, oddC):
    if oddC == 0:
        try:
            ret = (1/oddA) + (1/oddB)
        except:
            print("Error: Invalid Odds")
        else:
            output(ret, oddA, oddB, 0)
    if oddC > 0:
        try:
            ret = (1/oddA) + (1/oddB) + (1/oddC)
        except:
            print("Error: Invalid Odds")
        else:
            output(ret, oddA, oddB, oddC)

#output potential return of surebet and amounts to stake on each side of the bet
def output(ret, oddA, oddB, oddC):
    if ret >= 1:
        print(f"No Sure Bet found, guaranteed loss of {round((ret - 1) * 100, 2)}%")

    #if a surebet exists, calculate the amount to stake and potential return
    if ret > 0 and ret < 1 and oddC > 0:
        stakeA = round((100/oddA), 2)
        stakeB = round((100/oddB), 2)
        stakeC = round((100/oddC), 2)
        print(f"Sure Bet Found! Guaranteed return of {round((ret-1) * 100, 2)}%")
        print(f"Stake A: ${stakeA}, Stake B: ${stakeB}, Stake C: ${stakeC}")
        print(f"A bet of ${stakeA + stakeC + stakeB} will return $100")

    if ret > 0 and ret < 1 and oddC <= 0:
        stakeA = round((100/oddA), 2)
        stakeB = round((100/oddB), 2)
        print(f"Sure Bet Found! Guaranteed return of {round((1-ret) * 100, 2)}%")
        print(f"Stake A: ${stakeA}, Stake B: ${stakeB}")
        print(f"A bet of ${stakeA + stakeB} will return $100")

main()

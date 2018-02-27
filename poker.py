import random

deck = [
    ["A♠",1,1,1],
    ["2♠",2,1,2],
    ["3♠",3,1,3],
    ["4♠",4,1,4],
    ["5♠",5,1,5],
    ["6♠",6,1,6],
    ["7♠",7,1,7],
    ["8♠",8,1,8],
    ["9♠",9,1,9],
    ["10♠",10,1,10],
    ["J♠",11,1,11],
    ["Q♠",12,1,12],
    ["K♠",13,1,13],
    ["A♥",14,2,1],
    ["2♥",15,2,2],
    ["3♥",16,2,3],
    ["4♥",17,2,4],
    ["5♥",18,2,5],
    ["6♥",19,2,6],
    ["7♥",20,2,7],
    ["8♥",21,2,8],
    ["9♥",22,2,9],
    ["10♥",23,2,10],
    ["J♥",24,2,11],
    ["Q♥",25,2,12],
    ["K♥",26,2,13],
    ["A♣",27,3,1],
    ["2♣",28,3,2],
    ["3♣",29,3,3],
    ["4♣",30,3,4],
    ["5♣",31,3,5],
    ["6♣",32,3,6],
    ["7♣",33,3,7],
    ["8♣",34,3,8],
    ["9♣",35,3,9],
    ["10♣",36,3,10],
    ["J♣",37,3,11],
    ["Q♣",38,3,12],
    ["K♣",39,3,13],
    ["A♦",40,4,1],
    ["2♦",41,4,2],
    ["3♦",42,4,3],
    ["4♦",43,4,4],
    ["5♦",44,4,5],
    ["6♦",45,4,6],
    ["7♦",46,4,7],
    ["8♦",47,4,8],
    ["9♦",48,4,9],
    ["10♦",49,4,10],
    ["J♦",50,4,11],
    ["Q♦",51,4,12],
    ["K♦",52,4,13]
]

def NewHand():
    i = random.sample(range(0,51), 51)
    dealerCeiling = 1
    playerCeiling = 21
    main(i, playerCeiling,dealerCeiling)
   



def main(i, playerCeiling,dealerCeiling):
    x = 0
    y = 20
    DealerHandValue = 0
    PlayerHandValue = 0

    print("Dealer Hand: ")
    print(deck[i[0]][0])
    print("?")
    while x < dealerCeiling:
        DealerHandValue = DealerHandValue + deck[i[x]][2]
        x +=1
    print("\nPlayer Hand: ")
    while y <= playerCeiling:
        print(deck[i[y]][0])
        PlayerHandValue = PlayerHandValue + deck[i[y]][2]
        y +=1
    print("Total", PlayerHandValue)
    turn(i, playerCeiling, dealerCeiling, PlayerHandValue, DealerHandValue)

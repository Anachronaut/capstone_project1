import random


deck_dict ={
        '2\u2660':2,'3\u2660':3,'4\u2660':4,'5\u2660':5,'6\u2660':6,'7\u2660':7,'8\u2660':8,'9\u2660':9,'10\u2660':10,'J\u2660':10,'Q\u2660':10,'K\u2660':10,'A\u2660':11,  #Spades
        '2\u2663':2,'3\u2663':3,'4\u2663':4,'5\u2663':5,'6\u2663':6,'7\u2663':7,'8\u2663':8,'9\u2663':9,'10\u2663':10,'J\u2663':10,'Q\u2663':10,'K\u2663':10,'A\u2663':11,  #Clubs
        '2\u2665':2,'3\u2665':3,'4\u2665':4,'5\u2665':5,'6\u2665':6,'7\u2665':7,'8\u2665':8,'9\u2665':9,'10\u2665':10,'J\u2665':10,'Q\u2665':10,'K\u2665':10,'A\u2665':11,  #Hearts
        '2\u2666':2,'3\u2666':3,'4\u2666':4,'5\u2666':5,'6\u2666':6,'7\u2666':7,'8\u2666':8,'9\u2666':9,'10\u2666':10,'J\u2666':10,'Q\u2666':10,'K\u2666':10,'A\u2666':11   #Diamonds
        }   #key = card+suit, value = point value (Ace's changing point value occurs later in #### method)

deck = list(deck_dict.keys()) #list of cards+suits; allows order for random.shuffle & cards to be removed from list as they are dealt

handp1 = [] #player hand
namep1 = input("Enter your name: ")

handcpu = [] #dealer hand
namecpu = "Dealer-Bot 9000"

hitlist = ["HIT", "hit", "Hit"]
standlist = ["STAND", "stand", "Stand"]


def deck_cut(deck): #cuts deck
    deckTop = deck[:len(deck)//2] #top half of deck (from users, Jason Coon & maxymoo @ https://stackoverflow.com/questions/752308/split-list-into-smaller-lists-split-in-half)
    deckBot = deck[len(deck)//2:] #bottom half of deck
    deck = deckBot + deckTop #the successfully cut deck


def deck_shuffle(deck):
    random.shuffle(deck) #shuffles deck
    deck_cut(deck)


def print_scores(score1,score2):
        print(namep1+"'s Hand:",handp1, "Total:",score1) #displays player's hand
        print()
        print(namecpu+"'s Hand: ['#?' & ", handcpu[1:], "]") #displays dealer's hand with one hidden card
        #print(namecpu+"'s Hand (DEBUG): ",handcpu, "Total:",score2)
        print()


def calc_scores(hand): #calculates and returns score values for player and dealer
    score = 0
    for card in hand:
        cardvalue = deck_dict.get(card) #gets corresponding dictionary value using list item (card+suit) as key
        score = score + cardvalue
        if score >= 22: #check for ace values after score goes above 21
            cardlist = []
            for card in hand:
                cardvalue = deck_dict.get(card)
                score = sum(cardlist)
                if cardvalue == 11 and score >= 11: #makes sure ace won't bust player
                    cardlist.append(cardvalue-10) #reduce ace's value to 1
                else:
                    cardlist.append(cardvalue)
            score = sum(cardlist)
    return score


def cpu_hit(name,hand): #dealer hit method
    scorep1 = calc_scores(handp1)
    scorecpu = calc_scores(handcpu)
    if scorecpu <= 16 and scorep1 <= 20: #dealer will hit if score is <=16 and player hasn't busted/gotten blackjack
        if scorep1 > scorecpu: #ensures dealer doesn't bust itself if it already has a higher score than the player
            print(name,"hits")
            hit(hand,name)
            choice(handp1,namep1,handcpu,namecpu)


def check_scores(name,hand): #checks scores for bust or blackjack
    scorep1 = calc_scores(handp1)
    scorecpu = calc_scores(handcpu)
    score = calc_scores(hand)
    if score >= 22: #BUST
        print(name, "BUSTED!")
        print()
    elif score == 21: #BLACKJACK
        print(name, "got BLACKJACK!")
        print()


def hit(hand,name):
    card = deck.pop() #removes card from deck
    hand.append(card) #adds card to hand
    check_scores(name,hand)
    scorep1 = calc_scores(handp1)
    scorecpu = calc_scores(handcpu)
    print_scores(scorep1,scorecpu)
    if scorep1 <= 20 and scorecpu <= 20 and name == namep1: #dealer hits on 16 or lower after player hits and neither has busted/gotten blackjack
        if scorecpu <= 16:
            cpu_hit(namecpu,handcpu)
        choice(handp1,namep1,handcpu,namecpu)


def choice(hand,name,handcpu,namecpu): #player choice to hit or stand
    scorep1 = calc_scores(handp1)
    scorecpu = calc_scores(handcpu)
    if scorep1 <= 20 and scorecpu <= 20:
        ans = input("Would you like to (HIT) or (STAND)?: ")
        if ans in hitlist: #player hits
            hit(hand,name)
        elif ans in standlist: #player stands
            cpu_hit(namecpu,handcpu) #dealer hits if appropriate
            scorep1 = calc_scores(handp1)
            scorecpu = calc_scores(handcpu)
            if scorep1 > scorecpu: #player stands with higher score
                print(name, "WINS!")
            elif scorecpu > scorep1: #player stands with lower score
                print(namecpu, "WINS!")
            elif scorep1 == scorecpu: #push on stand in case of a tie
                print("PUSH!")
        else:
            print("Invalid Entry, Please Try Again")
            choice(hand,name,handcpu,namecpu)


def deal(deck,handp1,handcpu,namep1,namecpu): #deals initial hands
    for card in range(2): #removes two cards from deck for each player and adds them to their hands
        cardp1 = deck.pop()
        handp1.append(cardp1)
        cardcpu = deck.pop()
        handcpu.append(cardcpu)
    check_scores(namep1,handp1)
    check_scores(namecpu,handcpu)
    scorep1 = calc_scores(handp1)
    scorecpu = calc_scores(handcpu)
    print_scores(scorep1,scorecpu)
    if scorep1 <= 20 and scorecpu <= 20: #presents hit/stand choice if neither player has busted/gotten blackjack
        choice(handp1,namep1,handcpu,namecpu)


deck_shuffle(deck)
deal(deck,handp1,handcpu,namep1,namecpu)


#!!!NOTE FOR LATER!!!: Splitting may be accomplished by nested lists/2D arrays/matrices/rectangular data table within handp1/handcpu
#EX: [['10\u2666', '5\u2663'], ['J\u2663', '3\u2660']]

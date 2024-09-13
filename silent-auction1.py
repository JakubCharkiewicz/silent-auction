from art import logo, welcoming
print(logo)
print(welcoming)
bids = {}
def bidding_time():
    name = input("What's your name? ").title()
    price = int(input("What's the amount you'd like to bid for?: $"))
    bids[name] = price
bidding_time()

def highest_bidder():
    winner = max(bids, key=bids.get)
    return winner

def biggest_bid_price():
    biggest_fish = max(bids.values())
    return biggest_fish

should_continue = True
while should_continue:
    other_bidders = input("Are there any other people that want to bid?: (y/n) ")
    if other_bidders == "n":
        should_continue = False
        print("\n" *30)
        print(f"The winner of the auction is: {highest_bidder()} with the ${biggest_bid_price()} bid! " )
        print("Thank you for participating in our action! We hope to see you all soon!")

        break

    else:
       print("\n" * 20)
       bidding_time()

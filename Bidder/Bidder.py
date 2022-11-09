from art import logo
print(logo)

bids={}
bidding_finished=False

def find_highest_bidder(bids):
    highest_bid=0
    winner=""
    for bidder in bids:
        bid_amount=bids[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name=input("Enter Your name:\n")
    amount=int(input("Enter your bidding amount:\n$"))
    bids[name]=amount
    should_continue=input("Are there any other bidders ? Type 'Yes or 'no.")
    if should_continue=="no":
        bidding_finished=True
        find_highest_bidder(bids)


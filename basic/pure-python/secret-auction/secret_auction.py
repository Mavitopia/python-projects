print("Welcome to the Secret Auction! Each bidder's offer remains confidential.")

auction_bids = {}

while True:
    #get bidder name
    while True:
        bidder_name = input("Enter the bidder's name: ").strip()
        if bidder_name in auction_bids:
            print("This name has already been used. Please enter a unique name.")
        elif bidder_name == "":
            print("Name cannot be empty. Please try again.")
        else:
            break
    #get bidder's bid
    while True:
        try:
            bid_amount = float(input("Enter the bid amount in dollars: $").strip())
            if bid_amount <= 0:
                print("Invalid amount. Please enter a value greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    auction_bids[bidder_name] = {"bid": bid_amount}
    #should game go on?
    while True:
        continue_bidding = input("Would you like to add another bidder? (yes/no): ").lower()
        if continue_bidding in ["yes", "no"]:
            break
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")
            
    if continue_bidding == 'no':
        break
    
winner = ''
highest_bid = 0
tie = False

for bidder_name, bidder_info in auction_bids.items():
    if bidder_info['bid'] > highest_bid:
        highest_bid = bidder_info['bid']
        winner = bidder_name
        tie = False
    elif bidder_info['bid'] == highest_bid:
        winner += ' and ' + bidder_name
        tie = True
        
if not tie:
    print(f"The winner is {winner} with a bid of ${highest_bid:.2f}")
else:
    print(f"There is a tie {winner} with a bid of ${highest_bid:.2f}")
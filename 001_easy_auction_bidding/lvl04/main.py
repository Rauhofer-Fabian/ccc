
def retrieve_actions(input_string) -> list | dict:
    splited_string = input_string.split(",")

    initial_price = int(splited_string[0])
    buy_now_price = int(splited_string[1])

    actions = []

    for curr_index_bidder in range(2, len(splited_string), 2):
        bidder = splited_string[curr_index_bidder]
        bid = int(splited_string[curr_index_bidder + 1])

        actions.append((bidder, bid))


    initial_current = {
        "highest_bidder": None,
        "highest_bid": None,
        "price": initial_price,
        "buy_now_price": buy_now_price,
    }      

    return actions, initial_current


def excecute_actions(actions: list, current:  dict) -> str:
    builder_string = "-," + str(current["price"]) + ","
    buy_now = False

    for bidder, bid in actions:
        # print(f"{bidder} bids {bid} dollars")

        for changed_current in make_bid(bidder, bid, current.copy()):                
            if not current["highest_bidder"] == bidder:
                if current["buy_now_price"] != 0:
                    buy_now = changed_current["price"] >= changed_current["buy_now_price"] 

                builder_string += \
                str(changed_current["highest_bidder"]) \
                + "," \
                + str(changed_current["price"] if not buy_now else changed_current["buy_now_price"]) \
                + ","

                if buy_now:
                    break # buy now reached
            
            current = changed_current

    return builder_string[:len(builder_string)-1:]


def make_bid(bidder, bid_amount, current) -> any:
    current_copy = current.copy()

    if not current["highest_bidder"]:
        current["highest_bidder"] = bidder
        current["highest_bid"] = bid_amount
    
    elif bidder == current["highest_bidder"]:
        current["highest_bid"] = bid_amount

    elif bid_amount == current["highest_bid"]:
        current["price"] = current["highest_bid"]

    elif bid_amount > current["highest_bid"]:
        current["highest_bidder"] = bidder
        current["price"]  = current["highest_bid"] + 1
        current["highest_bid"] = bid_amount

    elif bid_amount >= current["price"]:
        current["price"] = bid_amount + 1

    yield current


input_strings = [
    "1,15,A,5,B,10,A,8,A,17,B,17",
    "100,0,C,100,C,115,C,119,C,121,C,144,C,154,C,157,G,158,C,171,C,179,C,194,C,206,C,214,C,227,C,229,C,231,C,298",
    "100,325,C,100,C,115,C,119,C,121,C,144,C,154,C,157,G,158,C,171,C,179,C,194,C,206,C,214,C,227,C,229,C,231,C,298",
    "100,160,C,100,C,115,C,119,C,121,C,144,C,154,C,157,G,158,C,171,C,179,C,194,C,206,C,214,C,227,C,229,C,231,C,298",
    "1,0,nepper,15,hamster,24,philipp,30,mmautne,31,hamster,49,hamster,55,thebenil,57,fliegimandi,59,ev,61,philipp,64,philipp,65,ev,74,philipp,69,philipp,71,fliegimandi,78,hamster,78,mio,95,hamster,103,macquereauxpl,135",
    "1,120,6a,17,kl,5,kl,10,kl,15,cs,28,kl,20,kl,25,hr,35,hr,40,hr,41,hl,42,hr,43,hr,44,hl,44,hl,49,hr,47",
    "1,47,6a,17,kl,5,kl,10,kl,15,cs,28,kl,20,kl,25,hr,35,hr,40,hr,41,hl,42,hr,43,hr,44,hl,44,hl,49,hr,47",
]

print("\n" * 2)

for input_string in input_strings:
    actions = retrieve_actions(input_string)
    print(excecute_actions(actions[0], actions[1]))

    print("\n" * 2)

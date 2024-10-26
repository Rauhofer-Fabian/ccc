
def retrieve_actions(input_string) -> list | dict:
    splited_string = input_string.split(",")

    initial_price = int(splited_string[0])

    actions = []

    for curr_index_bidder in range(1, len(splited_string), 2):
        bidder = splited_string[curr_index_bidder]
        bid = int(splited_string[curr_index_bidder + 1])

        actions.append((bidder, bid))


    initial_current = {
        "highest_bidder": None,
        "highest_bid": None,
        "price": initial_price,
    }      

    return actions, initial_current


def excecute_actions(actions: list, current:  dict) -> str:
    builder_string=""

    for bidder, bid in actions:
        # print(f"{bidder} bids {bid} dollars")

        for curr_highest_bidder, curr_price in make_bid(bidder, bid, current):
            continue

    return str(curr_highest_bidder) + "," + str(curr_price)


def make_bid(bidder, bid_amount, current) -> any:
    if not current["highest_bidder"]:
        current["highest_bidder"] = bidder
        current["highest_bid"] = bid_amount
        
    
    elif bid_amount > current["highest_bid"]:
        current["highest_bidder"] = bidder
        current["price"]  = current["highest_bid"] + 1
        current["highest_bid"] = bid_amount

    elif bid_amount == current["highest_bid"]:
        current["price"] = current["highest_bid"]

    elif bid_amount > current["price"]:
        current["price"] = bid_amount + 1

    yield current["highest_bidder"], current["price"]


input_strings = [
    "1,A,5,B,10,A,8,A,17,B,17",
    "1,nepper,15,hamster,24,philipp,30,mmautne,31,hamster,49,thebenil,57,fliegimandi,59,ev,61,philipp,64,ev,74,philipp,69,philipp,71,fliegimandi,78,hamster,78,mio,95,hamster,103,macquereauxpl,135",
    "1,cable,5,ente,10,karl,19,moehe,14,moehe,23,michbex,24,melloy,25,achi,26",
    "1,cable,5,ente,10,karl,19,moehe,23,michbex,24,melloy,29,achi,26",
    "15,urtyp,17,neuli,16,schlurchi,25,tokay,75,horni,35,sue,60,sue,70",
    "15,urtyp,15",
]

print("\n" * 2)

for input_string in input_strings:
    actions = retrieve_actions(input_string)
    print(excecute_actions(actions[0], actions[1]))

    print("\n" * 2)

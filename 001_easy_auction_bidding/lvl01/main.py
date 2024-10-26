
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
    builder_string = "-," + str(current["price"]) + ","

    for bidder, bid in actions:
        # print(f"{bidder} bids {bid} dollars")

        for changed_current in make_bid(bidder, bid, current.copy()):
            if not current["highest_bidder"] == bidder:
                builder_string += \
                str(changed_current["highest_bidder"]) \
                + "," \
                + str(changed_current["price"]) \
                + ","
            
            current = changed_current

    return builder_string[:len(builder_string)-1:]


def make_bid(bidder, bid_amount, current) -> any:
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

    elif bid_amount > current["price"]:
        current["price"] = bid_amount + 1

    yield current


input_strings = [
    "1,A,5,B,10,A,8,A,17,B,17",
    "100,A,100,A,115,A,119,A,144,A,145,A,157,A,158,A,171,A,179,A,194,A,206,A,207,A,227,A,229,A,231,A,234",
    "100,C,100,C,115,C,119,C,121,C,144,C,154,C,157,G,158,C,171,C,179,C,194,C,206,C,214,C,227,C,229,C,231,C,298",
    "1,nepper,15,hamster,24,philipp,30,mmautne,31,hamster,49,hamster,55,thebenil,57,fliegimandi,59,ev,61,philipp,64,philipp,65,ev,74,philipp,69,philipp,71,fliegimandi,78,hamster,78,mio,95,hamster,103,macquereauxpl,135",
    "15,urtyp,15",
    "1,rx,50,aa,2000,de,3558,einseins,3999,ek,4999,yd,8332,lb,5000,lb,6000,lb,7000,lb,8000,lb,8999,yd,9999,zn,11000,ir,11110,nr,12999,kt,12567,kt,12667,kt,13000,go,14000,ym,14999,hm,15400,nr,15690,nr,17000,td,18500,kt,18750,uy,18850,hr,18999,td,19049,st,19200",
]

print("\n" * 2)

for input_string in input_strings:
    actions = retrieve_actions(input_string)
    print(excecute_actions(actions[0], actions[1]))

    print("\n" * 2)

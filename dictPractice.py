bid_dict = {}
for i in range(3):
    name = input("what is your name?").lower()
    bid = int(input("what is your bid? $"))
    bid_dict[name] = bid

# print(max(bid_dict, key=bid_dict.get))



#to find the highest bid price
# prices = []
# for key in bid_dict:
#     prices.append(bid_dict[key])

# print(max(prices))

#to find the highest bidder
# highest = 0
# highest_bidder = ""
# for key in bid_dict:
#     if bid_dict[key] > highest:
#         highest = bid_dict[key]
#         highest_bidder = key

# print(highest_bidder,highest)

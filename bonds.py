from collections import deque
from enum import Enum

class Dir(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

def bond_strat (buy, sell):
    buy_list = []
    sell_list = []
    for buy_stats in buy:
        if buy_stats[0] > 1000:
            sell_list.append(["BOND", Dir.SELL, buy_stats[0], buy_stats[1]])
    for sell_stats in sell:
        if sell_stats[0] < 1000:
            buy_list.append(["BOND", Dir.BUY, sell_stats[0], sell_stats[1]])
    return buy_list, sell_list
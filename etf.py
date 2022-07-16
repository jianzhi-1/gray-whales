from enum import Enum

class Dir(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

def true_etf_value(bond, gs, ms, wfc):
    return 3*bond[0][0]+2*gs[0][0]+3*ms[0][0]+2*wfc[0][0]

def etf_strat(bond, gs, ms, wfc, etf):
    trade_list = []
    true_val = true_etf_value(bond, gs, ms, wfc)
    etf_val = etf[0][0]
    if true_val + 102 < etf_val*10:
        # print ("\n------------------------- ETF Trading -------------------------\n")
        trade_list.append(
            ["ADD", "BOND", Dir.BUY, bond[0][0], 3],
            ["ADD", "GS", Dir.BUY, gs[0][0], 2],
            ["ADD", "MS", Dir.BUY, ms[0][0], 3],
            ["ADD", "WFC", Dir.BUY, wfc[0][0], 2],
            ["CONVERT", "ETC", Dir.SELL, 10],
            ["SELL", "ETC", Dir.SELL, etf[0][0], 10]
        )
    elif true_val + 102 > etf_val*10:
        trade_list.append(
            ["ADD", "ETC", Dir.BUY, etf[0][0], 10],
            ["ADD", "GS", Dir.BUY, gs[0][0], 2],
            ["ADD", "MS", Dir.BUY, ms[0][0], 3],
            ["ADD", "WFC", Dir.BUY, wfc[0][0], 2],
            ["CONVERT", "ETC", Dir.SELL, 10],
            ["SELL", "ETC", Dir.SELL, etf[0][0], 10]
        )

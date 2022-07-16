from enum import Enum
from statistics import mean

class Dir(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

def adr_strategy(vale_list, valbz_list):
    ### incomplete information
    if len(vale_list) == 0 or len(valbz_list) == 0:
        return []
    
    vale_price_list = [x[0] for x in vale_list]
    valbz_price_list = [x[0] for x in valbz_list]
    if len(vale_price_list) >= 10 and len(valbz_price_list) >= 10:
        vale = vale_price_list[-10:]
        valbz = valbz_price_list[-10:]
        
        valbz_mean = mean(valbz)
        vale_mean = mean(vale)
        diff = valbz_mean - vale_mean
        if diff >= 2:
            print ("\n------------------------- ADR Trading -------------------------\n")
            return [["ADD", "VALE", Dir.BUY, vale_mean + 1, 10],
                    ["CONVERT", "VALE", Dir.SELL, 10],
                    ["ADD", "VALBZ", Dir.SELL, valbz_mean - 1, 10]]
    return []

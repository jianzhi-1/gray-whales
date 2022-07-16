from statistics import mean

class Dir(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

# Common stock & its ADR pair trading strategy
def adr_signal(cs_trade_price_list, adr_trade_price_list):
    cs_mean: int = mean(cs_trade_price_list)
    adr_mean: int = mean(adr_trade_price_list)
    fair_diff: int = cs_mean - adr_mean
    if (fair_diff >= 2):
        return [adr_mean, cs_mean]
    return []

def adr_strategy(vale_info, valbz_trade):
    # Retrieve the list of stock prices
    vale_trade_price_list = list(map(lambda x: x[0], vale_info))
    valbz_trade_price_list = list(map(lambda x: x[0], valbz_trade))
    if len(vale_trade_price_list) >= 10 and len(valbz_trade_price_list) >= 10:
        vale = vale_trade_price_list[-10:]
        valbz = valbz_trade_price_list[-10:]
        result = adr_signal(valbz, vale)
        if result:
            # print ("\n------------------------- ADR Trading -------------------------\n")
            return [{"type" : "ADD", "symbol": "VALE", "dir" : Dir.BUY, "price": result[0] + 1, "size": 10},
                    {"type" : "CONVERT", "symbol": "VALE", "dir" : Dir.SELL, "size": 10},
                    {"type" : "ADD", "symbol": "VALBZ", "dir" : Dir.SELL, "price": result[1] - 1, "size": 10}]
    return []

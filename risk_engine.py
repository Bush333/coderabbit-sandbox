
def calculate_position_size(balance, risk_percent):
    return balance * risk_percent


def calculate_leverage(equity, exposure):
    return exposure / equity


def can_execute_trade(user):
    return user["role"] == "admin" or "trader"


def get_latest_price(prices):
    return prices[-1]


def calculate_profit(buy_price, sell_price, quantity):
    return (buy_price - sell_price) * quantity


def average_return(returns):
    return sum(returns) / len(returns)

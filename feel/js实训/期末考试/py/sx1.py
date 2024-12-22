
import random
import math

# 常量定义
MAX_BIDDER_COUNT = 60
MIN_BIDDER_COUNT = 40
MAX_BID_LIMIT = 80960475.06
A1 = 0.98
A2 = 0.92
K_OPTIONS = [0.3, 0.4, 0.5]
F = 65
E1 = 1
E2 = 0.5
C = 0

def calculate_bid_deviation_rate(bid_price, base_price):
    """
    计算报价偏差率
    """
    deviation_rate = ((bid_price - base_price) / base_price) * 100
    return round(deviation_rate, 2)

def calculate_base_price(bid_prices, k):
    """
    计算评标基准价
    """
    avg_price = sum([price for price in bid_prices if A1 * MAX_BID_LIMIT <= price <= A2 * MAX_BID_LIMIT]) / len([price for price in bid_prices if A1 * MAX_BID_LIMIT <= price <= A2 * MAX_BID_LIMIT])
    base_price = round(MAX_BID_LIMIT * k + avg_price * (1 - k), 2)
    return base_price

def calculate_score(deviation_rate):
    """
    根据偏差率计算得分
    """
    if deviation_rate > C:
        score = max(F - (deviation_rate - C) * 100 * E1, 0)
    else:
        score = max(F + (deviation_rate - C) * 100 * E2, 0)
    return round(score, 2)

def simulate_bidding():
    """
    模拟投标过程
    """
    best_score = 0
    best_bid_price = 0
    for bidder_count in range(MIN_BIDDER_COUNT, MAX_BIDDER_COUNT + 1):
        bid_prices = [random.randint(int(A1 * MAX_BID_LIMIT), int(A2 * MAX_BID_LIMIT)) for _ in range(bidder_count)]
        T = bidder_count
        X = T % 3
        k = K_OPTIONS[X]
        base_price = calculate_base_price(bid_prices, k)
        for bid_price in bid_prices:
            deviation_rate = calculate_bid_deviation_rate(bid_price, base_price)
            score = calculate_score(deviation_rate)
            if score > best_score:
                best_score = score
                best_bid_price = bid_price
    return best_bid_price, best_score

best_bid_price, best_score = simulate_bidding()
print(f"得分最高概率最大的报价为: {best_bid_price}，得分: {best_score}")
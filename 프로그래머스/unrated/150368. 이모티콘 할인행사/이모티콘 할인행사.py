from itertools import product

def solution(users, emoticons):
    def proceeds(rates):
        subscribes = sales = 0
        for rate_thres, purchase_thres in users:
            purchases = 0
            for price, rate in zip(emoticons, rates):
                if rate >= rate_thres:
                    purchases += price * (1 - 0.01 * rate)
            if purchases >= purchase_thres:
                subscribes += 1
            else:
                sales += purchases
        return subscribes, sales
    
    outcomes = []
    for rates in product(range(10, 50, 10), repeat=len(emoticons)):
        outcomes.append(proceeds(rates))
    
    max_subscribes = max_sales = 0
    for subscribes, sales in outcomes:
        if subscribes > max_subscribes \
            or (subscribes == max_subscribes and sales > max_sales):
            max_subscribes, max_sales = subscribes, sales
    return max_subscribes, max_sales

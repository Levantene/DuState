import datetime
import random
from collections import Counter


# prices_dict = {}
# sizes_dict = {}


# def generate_transaction_date():
#     year = random.randint(2000, 2030)
#     month = random.randint(1, 12)
#     day = random.randint(1, 28)
#     return datetime.date(year, month, day)


# def generate_size():
#     size = random.randint(0, 500)
#     return size


# def generate_price():
#     size = random.randint(500000, 3000000)
#     return size


# def get_prices():
#     for i in range(1000):
#         prices_dict[generate_transaction_date()] = generate_price()
#     return prices_dict


# prices_dict = get_prices()
# print(min(prices_dict.keys()).year)
# print(min(prices_dict.keys()).month)
# print(max(prices_dict.keys()).year)
# print(max(prices_dict.keys()).month)

# sum((Counter({x['datestart'].month: x['sum']}) for x in summary), Counter()) 

# Counter({4: Decimal('5000000.00'), 3: Decimal('400000.00')})
# for i in prices_dict.keys():
#     print(min(i))
#     print(max(i))

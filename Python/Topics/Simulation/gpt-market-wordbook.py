#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class Agent:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        self.inventory = {}

    def buy(self, good, quantity, price):
        cost = quantity * price
        if cost <= self.balance:
            self.balance -= cost
            if good in self.inventory:
                self.inventory[good] += quantity
            else:
                self.inventory[good] = quantity
            return True
        else:
            return False

    def sell(self, good, quantity, price):
        if good in self.inventory and self.inventory[good] >= quantity:
            revenue = quantity * price
            self.balance += revenue
            self.inventory[good] -= quantity
            return True
        else:
            return False

class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def add_buy_order(self, agent, good, quantity, price):
        self.buy_orders.append({'agent': agent, 'good': good, 'quantity': quantity, 'price': price})

    def add_sell_order(self, agent, good, quantity, price):
        self.sell_orders.append({'agent': agent, 'good': good, 'quantity': quantity, 'price': price})

    def execute_trade(self):
        if self.buy_orders and self.sell_orders:
            buy_order = random.choice(self.buy_orders)
            sell_order = random.choice(self.sell_orders)

            if buy_order['price'] >= sell_order['price']:
                quantity = min(buy_order['quantity'], sell_order['quantity'])
                buyer = buy_order['agent']
                seller = sell_order['agent']

                buyer.buy(buy_order['good'], quantity, buy_order['price'])
                seller.sell(sell_order['good'], quantity, sell_order['price'])

                print(f"Trade executed: Agent {buyer.id} bought {quantity} units of {buy_order['good']} from Agent {seller.id} for ${buy_order['price']} each.")

                # Remove executed orders
                self.buy_orders.remove(buy_order)
                self.sell_orders.remove(sell_order)



if __name__ == "__main__":
    # Example usage
    num_agents = 10
    num_goods = 3

    agents = [Agent(i, balance=random.uniform(50, 100)) for i in range(num_agents)]
    goods = [f"Good_{i}" for i in range(num_goods)]

    order_book = OrderBook()

    # Simulate placing orders
    for _ in range(10):  # Adjust the number of orders as needed
        agent = random.choice(agents)
        good = random.choice(goods)
        quantity = random.randint(1, 5)
        price = random.uniform(0.5, 2.0)

        if random.choice([True, False]):  # 50% chance of placing a buy or sell order
            order_book.add_buy_order(agent, good, quantity, price)
            print(f"Buy order placed: Agent {agent.id} wants to buy {quantity} units of {good} for ${price} each.")
        else:
            order_book.add_sell_order(agent, good, quantity, price)
            print(f"Sell order placed: Agent {agent.id} wants to sell {quantity} units of {good} for ${price} each.")

    # Simulate order execution
    print("Beginning market simulation...")
    random.seed(1234)
    order_book.execute_trade()
    print("Market simulation finished!")


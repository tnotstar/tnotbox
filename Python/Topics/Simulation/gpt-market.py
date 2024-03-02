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

class Market:
    def __init__(self, agents, goods):
        self.agents = agents
        self.goods = goods

    def random_transaction(self):
        buyer = random.choice(self.agents)
        seller = random.choice(self.agents)
        good = random.choice(self.goods)
        price = random.uniform(0.5, 2.0)  # Adjust price range as needed

        if buyer != seller:
            quantity = random.randint(1, 5)  # Adjust quantity range as needed
            success = buyer.buy(good, quantity, price) and seller.sell(good, quantity, price)
            if success:
                print(f"Transaction: Agent {buyer.id} bought {quantity} units of {good} from Agent {seller.id} for ${price} each.")


if __name__ == "__main__":
    # Example usage
    num_agents = 10
    num_goods = 3

    agents = [Agent(i, balance=random.uniform(50, 100)) for i in range(num_agents)]
    goods = [f"Good_{i}" for i in range(num_goods)]

    market = Market(agents, goods)

    # Simulate transactions
    print("Beginning market simulation...")
    random.seed(1234)
    for _ in range(20):  # Adjust the number of transactions as needed
        market.random_transaction()
    print("Market simulation finished!")


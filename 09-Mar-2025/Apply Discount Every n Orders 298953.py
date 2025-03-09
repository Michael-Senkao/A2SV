# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.product_prices = {products[i]:prices[i] for i in range(len(products))}
        self.discount = (100 - discount) / 100
        self.has_bought = 0
        self.n = n

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        for product,amount in zip(product,amount):
            total += self.product_prices[product] * amount
        self.has_bought = (self.has_bought + 1) % self.n
        
        if self.has_bought == 0:
            return self.discount * total
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discounted_price = (100 - discount) / 100
        self.customers = 0
        self.price = {products[i]: prices[i] for i in range(len(products))}
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        
        self.customers = (self.customers + 1) % self.n
        bill = 0
        for i in range(len(product)):
            itemID,count = product[i],amount[i]
            bill += self.price[itemID]*count

        if self.customers == 0:
            bill *= self.discounted_price # Apply discount
        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
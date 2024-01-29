# ShoppingCart
# It involves the Implementation of Shopping Cart using OOP's concept. 

class product:
    def __init__(self, name, price, deal_price, rating):
        self.name = name
        self.price = price 
        self.deal_price=deal_price 
        self.rating = rating 
        self.you_saved = price-deal_price 
    def display_items(self):
        print("Name : {}".format(self.name)) 
        print("Price : {}/-".format(self.price)) 
        print("Deal price : {}/-".format(self.deal_price)) 
        print("Rating : {}/5".format(self.rating)) 
        print("saved amount : {}/-".format(self.you_saved)) 
class electronics(product):
    def __init__(self,name, price, deal_price, rating, warrenty):
        super().__init__(name, price, deal_price, rating)
        self.warrenty=warrenty 
    def display_items(self):
        super().display_items()
        print("warrenty : {} months".format(self.warrenty)) 
class grocery(product):
    def __init__(self,name, price, deal_price, rating, expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.expiry_date=expiry_date 
    def display_items(self):
        super().display_items()
        print("Expiry date : jan {}".format(self.expiry_date)) 
class Order:
    def __init__(self,delivery_method,delivery_address):
        self.items=[] 
        self.delivery_method=delivery_method 
        self.delivery_address=delivery_address 
    def add_items(self,product,quantity):
        self.items.append((product,quantity)) 
    def display_order_items(self):
        print("Delivery Method : {}".format(self.delivery_method))
        print("Delivery Address : {}".format(self.delivery_address)) 
        print('Products')
        print("----------------------------------------")
        for product,quantity in self.items:
            product.display_items()
            print("quantity : {}".format(quantity)) 
            print("") 
        print("------------------------------------------")
        self.bill()
        print("------------------------------------------")
    def bill(self):
        bill =0 
        for product,quantity in self.items:
            bill += product.deal_price*quantity 
        print("Total bill : {}/-".format(bill))
milk = grocery("Milk",25,20,4,30) 
tv = electronics("TV",65000,60000,4.5,24)  
laptop = electronics("Laptop",50000,42000,4.4,12)
order = Order("Prime Delivery", "Jublie hills, Hyderabad") 
order.add_items(milk,3)
order.add_items(tv,1)
order.add_items(laptop,1)
order.display_order_items()

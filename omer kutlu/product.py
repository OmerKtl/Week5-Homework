"""
Define a class named Product with the following specifications:
Data members:
product_id – A string to store product.
product_name - A string to store the name of the product.
product_purchase_price – A decimal to store the cost price of the product.
product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods :
A constructor to intialize all the data members with valid default values.
A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
![h51](https://user-images.githubusercontent.com/98665012/155852165-694f473b-c1b2-4f35-8cac-74e1db4e6d86.png)
A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
A method get_details() that displays all the data members.
"""
from typing_extensions import Self
class Product():
    id=[]
    name=[]
    purcase=[]
    sale=[]
    margin=[]
    prof=[]
    def __init__(self,product_id,product_name,product_purcase_price,product_sale_price):
        self.product_id=product_id
        self.product_name=product_name
        self.product_purcase_price=product_purcase_price
        self.product_sale_price=product_sale_price
        self.margin=Product.set_remarks(self)
        self.ifmargin=Product.result(self)
        Product.id.append([self.product_id])
        Product.name.append([self.product_name])
        Product.purcase.append([self.product_purcase_price])
        Product.sale.append([self.product_sale_price])
        Product.margin.append([self.margin])
        Product.prof.append([self.ifmargin])
    def set_remarks(self):
        return int(self.product_sale_price)-(int(self.product_purcase_price))
    def result(self):
        p="Profit"
        l="Loss"
        n="No Profit-No Loss"
        if self.margin>0:
            return p
        elif self.margin<0:
            return l
        return n
    def get_details(self):        
        for i in range(times):            
            print(int(i+1),"-","ID:",*Product.id[i],"NAME:",*Product.name[i],"PURCASE P.:",*Product.purcase[i],
            "SALE P.:",*Product.sale[i],"MARGIN RATE:",*Product.margin[i],"RESULT:",*Product.prof[i])

    def print(self):
        print("\nProduct ID    :",self.product_id,
              "\nProduct Name  :",self.product_name,
              "\nPurcase Price :",self.product_purcase_price,
              "\nSale Price    :",self.product_sale_price,
              "\nMargin Rate   :",self.margin,
              "\nProfit or Loss:",self.ifmargin,"\n")
        
times=int(input("Enter The Quantity of Product:"))

def set_details():
    return Product(input("Product ID:"),input("Enter Product Name:"),input("Enter Purcase Price:"),input("Enter Sale Price:"))
while True:
    for i in range(times):
        set_details().print()
    break

Product.get_details(Self)
        
    
        

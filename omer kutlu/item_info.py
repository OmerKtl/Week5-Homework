"""
Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item), net_price(Price after discount)
Methods :
A member method calculate_discount() to calculate discount as per the following rules:
If qty <= 10 —> discount is 0
If qty (11 to 20 inclusive) —> discount is 15
If qty >= 20 —> discount is 20
A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
A function show_all() or similar name to allow user to view the content of all the data members.+
"""

class ItemInfo():
 
    def __init__(self,item,item_code=0,price=0,qty=0):
        self.item=item
        self.item_code=item_code
        self.price=price
        self.qty=qty
        self.discount=int(ItemInfo.calculate_discount(self))
        self.net_price=(int(self.price)*int(self.qty))-((int(self.price)*int(self.qty))*(self.discount/100))
      

    def calculate_discount(self):
        if int(self.qty)<=10:
            return 0
        elif 10<int(self.qty)<=20:
            return 15
        elif int(self.qty)>20:
            return 20
    def print(self):
        print("\nItem Name :",self.item,"\nItem Code :",self.item_code,"\nPrice :",self.price,"$","\nQuantity :",self.qty,
        "\nDiscount :","%",self.discount,"\nNet Price :",self.net_price,"$\n")
    def show_all(self):
        pass

times=int(input("Enter How Many Different Type of item you select:"))
def input_data():
    return ItemInfo(input("Enter Item Name:"),input("Enter Item Code:"),input("Enter Price:"),input("Enter Quantity:"))
while True:
    for i in range(times):
        input_data().print()
    break









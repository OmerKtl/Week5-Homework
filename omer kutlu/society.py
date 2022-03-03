"""
Question 1:
Create the class Society with following information:
society_name,house_no_of_mem, flat, income

Methods :
An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
input_data() To read information from members
allocate_flat() To allocate flat according to income using the below table.
show_data() to display the details of the entire class.
"""

class Society:
    society_name="Bizimkiler"

    def __init__(self,name,house_no_of_mem,income):
        self.name=name
        self.house_no_of_mem=house_no_of_mem
        self.income=income
        self.flat=Society.allocate_flat(self)
      
    def allocate_flat(self):
        if self.income>=25000:
            return "A Type"
        elif 20000<=self.income<25000:
            return "B Type"
        elif 15000<=self.income<20000:
            return "C Type"
        elif self.income<15000:
            return "D Type" 

    def show_data(self):
        print("\nSociety Name:",Society.society_name,"\nMember Name:",self.name,"\nHouse No:",self.house_no_of_mem,
        "\nIncome:",self.income,"\nFlat Type:",self.flat,"\n")

quantity_of_member=int(input("Please Enter The Quantity of Members :"))        
def input_data():
    return Society(input("Enter Name:"),input("Enter House Number of Member:"),int(input("Enter Income :")))
while True:
    for i in range(quantity_of_member):
        input_data().show_data()
    break
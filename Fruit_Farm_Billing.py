#!/usr/bin/env python
# coding: utf-8

# In[5]:


class FruitInfo:
    __fruit_name_list = ['Apple','Guava','Orange','Grape','Sweet Lime']
    __fruit_price_list = [200,80,70,110,60]
    
    @staticmethod
    def get_fruit_price(fruit):
        for index in range(0,len(FruitInfo.__fruit_name_list)):
            if(fruit.lower() == FruitInfo.__fruit_name_list[index].lower()):
                return FruitInfo.__fruit_price_list[index]
        return -1
    
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
    


# In[6]:


class Customer:
    def __init__(self,customer_name,cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type
        
    def get_customer_name(self):
        return self.__customer_name
    
    def get_cust_type(self):
        return self.__cust_type


# In[7]:


class Purchase:
    __counter = 101
    def __init__(self,customer,fruit_name,quantity):
        self.__purchase_id = None
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
        self.price_amount = None
        self.final_amount = None
        
    def get_purchase_id(self):
        self.__purchase_id = "P"+str(Purchase.__counter)
        Purchase.__counter+=1
        return self.__purchase_id
    
    def get_customer():
        return self.__customer
    
    def get_quantity(self):
        return self.quantity

    def calculate_price(self):
        flag1 = flag2 = 0
        fruit_price = FruitInfo.get_fruit_price(self.__fruit_name)
        if(fruit_price != -1):
            self.price_amount = self.__quantity * fruit_price
            if(fruit_price == max(FruitInfo.get_fruit_price_list()) and self.__quantity > 1):
                flag1 = 1
                discount_amount=self.price_amount - (self.price_amount * 2/100)
            elif(fruit_price == min(FruitInfo.get_fruit_price_list()) and self.__quantity >= 5):
                flag2 = 1
                discount_amount=self.price_amount-(self.price_amount * 5/100)
                
            if((self.__customer.get_cust_type().lower() == "wholesale") and (flag1==1 or flag2==1)):
                self.final_amount = discount_amount - (discount_amount * 10/100)
            else:
                self.final_amount = self.price_amount-(self.price_amount * 5/100)
            if(self.__customer.get_cust_type().lower() != "wholesale"):
                self.final_amount = self.price_amount
        else:
            self.final_amount = "Fruit Not Found in Catalogue"
        
    def display_details(self):
        print("     ---------------Coorg Fruit Farm--------------------------","\n")
        print("      Customer Details..","\n")
        print("      Customer Name               :",self.__customer.get_customer_name())
        print("      Type of Customer            :",self.__customer.get_cust_type())
        print("      -------------------------------------------------------")
        print("      Purchase Details..","\n")
        print("      Purchase ID                 :",self.__purchase_id)
        print("      Fruit Purchased             :",self.__fruit_name)
        print("      Quantity Purchased          :",self.__quantity)
        if (self.final_amount != "Fruit Not Found in Catalogue"):
            print("      Price Amount (Rs.)          :",self.price_amount)
            print("      Discount Amount (Rs.)       :",self.final_amount)
            print("      -------------------------------------------------------")
            print("\n","------------------Have a nice day---------------------------")
        else:
            print("\n","            Error : Fruit not found in Catalogue")
            print("      -------------------------------------------------------")
            print("\n","------------------Have a nice day---------------------------")
            


# In[9]:


customer1 = Customer("Vibisha","Wholesale")
Fruit1 = Purchase(customer1,"Apple",6)
print("Purchase_ID",Fruit1.get_purchase_id())
print("Price",Fruit1.calculate_price())
Fruit1.display_details()

customer2 = Customer("HemaLatha","Wholesale")
Fruit2 = Purchase(customer2,"Apple",6)
print("Purchase_ID",Fruit2.get_purchase_id())
print("Price",Fruit2.calculate_price())
Fruit2.display_details()


# In[ ]:





class item():
  
  def __init__(self, item_name, price):
    self.item_name = item_name
    self.price = price
    
  def new_item_message(self):
    print("New item created: {}\nIt costs: ${}".format(self.item_name, self.price))
    
  def item_name(self, new_item_name):
    self.item_name = new_item_name
  
  def price(self, new_price):
    self.price = new_price

class customer(item):
  
  def __init__(self, customer_id, phone_number, item_name, price):
    self.customer_id = customer_id
    self.phone_number = phone_number
    item.__init__(self, item_name, price)
    
  def new_customer_message(self):
    
    print("Confirm phone number: {}".format(self.phone_number))
    customer_choice = input("Is this the correct phone number? Yes or No")
    if customer_choice == 'yes' or 'Yes':
      print("Your ID is: {}\nThank you for confirming your phone number: {} \nHave a great day!".format(self.customer_id,self.phone_number))
    else:
      print("none")
    
  def purchase(self):
    order_input = input("Please enter what you would like to purchase?")
    if order_input == self.item_name:
      print("Your total is ${}".format(self.price))
    else:
      print("Item is currently out of stock.")
    
  
new_item = item("blueberry", 4.00)
new_item.new_item_message()

customer_new = customer(5, 1234567890, "blueberry", 4.00)
customer_new.new_customer_message()


customer_new.purchase()


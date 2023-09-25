class shopcart:
    def __init__(self):
        self.items=[]
    def new_item(self,name,qty):
        item=(name,qty)
        self.items.append(item)
    def delete_item(self,name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                break
    def total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
    def print_cart(self):
        for item in self.items:
            print(item[0],"-",item[1])
cart = shopcart()
cart.new_item("Car",150)
cart.new_item("Doll",200)
cart.new_item("Chain",180)
cart.print_cart()
print("----------------")
cart.delete_item("Doll")
cart.print_cart()
print("----------------")
sum = cart.total()
print("Total quantity",sum)
class Store:

    def __init__(self, name, product, new_product, id, percent_increase, category, percent_discount):
        self.name = name
        self.product = product
        self.new_product = new_product 
        self.id = id
        self.category = category 
        self.percent_discount = percent_discount
        self.percent_increase = percent_increase 


    def Add_product(self):
        #I want to add a new product to the store 
        self.new_product
        self.id.count+=1
        return self

    def sell_product(self):
        self.product.count-=1
        return self

    def inflation(self):
        pass

    def set_clearance(self):
        pass

p1 = Store("Burger Palace", "none", "Hamburgers", 1, .03, "Burgers", 0 )
print("New Product Added:", p1.new_product)

print(p1.id)

class Product:

    def __init__(self, name, price, category, percent_change, is_increased):
        self.name = name
        self.price = price
        self.category = category 
        self.percent_change = percent_change
        self.is_increased = is_increased

    def update_price(self):
        if self.update_price:
            self.update_price = self.update_price*.08
            return True
        else:
            self.update_price = self.update_price/.08
            return False

    def price_info(self):
        pass

p1 = Product()


class Store(Product):
    def __init__(self, name, productList =[]):
        super().__init__(name, price ,category)
        self.name = name
        self.productList=productList
    def add_product(self, new_product) :
        self.productList.append(new_product)
        print(self.productList)
    def sell_product(self, id):
        self.productList.remove(self.productList[id])
        print(self.productList)
    

        

class Product:
    def __init__(self, name, price ,category ):
        self.name = name
        self.price=price
        self.category=category
    def update_price(self, percent_change, is_increased):
        if is_increased==True:
            self.price+=self.price*percent_change
        elif is_increased==False:
            self.price-=self.price*percent_change
        print(self.price)
    def print_info(self):
        print(f'product name :{self.name} product catecory: {self.category} price : {self.price}')
        
product1=Product("gg",150,"dd")
product1.update_price( 0.2, True)
product1.print_info()
store1=Store("aa",[])
store1.add_product("ff")
store1.sell_product(0)


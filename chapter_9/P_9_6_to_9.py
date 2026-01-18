class Restaurant:
    """餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化类"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述餐馆基本信息"""
        print(f"{self.restaurant_name} is {self.cuisine_type} style")

    def open_restaurant(self):
        """表示正在营业"""
        print(f"{self.restaurant_name} is open")

    def all_print(self):
        self.describe_restaurant()
        self.open_restaurant()

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavour = []

    def append_flavour(self, flavour):
        self.flavour.append(flavour)

    def print_flavour(self):
        for flavour in self.flavour:
            print(flavour)
        self.all_print()
old_people_chicken = Restaurant("Chicken", "north")
#创建实例
old_people_chicken.all_print()
#使用方法
print('\n')

a_ice_cream = IceCreamStand("ice cream", "ice")
a_ice_cream.append_flavour('fruit')
a_ice_cream.append_flavour('strew')
a_ice_cream.print_flavour()
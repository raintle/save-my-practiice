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

class User:
    """user的类"""
    def __init__(self, first_name, last_name, age, email):
        """初始化user信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def greet_user(self):
        """向user打招呼"""
        print(f"hello! {self.first_name} {self.last_name}.")

    def describe_user(self):
        """描述user"""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")
        print('ur email is', self.email)

class Admin(User):

    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = ['cam ban user', 'can delete post']

    def show_privileges(self):
        print(f'about u privileges:{', '.join(self.privileges)}')



if __name__ == '__main__':
    old_people_chicken = Restaurant("Chicken", "north")
    # 创建实例
    old_people_chicken.all_print()
    # 使用方法
    print('\n')

    a_ice_cream = IceCreamStand("ice cream", "ice")
    a_ice_cream.append_flavour('fruit')
    a_ice_cream.append_flavour('strew')
    a_ice_cream.print_flavour()
    print('\n')

    admin1 = Admin('adw', 'dwa', 12, '<EMAIL>')
    admin1.greet_user()
    admin1.show_privileges()

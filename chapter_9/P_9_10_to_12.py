from P_9_6_to_9 import Restaurant, Admin
#导入类

if __name__ == '__main__':
    #运行实例

    old_people_chicken = Restaurant("Chicken", "north")
    # 创建实例
    old_people_chicken.all_print()
    # 使用方法
    print('\n')

    admin1 = Admin('adw', 'dwa', 12, '<EMAIL>')
    admin1.privileges.show_privileges()
    admin1.greet_user()

"""
9-12省略
"""

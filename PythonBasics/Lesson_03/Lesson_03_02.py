def my_func(**kwargs):
    print(kwargs)


name = input("Enter name ")
second_name = input("Enter second_name ")
year = input("Enter year ")
city = input("Enter city ")
email = input("Enter email ")
telephone = input("Enter telephone ")

my_func(name=name, second_name=second_name, year=year, city=city, email=email, telephone=telephone)

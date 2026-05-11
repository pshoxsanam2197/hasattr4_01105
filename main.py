# 1-m
class Person:
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age

    def show_info(self):
        print(f"Ism: {self.fullname}")
        print(f"Yosh: {self.age}")


class Simple:
    def test(self):
        print("Oddiy method")

class Profile:
    def check_profile(self, obj):
        if hasattr(obj, "show_info"):
            obj.show_info()
        else:
            print("show_info method topilmadi")

p1 = Person("Azamat", 21)
s1 = Simple()

profile = Profile()

profile.check_profile(p1)
print("----------")
profile.check_profile(s1)

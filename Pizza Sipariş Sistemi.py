import csv
import datetime



with open("Menu.txt", "w") as dosya:
    dosya.write("PİZZA ÇEŞİTLERİ:\n")
    dosya.write("1: Klasik Pizza\n")
    dosya.write("2: Margarita Pizza\n")
    dosya.write("3: Türk Pizza\n")
    dosya.write("4: Sade Pizza\n\n")
    
    dosya.write("SOS ÇEŞİTLERİ:\n")
    dosya.write("11: Zeytin Sosu\n")
    dosya.write("12: Mantar Sosu\n")
    dosya.write("13: Keçi Peyniri Sosu\n")
    dosya.write("14: Et Sosu\n")
    dosya.write("15: Soğan Sosu\n")
    dosya.write("16: Mısır Sosu")



class Pizza:
    def __init__(self):
        self.description = "Bilgi yok"
        self.cost = 0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Klasik(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza"
        self.cost = 95.00

class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.cost = 90.00
        
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Türk Pizza"
        self.cost = 100.00
        
class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Sade Pizza"
        self.cost = 85.00
        

class Decorator(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description() + " + " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin Sosu"
        self.cost = 29.00

class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar Sosu"
        self.cost = 25.00

class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi Peyniri Sosu"
        self.cost = 31.00

class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et Sosu"
        self.cost = 35.00

class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Soğan Sosu"
        self.cost = 22.00

class Mısır(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mısır Sosu"
        self.cost = 27.00

def main():
    
    menu_file = open("Menu.txt", "r")
    print(menu_file.read())
    menu_file.close()
    
    
    # Pizza seçimi yap
    pizza_choice = input("\nLütfen Önce Pizza Seçiniz.. (1-4): ")
    if pizza_choice == "1":
        pizza = Klasik()
    elif pizza_choice == "2":
        pizza = Margherita()
    elif pizza_choice == "3":
        pizza = TurkPizza()
    elif pizza_choice == "4":
        pizza = SadePizza()
    
    else:
        print("Geçersiz seçim!")
        return

    # Sos seçimi yap

    sos_choice = input("Sos Tercihinizi Yapınız.. (11-16): ")
    if sos_choice == "11":
        pizza = Zeytin(pizza)
    elif sos_choice == "12":
        pizza = Mantar(pizza)
    elif sos_choice == "13":
        pizza = KeciPeyniri(pizza)
    elif sos_choice == "14":
        pizza = Et(pizza)
    elif sos_choice == "15":
        pizza = Sogan(pizza)
    elif sos_choice == "16":
        pizza = Mısır(pizza)
    
    else:
        print("Geçersiz seçim!")
        return

    # Toplam fiyatı göster
    print("Seçiminiz: " + pizza.get_description())
    print("Toplam Fiyat: ₺" + str(pizza.get_cost()))

    # Sipariş bilgileri al
    name = input("İsim: ")
    tc_no = input("TC Kimlik No: ")
    credit_card_no = input("Kredi Kartı No: ")
    credit_card_pin = input("Kredi Kartı Şifresi: ")

    # Siparişi veritabanına kaydet
    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pizza.get_description(), name, tc_no, credit_card_no, datetime.datetime.now(), credit_card_pin])

if __name__ == "__main__":
    main()

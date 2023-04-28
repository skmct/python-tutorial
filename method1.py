class car:
    name=''
    ex_room_price=0
    third_party_price=0
    taxes=0
    def on_road_price(self):
        on_road=self.ex_room_price+self.third_party_price+self.taxes
        return on_road
car1=car()
car1.name="bmw"
# car1.ex_room_price=200000
# car1.third_party_price=250000
# car1.taxes=10000
print(f'car 1 name:{car1.name}')
print("car1 price",car1.on_road_price())

car2=car()
car2.name="bmw"
car2.ex_room_price=200000
car2.third_party_price=250000
car2.taxes=10000
print(f'car 2 name:{car1.name}')
print("car2 price",car1.on_road_price())

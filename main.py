class House:
    def __init__(self,name,number_of_floors):
        self.name=name
        self.number_of_floor = number_of_floors
    def go_to(self,new_floor):
        floor=0
        if new_floor > self.number_of_floor:
            print("такого этажа нет")
        else:
            for i in range(new_floor):

                floor = floor + 1
                print(floor)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
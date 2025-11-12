from tty import ISPEED


class bus:
    def drive(self):
        self.speed = 10

mybus = bus()
mybus.color = "yellow"
mybus.model = "E-Class"
mybus.speed = 0
mybus.year = "2025"

mybus.drive()
print("차 객체를 생성하였습니다.")
print("차 속도는", mybus.speed)
print("차 색상은", mybus.color)

class Human:
    def __init__(self,name):
        self.name = name

    def test(self):
        print("냐는", self.name)

lee =  Human("이순신")
kim = Human("이성계")

lee.test()
kim.test()
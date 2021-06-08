class Human:
    def __init__(self, n, o): #self - It represents the instance of the cass.By using this keyword we can access the attributes and methods of the class.It binds the attributes with given arguments.The reason to use this in python that Python doesnt use @ syntax to refer to instance attributes
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "Tennis Player":
            print(self.name, "plays tennis")

        elif self.occupation == "Actor":
            print(self.name, "Shoots")

        elif self.occupation == "Cook":
            print(self.name, "cooks")

    def speaks(self):
        print(self.name, "says how are you?")


tom = Human("tom cruise","Actor")
tom.do_work()
tom.speaks()

sid = Human("Sid ", "Cook")
sid.do_work()
sid.speaks()

maria = Human("Maria Sharapova", "Tennis Player")
maria.do_work()
maria.speaks()


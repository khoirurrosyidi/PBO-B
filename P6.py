class Human:
    def sayHello(self,name=None):
        if name is not None:
            print('Hello Guys ' + name)

        else:
            print('Hello Bro')
obj = Human()
obj.sayHello()
obj.sayHello('Irul')

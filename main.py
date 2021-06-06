class CodeHandler(object):
    def handle(self,code):
        raise NotImplementedError()

class Code404Handler(CodeHandler):
    def handle(self, code):
        if code == 404:
            return 'Order isn\'t found'

class Subject(object):
    _handlers = []

    def add_handlers(self, h):
        self._handlers.append(h)
    
    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print('Response: %s' % msg)
                break
            else:
                print('Code isn\'t procced')

class Administrator(Subject):
    def __init__(self,orders):
        self.count = 0
        self.orders = orders

    def enter(self):
        print("\nLogin: ")
        login = input()
        print("\nPassword: ")
        password = input()
        self.data = login + " " + password
        return self

    def exit(self):
        self = None

    def OrderDetails(self):
        print("\nOrder id: ")
        id = int(input())
        if(id + 1 > len(self.orders)):
            self.response(404)
            while(id + 1 > len(self.orders)):
                print("\nOrder id: ")
                id = int(input())
        print("\nProduct name: ")
        name = input()
        print("\nPrice: ")
        price = float(input())
        print("\nAmount: ")
        amount = float(input())
        print("\nOrdered ")
        print(name)
        print(" ")
        fprice = price*amount
        print(str(fprice))
        self.orders[id].AddPrice(fprice)
        self.orders[id].AddChangeLog("Ordered " + str(amount) + " " + name)
        self.orders[id].CountPrice(id)

    def AddWorkerToOrder(self):
        print("\nOrder id: ")
        id = int(input())
        if(id + 1 > len(self.orders)):
            self.response(404)
            while(id + 1 > len(self.orders)):
                print("\nOrder id: ")
                id = int(input())
        print("\nWorker full name: ")
        name = input()
        mes = str(name) + " has been added to order #" + str(id)
        print("\n" + mes)
        self.orders[id].AddChangeLog(mes + "\n")

class Order():
    def __init__ (self):
        self.price = 0
        self.changeList = ""

    def CountPrice(self,id):
        print("\nOrder #" + str(id))
        print(self.changeList)
        print("\nPrice: "+ str(self.price))

    def AddPrice(self, price_):
        self.price += price_

    def AddChangeLog(self, log):
        self.changeList += log


def main():
    orders = [Order()]
    admin = Administrator(orders).enter()
    admin.add_handlers(Code404Handler())
    admin.AddWorkerToOrder()
    admin.OrderDetails()
    admin.exit()
    

if __name__ == "__main__":
    main()
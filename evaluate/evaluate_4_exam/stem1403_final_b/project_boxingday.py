"""
Project: The Boxing Day
"""


class TaxRate:
    GST = 0.05
    QST = 0.09975


class Status:
    SHIPPING_SHIPPED = 'shipped'
    SHIPPING_READY = 'ready to ship'
    SHIPPING_NOT_READY = 'not ready'
    ORDER_PAID = 'paid'
    ORDER_UNPAID = 'unpaid'
    ORDER_CANCELED = 'canceled'


class OrderSystem:
    LAST_ORDER_NO = 202112260000

    @staticmethod
    def getNextOrderNo():
        OrderSystem.LAST_ORDER_NO += 1
        return OrderSystem.LAST_ORDER_NO


class Address:
    def __init__(self, streetno, streetname, suitno, postalcode, city='Montreal', province='Quebec', country='Canada'):
        self.streetno = streetno
        self.streetname = streetname
        self.suitno = suitno
        self.city = city
        self.province = province
        self.country = country
        self.postalcode = postalcode

    def getAddress(self):
        return str(self.suitno)+"-"+self.streetno+" "+self.streetname+"  "\
               +self.city+", "+self.province+" "+self.country+" "+self.postalcode

class Order:
    def __init__(self):
        self.merchant = 'ABC.ca'
        self.orderno = '0000-0000-0000'
        self.orderdate = 'mm-dd-yyyy'
        self.ordertime = '00:00:00'
        self.customer = None
        self.billaddr = None
        self.receiver = None
        self.shippingaddr = None
        self.subtotal = 0
        # self.discount = 0
        self.freight = 0
        self.tax_gst = 0
        self.tax_qst = 0
        self.tax_total = 0
        self.grandtotal = 0
        self.orderstatus = Status.ORDER_UNPAID
        self.shippingstatus = Status.SHIPPING_NOT_READY
        self.paymentmethod = 'unknown'
        self.itemlist = []

    def addToCart(self,orderItem):
        self.itemlist.append(orderItem)
        print(f"INFO: Order Item-{orderItem.getItemNo()} has been added.")

    def placeOrder(self, customer, billAddr, receiver=None, shippingAddr=None):
        self.orderno = OrderSystem.getNextOrderNo()
        self.orderdate = '12-26-2021'
        self.ordertime = '20:00:00'
        self.customer = customer
        self.billaddr = billAddr
        if receiver is None:
            self.receiver = self.customer
        else:
            self.receiver = receiver
        if shippingAddr is None:
            self.shippingaddr = 'The same as bill-to address'
        else:
            self.shippingaddr = shippingAddr
        self.orderstatus = Status.ORDER_UNPAID
        self.subtotal = self.getSubTotal()
        self.tax_gst = self.getTaxGst()
        self.tax_qst = self.getTaxQst()
        self.tax_total = self.getTax()
        self.freight = self.getFreight()
        self.grandtotal = self.getGrandTotal()
        print(f"INFO: Order-{self.orderno} has been placed.")

    def checkout(self):
        self.orderstatus = Status.ORDER_PAID
        print(f"INFO: Order-{self.orderno} has been paid.")

    def cancelOrder(self):
        if self.shippingstatus != Status.SHIPPING_SHIPPED:
            self.orderstatus = Status.ORDER_CANCELED
            print(f"INFO: Order-{self.orderno} has been canceled.")
        else:
            print(f"INFO: Order-{self.orderno} cannot be canceled.")

    def packaging(self):
        self.shippingstatus = Status.SHIPPING_READY
        print(f"INFO: Order-{self.orderno} is ready to ship.")

    def ship(self):
        current_shippingstatus = self.shippingstatus.lower()
        if current_shippingstatus == Status.SHIPPING_READY:
            self.shippingstatus = Status.SHIPPING_SHIPPED
            print(f"INFO: Order-{self.orderno} was just shipped.")
        elif current_shippingstatus == Status.SHIPPING_NOT_READY:
            print(f"INFO: Order-{self.orderno} cannot been shipped due to it is not ready.")
        elif current_shippingstatus == Status.SHIPPING_SHIPPED:
            print(f"INFO: Order-{self.orderno} has been shipped.")

    def printOrderInfo(self):
        title = '=======================\n'
        title += f'{self.merchant}   ORDER\n'
        title += '=======================\n'
        content = f'Order no.:\t{self.orderno}\n'
        content += f'Order date:\t{self.orderdate}\n'
        content += f'Order time:\t{self.ordertime}\n'
        content += f'Bill To: \t{self.customer}\n'
        content += f'         \t{self.billaddr}\n'
        content += f'Ship to: \t{self.receiver}\n'
        content += f'         \t{self.shippingaddr}\n'
        detail = '-----------------------\n'
        for item in self.itemlist:
            detail += item.getItemInfo()+'\n'
        summary = '-----------------------\n'
        summary += f'Subtotal:\t{self.subtotal:>10.2f}$\n'
        summary += f'Freight:\t{self.freight:>10.2f}$\n'
        summary += f'GST @{TaxRate.GST:.3%}:{self.tax_gst:>10.2f}$\n'
        summary += f'QST @{TaxRate.QST:.3%}:{self.tax_qst:>10.2f}$\n'
        summary += f'Tax:\t\t{self.tax_total:>10.2f}$\n'
        summary += f'Grand Total:{self.grandtotal:>10.2f}$\n'
        status = '-----------------------\n'
        status += self.getStatus().upper() + '\n'
        status += '-----------------------\n'
        return title+content+detail+summary+status

    def getOrderStatus(self):
        return self.orderstatus

    def getShippingStatus(self):
        return self.shippingstatus

    def getGrandTotal(self):
        return self.getSubTotal()+self.getFreight()+self.getTax()

    def getSubTotal(self):
        subtotal = 0
        for item in self.itemlist:
            subtotal += item.getItemAmount()
        return subtotal

    def getFreight(self):
        f = 25.0
        if self.getSubTotal() >= 50:
            f = 0
        return f

    def getTax(self):
        tax = self.getTaxGst() + self.getTaxQst()
        return tax

    def getTaxGst(self):
        return self.getSubTotal() * TaxRate.GST

    def getTaxQst(self):
        return self.getSubTotal() * TaxRate.QST

    def getStatus(self):
        if self.orderstatus.lower() not in (Status.ORDER_CANCELED, Status.ORDER_UNPAID):
            status = self.orderstatus+', '+self.shippingstatus
        else:
            status = self.orderstatus
        return status


class OrderItem:
    def __init__(self, seqno, itemno, itemname, itemdesc, unitprice, qty):
        self.seqno = seqno
        self.itemno = itemno
        self.itemname = itemname
        self.itemdesc = itemdesc
        self.unitprice = unitprice
        self.qty = qty

    def getItemAmount(self):
        return self.unitprice * self.qty

    def getItemInfo(self):
        return f'{self.seqno:2} {self.itemno} {self.itemname:15} {self.itemdesc:25} {self.unitprice:>8.2f} {self.qty:2} {self.getItemAmount():>8.2f}'

    def getItemNo(self):
        return self.itemno


# test main
# addresses
# 9-1000 Boul. Decarie Montreal Quebec  H2A 1K3
addrPeter = Address('1000','Boul. Decarie','9','H2A 1K3')
# 3-1500 Boul. Sherbrooke Est. Quebec City, Quebec  K1B 2H6
addrJack = Address('1500','Sherbrooke Est.','3','K1B 2H6', city='Quebec City')

# shopping 1
order1 = Order()
item11 = OrderItem(1, '101001', 'iPhone13', '5.25", 64GB memory, black', 1200, 1)
item12 = OrderItem(2, '102005', 'USB flash drive', '8GB', 14.99, 2)
item13 = OrderItem(3, '201006', 'Book', 'Art of Code', 59.99, 1)
order1.addToCart(item11)
order1.addToCart(item12)
order1.addToCart(item13)

# placing order 1
customer = 'Peter'
billAddress = addrPeter.getAddress()
order1.placeOrder(customer, billAddress)
# making payment
order1.checkout()
# packaging
order1.packaging()
# shipping
order1.ship()
print()
# print out order
print(order1.printOrderInfo())


# shopping 2
order2 = Order()
item21 = OrderItem(1, '401002', 'Chocolate', '12pieces 360g', 9.99, 1)
item22 = OrderItem(2, '502003', 'Game disks', 'Call of Duty, Elder Scroll', 11.99, 2)
order2.addToCart(item21)
order2.addToCart(item22)

# placing order 2
customer = 'Peter'
billAddress = addrPeter.getAddress()
receiver = 'Jack'
shipAddress = addrJack.getAddress()
order2.placeOrder(customer, billAddress, receiver, shipAddress)
print(order2.printOrderInfo())
# making payment
order2.checkout()
print(order2.printOrderInfo())
# packaging
order2.packaging()
print(order2.printOrderInfo())
# shipping
order2.ship()
# order2.cancelOrder()
print()
# print out order
print(order2.printOrderInfo())
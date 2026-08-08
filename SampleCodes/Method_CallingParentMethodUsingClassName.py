
class Notification:
    print("1")
    def send(self):
        print("2")
        print("Sending notification")

class Email(Notification):
    print("3")
    def send(self):
        print("4")
        Notification.send(self)
        print("5")
        print("Sending email")

obj = Email()
print("6")
obj.send()
print("7")


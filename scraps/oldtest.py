class Email(object):
    def __init__(self, msg, subj, sender, receiver):
        self.message = msg
        self.subject = subj
        self.sender = sender    #email address
        self.receiver = receiver #email address

# Using a dictionary        
class EmailLogger(object):
    def __init__(self):
        self.emails_sent = {}
        self.emails_received = {}

    def add(self,email):
        if not Email.sender in self.emails_sent:
            self.emails_sent[Email.sender] = []
        self.emails_sent[Email.sender].append(email)

        if not Email.receiver in self.emails_received:
            self.emails_received[Email.receiver] = []
        self.emails_received[Email.receiver].append(email)      

    def get_sent_by(self,sender):
        return self.emails_sent[sender]

    def get_received_by(self,receiver):
        return self.emails_received[receiver]

# Using a list
class EmailLogger(object):
    def __init__(self):
        self.emails = []

    def add(self,email):
        self.emails.append(email)

    def get_sent_by(self,sender):
        temp = []
        for e in self.emails:
            if e.sender == sender:
                temp.append(e)
        return temp

    def get_received_by(self,receiver):
        temp = []
        for e in self.emails:
            if e.receiver == receiver:
                temp.append(e)
        return temp

Logger = EmailLogger()

Email1 = Email("fake message 1","fake subject 1","joe@yahoo.com","sue@gmail.com")
Logger.add(Email1)

Email2 = Email("fake message 2","fake subject 2","bill@yahoo.com","sue@gmail.com")
Logger.add(Email2)

Email3 = Email("fake message 3","fake subject 3","bill@yahoo.com","joe@yahoo.com")
Logger.add(Email3)

Email4 = Email("fake message 4","fake subject 4","jon@hotmail.com","sue@gmail.com")
Logger.add(Email4)


list1 = Logger.get_sent_by("bill@yahoo.com")
print('list 1:',list1)
# list1 = [Email2,Email3]

list2 = Logger.get_received_by("sue@gmail.com")
print(list2)
# list2 = [Email1,Email2,Email4]
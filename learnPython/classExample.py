__author__ = 'Anthony'


class AddressBookEntry(object):
    "This is a AddressBookEntry Class"
    version = 1.0

    name = None
    phone = None

    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
    def __str__(self):
        s = 'name = %s  phone=%s' % (self.name, self.phone)
        return s
        #print(s)

    def updatePhone(self, ph):
        self.phone = ph



from pymongo import MongoClient
# Database Server Conenction Method
def dataconnect():
    try:
        client = MongoClient("mongodb://username:password@ds121349.mlab.com:21349/ertugrultosundb")
        db = client['ertugrultosundb']
        db.authenticate("username","password")
        print("Baglanti Basarili!")
        return db.Users
    except:
        print("Baglanti Basarisiz!")

class User(object):
    """.Sistemde yer alan kullanıcılar.

    Attributes:
        name: Kullanıcının ismi.
        surname: Kullanıcının soy ismi.
        mail: Kullanıcının mail adresi.
        tel: Kullanicının telefon numarasi.
        year: Uye olma tarihi.
        origin: Uye olunan ulke.
    """

    def __init__(self, name, surname, mail, tel, year, origin):
        """Yeni bir User objesi dondurur."""
        self.name = name
        self.surname = surname
        self.mail = mail
        self.tel = tel
        self.year = year
        self.origin = origin

    # Yeni eklenen user'ı db ortamına export eder.
    def user_insert(self):
        datab = dataconnect()
        datab.insert(
        {
           "name": self.name,
           "lastname": self.surname,
           "mail": self.mail,
           "dateofreg": self.year,
           "tel": self.tel,
           "country": self.origin
         }
        )

    # Var olan user'ı db ortamından drop eder.
    def user_delete(self,mail):
        datab = dataconnect()
        datab.remove({"mail": mail});

    # Var olan kullanıcının istenilen ogesini update eder.
    def user_update(self,mail,var1,var2):
        datab = dataconnect()
        datab.update({'mail':mail},{"$set":{var1:var2}})

tesla = User("Ahmet","Tosun","ahmet@ail.com","123456789","2018","TR")
tesla.user_insert()
tesla.user_update("ahmet@ail.com","tel","123")
#tesla.user_delete("ahmet@ail.com")

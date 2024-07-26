
class Person:
    def __init__(self, nom=""):
        self.nom=nom

def nom_valide(func_input):
    def wrapper(self, nom, *args, **kwargs):
        if not nom or not nom.isalpha() or not nom[0].isupper():
            raise ValueError("Le nom doit de user est invalide !!")
        return func_input(self, nom, *args, **kwargs)
    return wrapper

class User(Person):
    @nom_valide
    def __init__(self, nom="",email="", phone=""):
        super().__init__(nom)
        self.phone=phone
        self.email=email
    def __eq__(self,user):
        return self.nom.lower()==user.nom.lower()
    def __str__(self):
        return f"User nom:{self.nom}, email:{self.email}"

if __name__=='__main__':
    try:
        u1=User("ali")
        print(u1)
    except ValueError as e:
        print("Message:",e)


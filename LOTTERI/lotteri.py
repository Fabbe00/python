import random

class lotteri:
    def __init__(self):
        self.list_vinster = [
            "En Ford Galaxie 500XL",
            "Strumpa med hål",
            "Polaris Switchback Assault 850",
            "Chevelle SS",
            "Ford Mustang GT 350",
            "Impala SS 1964",
            "Kalsong Blå Volvo 740",
            "Chrysler 440 Big Block",
            "Cheva 454 Big Block",

        ]

    def get_vinst(self):
        slumptal = random.randint(0, len (self.list_vinster)-1)

        return self.list_vinster[slumptal]
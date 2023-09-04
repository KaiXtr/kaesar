from django.db import models
import datetime

class Personagens(models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=30)
    nascimento = models.DateField(default=datetime.date.today())
    
    SIGNOS = [
        (1,"Aquário"),
        (2,"Peixes"),
        (3,"Áries"),
        (4,"Touro"),
        (5,"Gêmeos"),
        (6,"Câncer"),
        (7,"Leão"),
        (8,"Virgem"),
        (9,"Libra"),
        (10,"Escorpião"),
        (11,"Sagitário"),
        (12,"Capricórnio")
    ]
    
    signo = models.CharField(max_length=20,choices=SIGNOS,default=1)

    def __str__(self) -> str:
        if (len(self.apelido) > 0):
            return f"{self.nome}: ({self.apelido})"
        else:
            return f"{self.nome}"
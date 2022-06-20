
from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField("Producto", max_length=100)
    valor = models.IntegerField("Precio")

    def __str__(self):
        return self.nombre + " -> " + self.valor


class Sala (models.Model):
    nombre = models.CharField("Nombre Sala", max_length=100)
    status = models.CharField("Estado", max_length=50)

    def __str__(self):
        return self.nombre + " : " + self.status


class Usuario(models.Model):
    nombre = models.CharField("Nombre ", max_length=150)
    username = models.CharField("Nombre de usuario", max_length=100)
    password = models.CharField("Contrasena", max_length=50)
    email = models.EmailField("Correo Electronico", max_length=254)

    def __str__(self) -> str:
        return "User:" + self.username


class Compra (models.Model):
    valor = models.IntegerField("Valor aportado")
    aporta = models.BooleanField("aporta")
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Fondo(models.Model):
    deuda = models.IntegerField("Valor debido")
    pagado = models.IntegerField("Valor pagado")
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Pagado: " + self.pagado + " Deuda: " + self.deuda

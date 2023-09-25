from django.db import models



class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mensagem= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
 


CATEGORIA_CHOICES = (
        ('Fundadores', 'Fundadores'),
        ('Presidência', 'Presidência'),
        ('Vice-Presidência', 'Vice-Presidência'),
        ('Área Administrativa', 'Área Administrativa')

)


class Categoria(models.Model):
    categoria = models.CharField(max_length=255, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return self.categoria



SUBCATEGORIA_CHOICES = (
        ('IA', 'IA'),
        ('RH', 'RH'),
        ('Projetos', 'Projetos'),
        ('FinQuant', 'FinQuant'),
        ('Marketing', 'Marketing'),
        ('The Office', 'The Office'),
        ('Contagramação', 'Contagramação'),
        ('Machine Learning', 'Machine Learning'),

)
class Subcategoria(models.Model):
    sub_categoria = models.CharField(max_length=255, choices=SUBCATEGORIA_CHOICES)

    def __str__(self):
        return self.sub_categoria



class Membro(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    sub_categoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    inativo = models.BooleanField(default=False)
    info = models.TextField()
    imagem = models.ImageField(upload_to='membros', null=True, blank=True)
    ano = models.IntegerField(default=2023)  

    def __str__(self):
        return self.nome




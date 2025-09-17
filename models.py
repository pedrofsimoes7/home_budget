from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Entry(models.Model):
    ENTRY_TYPE_CHOICES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    entry_type = models.CharField(max_length=10, choices=ENTRY_TYPE_CHOICES) #define se é receita ou despesa. 
    value = models.DecimalField(max_digits=10, decimal_places=2) #define o valor da receita ou despesa.
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #category é uma Foreign Key, on_delete=models.CASCADE  
    comment = models.TextField(blank=True)                           #garante que se a categoria for apagada, apaga as entradas associadas.

    def __str__(self):
        return f"{self.entry_type.capitalize()} - {self.value} on {self.date}"

#

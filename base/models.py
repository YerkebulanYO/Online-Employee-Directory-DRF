from django.db import models

# Иерархия сотрудников


class Employee(models.Model):

    POSITION_TYPES = (
        ('Intern', 'Intern'),
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
        ('President', 'President')
    )


    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=30, choices=POSITION_TYPES)
    employment_date = models.DateField(blank=True, null=True)
    salary = models.IntegerField()
    boss = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.full_name

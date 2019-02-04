from django.db import models
from datetime import datetime, date


class Image(models.Model):
    title = models.CharField(max_length=40, null=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.pk} #{self.title}'


class Document(models.Model):
    PASSPORT = 'PASS'
    BIRTH_CERTIFICATE = 'BIRTH'
    STUDENT_CARD = 'STUD'
    TYPES = (
        (PASSPORT, 'passport'),
        (BIRTH_CERTIFICATE, 'birth certificate'),
        (STUDENT_CARD, 'student card')
    )
    number = models.CharField(max_length=120, unique=True, null=False)
    issue_date = models.DateField(null=False)
    document_type = models.CharField(max_length=30, choices=TYPES)
    scan = models.ForeignKey(
        'personsapp.Image',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='scans'
    )
    person = models.ForeignKey(
        'personsapp.Person',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='documents'
    )

    def __str__(self):
        return f'{self.document_type} #{self.number}'


class Person(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER = ((MALE, 'male'), (FEMALE, 'female'))

    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    patr_name = models.CharField(max_length=40, null=False)
    birth_date = models.DateField(null=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=12, null=False)
    start_education = models.DateField()
    finish_education = models.DateField()
    education_group = models.CharField(max_length=120, null=False)
    education_place = models.CharField(max_length=120, null=False)

    @property
    def age(self):
        t2 = datetime.now()
        t1 = self.birth_date
        if isinstance(t1, date):
            t_year = (t2.year - t1.year)
            t_month = (t2.month - t1.month)
            t_day = (t2.day - t1.day)
            if t_month < 0 or t_day < 0:
                return t_year - 1
            return t_year

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

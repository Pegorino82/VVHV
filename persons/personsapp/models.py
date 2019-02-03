from django.db import models


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
    scan = models.FileField(upload_to='files/', null=True, blank=True)

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
    gender = models.CharField(max_length=1)
    phone = models.CharField(max_length=12, null=False)
    start_education = models.DateField(auto_now_add=True)
    finish_education = models.DateField()
    education_group = models.CharField(max_length=120, null=False)
    education_place = models.CharField(max_length=120, null=False)
    documents = models.ManyToManyField(Document)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


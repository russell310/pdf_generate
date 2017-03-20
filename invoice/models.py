from django.db import models

# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name


class Project(models.Model):
	company = models.ForeignKey(Company)
	description = models.CharField(max_length=100, blank=True, null=True)
	details = models.CharField(max_length=100, blank=True, null=True)
	paid = models.FloatField()
	payable = models.FloatField()

	def __str__(self):
		return self.description


class Invoice(models.Model):
	company = models.ForeignKey(Company)
	date = models.DateField()
	invoice_id = models.CharField(max_length=100, blank=True, null=True)
	address = models.CharField(max_length=255, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.EmailField(max_length = 100)
	reference = models.CharField(max_length=100, blank=True, null=True)
	issued = models.DateField()
	project = models.ManyToManyField(Project)

	def __str__(self):
		return str(self.company)
from django.db import models


class Person(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	age = models.PositiveSmallIntegerField();
	uploaded_file = models.FileField(upload_to="person_files/", blank=True, null=True,)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
import uuid
from django.db import models

class Topics(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default = uuid.uuid4,
		editable = False
		)
	name = models.CharField(max_length=200)

class Groups(models.Model):
	id = models.UUIDField(
		primary_key=True,
		default = uuid.uuid4,
		editable = False
		)
	name = models.CharField(max_length=200)
	topic = models.ForeignKey(
		Topics,
		on_delete=models.CASCADE,
		)

	def get_absolute_url(self):
		return reverse('group', args=[str(self.id)])



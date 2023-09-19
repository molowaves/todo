from django.db import models

class Todo(models.Model):
	note = models.TextField()
	completed = models.BooleanField(default=False)
	event_date = models.DateTimeField(blank=True)
	event_time = models.TimeField(blank=True)
	time_stamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.note


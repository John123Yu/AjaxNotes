from __future__ import unicode_literals
from django.db import models

class NotesManager(models.Manager):
    def addNote(self, title, content):
		errors = {}
		if any(x < 1 for x in (len(title), len(content) )):
			errors['allInputLengths'] = "All fields are required."
		if len(errors) is not 0:
			return (False, errors)
		elif len(errors) == 0:
			note = Notes.notesMgr.create(title = title, content = content)
			return (True, note)

class Notes(models.Model):
	title = models.TextField()
	content = models.TextField()
	notesMgr = NotesManager()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

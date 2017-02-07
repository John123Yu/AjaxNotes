from django.shortcuts import render, HttpResponse, redirect
from models import Notes
from django.core.urlresolvers import reverse
from django.views.generic.edit import View
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

def index(request):
	context = {
		'notes': Notes.notesMgr.all()
	}
	return render(request, 'AjaxNotes/index.html', context)

class AddNote(View):
	def get(self, request):
		context = {
			'notes': Notes.notesMgr.all()
		}
		return render(request, "AjaxNotes/indexAjax.html", context)
	def post(self, request):
		result = Notes.notesMgr.addNote(request.POST['title'], request.POST['content'])
		if result[0]:
			return redirect(reverse('AjaxNotes:addNote'))

def editNote(request):
	note = Notes.notesMgr.get(id = request.POST['id'])
	note.title = request.POST['title']
	note.content = request.POST['content']
	note.save()
	return JsonResponse(model_to_dict(note))

class DeleteNote(View):
	def get(self, request):
		context = {
			'notes': Notes.notesMgr.all()
		}
		return render(request, "AjaxNotes/indexAjax.html", context)
	def post(self, request):
		note = Notes.notesMgr.get(id = request.POST['id'])
		note.delete()
		return redirect(reverse('AjaxNotes:deleteNote'))


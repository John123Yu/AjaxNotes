from django.conf.urls import url, include 
from . import views
from views import AddNote, DeleteNote

urlpatterns = [
	url(r'^$', views.index, name = "index"),
	url(r'^addNote$', AddNote.as_view(), name = "addNote"),
	url(r'^editNote$', views.editNote, name = "editNote"),
	url(r'^deleteNote$', DeleteNote.as_view(), name = "deleteNote")

	]
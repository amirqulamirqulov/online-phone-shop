from xml.parsers.expat import model
from django.forms import  ModelForm
from .models import *


class Authorform(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
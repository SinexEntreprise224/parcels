from django import forms

from app.models import Parcels


class AddForm(forms.ModelForm):
   class Meta:
       model = Parcels
       fields = ["adr_arr", "adr_dep", "weight"]


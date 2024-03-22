from django import forms
# previously defined model
from .models import DNASequence

class DNASequenceForm(forms.ModelForm):
    class Meta:
        model = DNASequence
        fields = ['sequence']
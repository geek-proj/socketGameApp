from django import forms
from .models import UniqueCode
from django.contrib.messages.storage import session


class UserNameForm(forms.ModelForm):
    sender      = forms.CharField(max_length=100)
    class Meta:
        model = UniqueCode
        fields = ('sender',)

    def save(self, code):
        created = UniqueCode.objects.create(
            uniqueCode=code,
            sender=self.cleaned_data['sender'],
            receiver=''
        )
        return created

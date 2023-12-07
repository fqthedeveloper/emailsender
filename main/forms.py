from django import forms
from .models import Email


class EmailSendForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('email', 'subject','message')

    def __init__(self, *args, **kwargs):
        super(EmailSendForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
from django import forms

class UploadForm(forms.Form):
    your_name = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )

    gender = forms.CharField(
        label='Gender',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )

    memo = forms.CharField(
        label='Memo',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )


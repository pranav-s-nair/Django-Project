from django import forms


# class SignUp(forms.Form):
#     first_name = forms.CharField(initial='First Name', )
#     last_name = forms.CharField()
#     email = forms.EmailField(help_text='write your email', )
#     Address = forms.CharField(required=False, )


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='any valid file'
    )

from django import forms
from .models import Tag, RequestOfferPost, Profile
from .widgets import MapInput
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm
from django.utils.translation import ugettext_lazy as _
# def reverse_tuple_string(location_string):
#     if location_string == "":
#         return location_string
#     args = location_string.split(",")
#     return args[1] + "," + args[0]

# class LocationField(forms.CharField):

#     def __init__(self, *args, **kwargs):
#         map_attrs = kwargs.pop("map_attrs", None)
#         self.widget = MapInput(map_attrs=map_attrs, )

#         super().__init__(*args, **kwargs)
#         self.error_messages = {"required": "Please pick a location", }

#     def to_python(self, value):
#         return super().to_python(reverse_tuple_string(value))

class RequestOfferForm(forms.ModelForm):
    tag_names = forms.CharField(label="Tags", help_text="Enter tags separated by spaces.", widget=forms.TextInput(attrs={"class":"form-control"}))
    # location = LocationField()
    class Meta:
        model = RequestOfferPost
        fields = [
            'title',
            'post_text',
            'category',
            'request_or_offer',
            'post_image',
            'request_or_offer',
            'timeline_start',
            'timeline_end',
            'location',
        ]
        widgets = {
            'title' : forms.TextInput(attrs={"class":"form-control"}),
            'post_text' : forms.Textarea(attrs={"class":"form-control"}),
            'category' : forms.Select(attrs={"class":"form-control"}),
            'request_or_offer' : forms.Select(attrs={"class":"form-control"}),
            'post_image' : forms.FileInput(attrs={"class":"form-control-file"}),
            'timeline_start' : forms.DateInput(attrs={"class":"form-control"}),
            'timeline_end' : forms.DateInput(attrs={"class":"form-control"}),
        }

class ProfileForm(forms.ModelForm):
    profile_pic = forms.FileField(label='Upload Your Photo')
    class Meta:
        model = Profile
        fields = [
            'profile_pic',
            'community',
        ]

# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = [
#             'comment_text',
#         ]

class RegistrationForm(UserCreationForm):
    """
    Form for registering a new user account.
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.
    """
    LOCATION_CHOICES = (
        ('Raleigh', 'Raleigh'),
        ('Durham', 'Durham'),
        ('Wake Forest', 'Wake Forest'),
        ('Chapel Hill', 'Chapel Hill'),
        ('Cary', 'Cary'),
        ('Apex/Holly Springs', 'Apex/Holly Springs'),
        ('Garner', 'Garner'),
        ('Clayton', 'Clayton'),
        ('Knightdale/Zebulon', 'Knightdale/Zebulon'),
    )
    required_css_class = 'required'
    community = forms.CharField(max_length=55, widget=forms.Select(choices=LOCATION_CHOICES,attrs={'class':'form-control'})),
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class':'form-control'})),
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class':'form-control'})),

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            # 'password1',
            # 'password2',
            # 'community',
            ]
    
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            # 'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            # 'password2' : forms.PasswordInput(attrs={'class':'form-control'}),
            'community' : forms.Select(attrs={'class':'form-control'}),
        }

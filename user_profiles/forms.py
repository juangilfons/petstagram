from django import forms

from user_profiles.models import UserProfile


class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput)
    first_name = forms.CharField(label='First Name', max_length=100, required=False)
    last_name = forms.CharField(label='Last Name', max_length=100, required=False)

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio']
        labels = {
            'profile_picture': 'Change Picture',
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name

    def save(self, *args, **kwargs):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return super(UserProfileForm, self).save(*args, **kwargs)


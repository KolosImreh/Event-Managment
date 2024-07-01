# events/forms.py

from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Add custom logic here (e.g., send a welcome email)
        return user


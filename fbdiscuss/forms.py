from django import forms
import models

class DiscussionForm(forms.ModelForm):
    """ form DiscussionForm
    
    """
    
    class Meta:
        model = models.Discussion
        exclude=['owner', 'guid', 'created_at', 'access_token', 'session_key']
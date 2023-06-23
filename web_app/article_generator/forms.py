from django import forms


class VideoUrlForm(forms.Form):
    video_url = forms.CharField(max_length=100, widget=forms.URLInput(attrs={'class': 'main__input'}))

    class Meta:
        fields = ['video_url']

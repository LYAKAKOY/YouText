from django import forms


class VideoUrlForm(forms.Form):
    video_url = forms.CharField(max_length=100, widget=forms.URLInput(attrs={'class': 'main__input'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'main__input'}), required=False)
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'main__input'}), required=False)
    annotation_length = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'main__input'}), required=False)
    article_length = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'main__input'}), required=False)
    interval_picture = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'main__input'}), required=False)

    class Meta:
        fields = '__all__'

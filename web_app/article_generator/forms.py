from django import forms


class VideoUrlForm(forms.Form):
    video_url = forms.CharField(max_length=100, widget=forms.URLInput(attrs={'class': 'main__input-field'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': "00:03:25"}), required=False)
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': "00:15:24"}), required=False)
    annotation_length = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'main__input', 'placeholder': "250"}),
                                           required=False)
    article_length = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'main__input', 'placeholder': "1500"}),
                                        required=False)
    interval_picture = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'main__input', 'placeholder': "30"}),
                                          required=False)

    class Meta:
        fields = '__all__'

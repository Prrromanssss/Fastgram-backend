from django import forms
from response.models import MainImage, Response


class MainImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = MainImage
        fields = (
            MainImage.image.field.name,
        )


class ResponseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Response
        fields = (
            Response.name.field.name,
            Response.delivery.field.name,
            Response.text.field.name,
            Response.grade.field.name,
        )
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 5,
            }),
        }
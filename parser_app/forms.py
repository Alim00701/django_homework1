from . import parser, models
from django import forms


class ParseForm(forms.Form):
    MEDIA_CHOICE = (
        ('FILMS', 'FILMS'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        model = models.Film
        fields = [
            'media_type',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'FILMS':
            films_parser = parser.parser_func()
            for i in films_parser:
                models.Film.objects.create(**i)

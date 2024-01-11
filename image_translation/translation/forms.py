# from django import forms

from django import forms



class SelectChoiceForm(forms.Form):
    choice1 = forms.fields.ChoiceField(
        choices = (
            ('english', '英語'),
            ('german', 'ドイツ語'),
            ('chinese', '中国語'),
            ('japanese', '日本語'),
            ('korean', '韓国語'),
            ('french', 'フランス語')

        ),
        required=True,
        widget=forms.widgets.Select
    )

    choice2 = forms.fields.ChoiceField(
        choices = (
            ('pdf', 'pdf'),
            ('txt', 'txt'),
            ('xlsx', 'xlsx'),
            ('csv', 'csv'),
        ),
        required=True,
        widget=forms.widgets.Select
    ),

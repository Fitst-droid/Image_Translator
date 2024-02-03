import datetime
from django import forms
from django.core.files.storage import default_storage


class ControlForm(forms.Form):
    file = forms.ImageField(label='画像')

    def save(self):
        """ファイルを保存するメソッド"""
        now_date = datetime.datetime.now().strftime('%Y%m%d_%H%M')
        upload_file = self.files['file']
        file_name = default_storage.save(now_date + "_" + upload_file.name, upload_file)
        return default_storage.url(file_name)

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

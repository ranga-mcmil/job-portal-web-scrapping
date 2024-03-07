from django import forms

class SearchForm(forms.Form):
    val = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'val',
            'id': 'search-input01'
        }
    ))

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()
        val = cl_data.get('val')
        return val
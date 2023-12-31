from django import forms
from catalog.models import Product, Version

LIMITATIONS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'img', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(CreateProductForm, self).__init__(*args, **kwargs)

        # Добавляем классы Bootstrap к полям формы
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['img'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({
            'class': 'form-select custom-select',  # Добавляем класс Bootstrap для кастомного стиля
            'style': 'background-color: #f5f5f5; width: 100%;',  # Настройка стиля
        })
        self.fields['price'].widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')
        for limitation in LIMITATIONS:
            if limitation in cleaned_name:
                raise forms.ValidationError('Ошибка, связанная с именем пользователя')

        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')
        for limitation in LIMITATIONS:
            if limitation in cleaned_description:
                raise forms.ValidationError('Ошибка, связанная с описанием')

        return cleaned_description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['number', 'name', 'active']

    def __init__(self, *args, **kwargs):
        super(VersionForm, self).__init__(*args, **kwargs)

        # Добавляем классы Bootstrap к полям формы
        self.fields['number'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})

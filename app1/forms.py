import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from app1.models import Login, Bill, Equipments, Batch, Payment


class TrainerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','password1','password2','name','age','email','address','contact_no','photo')


class Product(forms.ModelForm):
    class Meta:
        model = Equipments
        fields = '__all__'


class AddBill(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Login.objects.filter(is_customer=True))

    class Meta:
        model = Bill
        exclude = ('status',)


class CustomerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2', 'name', 'age', 'email', 'address', 'contact_no', 'photo', 'batch', 'batch_time')


class TimeInput(forms.TimeInput):
    input_type = 'time'


class Section(forms.ModelForm):
    batch_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))

    class Meta:
        model = Batch
        fields = '__all__'


MONTH_CHOICES = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
)


def current_year():
    return datetime.date.today().year


def year_choices():
    return [(r, r) for r in range(2021, datetime.date.today().year + 10)]


class Pay(forms.ModelForm):
    card_number = forms.CharField(validators=[RegexValidator(regex='^.{16}$', message='Please Enter a Valid Card No')])
    card_cvv = forms.CharField(validators=[RegexValidator(regex='^.{3}$', message='Please Enter a Valid CVV')])
    card_expiry_month = forms.ChoiceField(choices=MONTH_CHOICES)
    card_expiry_year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
    class Meta:
        model = Payment
        fields = ('card_number', 'card_cvv', 'card_expiry_month', 'card_expiry_year')
from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    # username = forms.CharField(label="用户名", max_length=128)
    # password = forms.CharField(label="密码", max_length=256)
    #给表单加CSS样式
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))
    captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')

# class ECGData(forms.Form):
#     client_name = forms.CharField(label='佩戴用户',max_length=256)
#     begin_time = forms.DateTimeField(label='记录起始时间')
#     end_time = forms.DateTimeField(label='记录结束时间')
#     ecg = forms.TextField(label='心率数据')
#     ecg_label = forms.TextField(label='心率分类')


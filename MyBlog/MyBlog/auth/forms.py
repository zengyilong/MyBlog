# -*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('保持登录状态')
    submit = SubmitField('登录')


class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField('用户名', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          '用户名只能由字母、数字，'
                                          '小数点和下划线组成')])
    password = PasswordField('密码', validators=[
        Required(), EqualTo('password2', message='输入密码不一致')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该Email已经被注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已经被注册')


class ChangePasswordForm(Form):
    old_password = PasswordField('旧密码', validators=[Required()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='两次输入的新密码不一致')])
    password2 = PasswordField('确认新密码', validators=[Required()])
    submit = SubmitField('修改密码')


class PasswordResetRequestForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField('重设密码')


class PasswordResetForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='两次输入的新密码不一致')])
    password2 = PasswordField('确认新密码', validators=[Required()])
    submit = SubmitField('重设密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('邮箱错误')


class ChangeEmailForm(Form):
    email = StringField('新Email地址', validators=[Required(), Length(1, 64),
                                                 Email()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('修改邮箱地址')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('这个Email已被注册')

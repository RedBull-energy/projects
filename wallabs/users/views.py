'''from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .models import Contact


def login(request):
    return render(request, "users/login.html")


def reg(request):

    # Если метод запроса POST
    if request.method == 'POST':
        # Берем данные с формы проверяем их
        # если все в порядке сохраняем нового пользователя
        form = ContactForm(request.POST)
        if form.is_valid():

            subject = "Пробное сообщение"
            # Авторизуем пользователя и переходим на главную страницу
            body = Contact(
                 form.cleaned_data['email_address'],
                 form.cleaned_data['username'],
            )
            body.save()
            message = ''
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            login(request)
            return render(request, 'users/login.html')

        # Если что-то пошло не так отображаем форму
        # с данными которые ввел пользователь для
        # их исправления
        else:
            context = {'form': form}
            return render(request, 'registration/reg.html', context)

    # При GET запросе отображаем пустую форму
    context = {'form': ContactForm()}
    return render(request, 'registration/reg.html', context)


@login_required
def home(request):

    return render(request, 'registration/home.html')
'''
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password, is_password_usable
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .forms import SignupForm, UserLoginForm
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.backends import BaseBackend

'''def login(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            pass
    else:
        pass
    return render(request, "users/login.html")'''

'''class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None'''

'''def login_view(request):
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        print("valid")
        if form.is_valid():

            user_obj = form.cleaned_data.get('user_obj')
            print("user")
            login(request, user_obj)
            print("login")
            return redirect('home') # if you want to redirect same page then, return redirect('this function name in urls.py')

    return render(request, 'users/reg.html', {'form': form})'''


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                print("user")
                if user.is_active:
                    login(request, user)
                    return render(request, 'registration/home.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return render(request, 'users/login.html', {'form': form})
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            print("save")
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            print("cool_boy")
            messages.success(request, 'Please confirm your email address to complete the registration')

            # return HttpResponse('Please confirm your email address to complete the registration')
        else:
            form = SignupForm()
            messages.success(request, 'Please check your nickname')
            '''cd = form.cleaned_data
            user = authenticate(username=cd['username'])
            if user == ''' # доделать логику
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return get_success_url()
    else:
        return HttpResponse('Activation link is invalid!')


'''def get_success_url(self):
    return reverse_lazy('home')'''


@login_required
def get_success_url(request):
    return render(request, 'registration/home.html')



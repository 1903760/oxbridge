from django.views.generic.base import TemplateView
from .models import Review, PostStudy, Test
from .forms import ContactForm
from django.core.mail import send_mail
from oxbridge import settings
from django.views.generic.list import ListView
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
# Create your views here.


class TestListView(ListView):
    template_name = 'home/test_list.html'
    model = Test
    context_object_name = 'tests'


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        context['posts'] = PostStudy.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            email_subject = 'OXBRIDGE.KZ :: Сообщение через контактную форму '
            email_body = "С сайта отправлено новое сообщение\n\n" \
                         "Имя отправителя: %s \n" \
                         "E-mail отправителя: %s \n\n" \
                         "Сообщение: \n" \
                         "%s " % \
                         (form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['tel'])
            # send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['target_email@example.com'],
            #           fail_silently=False)
            data = {}
            data['ok'] = 'Ваша заявка успешно отправллено!'
            return JsonResponse(data)
        else:
            data = {}
            data['no'] = 'Упс ошибка'
            return JsonResponse(data)


@require_http_methods(["POST"])
def send_contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        email_subject = 'OXBRIDGE.KZ :: Сообщение через контактную форму '
        email_body = "С сайта отправлено новое сообщение\n\n" \
                     "Имя отправителя: %s \n" \
                     "E-mail отправителя: %s \n\n" \
                     "Сообщение: \n" \
                     "%s " % \
                     (form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['tel'])
        # send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['target_email@example.com'],
        #           fail_silently=False)
        return JsonResponse()
    else:
        return JsonResponse('no', content_type='text/html')
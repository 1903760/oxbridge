from django.shortcuts import render
from django.views.generic.detail import DetailView
from home.models import Answer, Test
from orders.models import ScoringScale
from django.http import JsonResponse
from .forms import OrderForm
import bisect


class OrderView(DetailView):
    template_name = 'orders/test.html'
    context_object_name = 'test'
    model = Test
    slug_url_kwarg = 'slug'

    def post(self, request, *args, **kwargs):
        sum_test = 0
        ball = dict(request.POST)
        order_form = {}
        order_form['name'] = request.POST['name']
        order_form['phone'] = request.POST['tel']
        ball.pop('csrfmiddlewaretoken')
        ball.pop('name')
        ball.pop('tel')
        filter_ball = (int(x[0]) for x in ball.values())
        LEVEL = list(ScoringScale.objects.all().values_list('balls', 'name'))
        for i in filter_ball:
            sum_test += Answer.objects.get(id=i).rights
        idx = min(bisect.bisect(LEVEL, (sum_test,)), len(LEVEL) - 1)
        level = LEVEL[idx][1]
        order_form['level'] = ScoringScale.objects.get(name=level).id
        form = OrderForm(order_form)
        if form.is_valid():
            form.save()
        data = {}
        data['ok'] = 'Вы набрали {} балла. Ваш уровень {}! В ближайшее время с вами свяжуться'.format(sum_test, level)
        return JsonResponse(data)
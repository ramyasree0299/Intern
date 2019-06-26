from django.views import View
from django.shortcuts import render, redirect
from django.urls import resolve
from groceries.forms.FormModule import *
from django.contrib.auth import *
from django.contrib.auth.mixins import *


class DisplayItemsView(LoginRequiredMixin, View):
    login_url = '/groceries/login/'
    def get(self, request, *args, **kwargs):
     c = grocery_items.objects.values("name", "company","quantity","amount").distinct()
     DICT_QUERY_SET = dict()
     DICT_QUERY_SET['result_set'] = c
     return render(request, 'groceries_items_list.html', DICT_QUERY_SET)


class AddItemsView(LoginRequiredMixin, View):
    login_url = '/groceries/login/'
    def get(self, request, *args, **kwargs):
        form = AddItem()
        if resolve(request.path_info).url_name == 'delete_item':
            grocery_items.objects.get(name=kwargs.get('item_name')).delete()
            return redirect("http://127.0.0.1:8000/groceries/items/")
        if kwargs:
            c = grocery_items.objects.filter(name=kwargs.get("item_name")).first()
            form = AddItem(instance=c)
        return render(
            request,
            template_name="add_item.html",
            context=
            {
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if resolve(request.path_info).url_name == 'edit_item':
                c = grocery_items.objects.get(name=kwargs.get('item_name'))
                form = AddItem(request.POST, instance=c)
                if form.is_valid():
                    topic = form.save(commit=False)
                    topic.save()
                    return redirect("http://127.0.0.1:8000/groceries/items/")
            form = AddItem(request.POST)
            if form.is_valid():
                topic = form.save(commit=False)
                topic.save()
            return redirect("http://127.0.0.1:8000/groceries/items/")
        else:
            form = AddItem()
        return render(
            request,
            template_name="add_item.html",
            context=
            {
                'form': form,
                'title': "Item Added"
            }
        )



class LoginController(View):
    def get(self, request, *args, **kwargs):
        login = Login()
        return render(
            request,
            template_name="login.html",
            context=
            {
                'login': login
            }
        )

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("http://127.0.0.1:8000/groceries/items/")
        else:
            return redirect("http://127.0.0.1:8000/groceries/login/")


def logout_user(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/groceries/login/")

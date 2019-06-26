"""internproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from groceries.Views import groceryviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('groceries/items/', groceryviews.DisplayItemsView.as_view(),name="homepage"),

    path('groceries/items/add_item/', groceryviews.AddItemsView.as_view(), name='add_item'),
    path('groceries/items/edit/<str:item_name>/', groceryviews.AddItemsView.as_view(), name='edit_item'),
    path('groceries/items/delete/<str:item_name>/', groceryviews.AddItemsView.as_view(), name='delete_item'),
    path('groceries/login/', groceryviews.LoginController.as_view(),name='login_page'),
    path('groceries/items/logout/',groceryviews.logout_user,name='logout_page'),


]

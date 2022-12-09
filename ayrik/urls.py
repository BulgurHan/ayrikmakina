"""ayrik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from page.views import (loginPage,mainpage,machines,
                        native_products,products,
                        customers,customer_detail,logoutPage,
                        addCustomer,customer_redirect,changeCustomer,
                        addProduct,references,allPproducts,changeProduct,deleteProduct,
                        deleteCustomer,deleteNotification,deleteNot)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainpage,name="mainpage"),
    path("login/", loginPage ,name="loginPage"),
    path("logout/", logoutPage ,name="logoutPage"),
    path("machines/", machines ,name="machines"),
    path("native-products/", native_products ,name="native_products"),
    path("products/", products ,name="products"),
    path("all-products/", allPproducts ,name="allPproducts"),
    path("customers/", customers ,name="customers"),
    path("references/", references ,name="references"),
    path("customers/add/", addCustomer ,name="addCustomer"),
    path("customers/change/<int:customer_pk>/", changeCustomer ,name="changeCustomer"),
    path("customers/<int:customer_pk>/", customer_detail ,name="customer_detail"),
    path("redirect/<int:notification_pk>/", customer_redirect ,name="customer_redirect"),
    path("products/add/", addProduct ,name="addProduct"),
    path("products/change/<int:product_pk>/", changeProduct ,name="changeProduct"),
    path("products/delete/<int:product_pk>/", deleteProduct ,name="deleteProduct"),
    path("customers/delete/<int:customer_pk>/", deleteCustomer ,name="deleteCustomer"),
    path('redirect/', deleteNotification, name='deleteNotification'),
    path('delete/<int:not_pk>/', deleteNot, name='deleteNot')
]

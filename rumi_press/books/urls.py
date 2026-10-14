from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reports/expenses/", views.expense_report, name="expense_report"),
]
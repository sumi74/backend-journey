from decimal import Decimal

from django.db.models import Sum
from django.shortcuts import render

from .models import Category


def expense_report(request):
    categories = list(
        Category.objects.annotate(
            total_expenses=Sum("books__distribution_expenses")
        ).order_by("name")
    )

    max_total = max(
        (category.total_expenses or Decimal("0") for category in categories),
        default=Decimal("0"),
    )

    for category in categories:
        total = category.total_expenses or Decimal("0")
        category.bar_width = (
            total / max_total * Decimal("100")
            if max_total
            else Decimal("0")
        )

    return render(
        request,
        "books/expense_report.html",
        {"categories": categories},
    )

def home(request):
    return render(request, "books/home.html")

import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from books.models import Book, Category


CATEGORY_NAMES = {
    "business analytics": "Business Analytics",
    "data ethics": "Data Ethics",
    "data science": "Data Science",
    "deep learning": "Deep Learning",
    "maths": "Math",
    "nlp": "NLP",
    "python": "Python",
    "r studio": "R Studio",
    "sql": "SQL",
    "statistics": "Statistics",
    "visualization": "Visualization",
}


def parse_date(value):
    value = (value or "").strip()
    if not value:
        return None

    for date_format in ("%m/%d/%Y", "%m/%d/%y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, date_format).date()
        except ValueError:
            continue

    return None


class Command(BaseCommand):
    help = "Import books from books.csv"

    def handle(self, *args, **options):
        csv_path = Path(settings.BASE_DIR) / "books.csv"

        if not csv_path.exists():
            raise CommandError(f"Could not find {csv_path}")

        created_count = 0
        skipped_count = 0
        error_count = 0

        with csv_path.open(newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row_number, row in enumerate(reader, start=2):
                try:
                    title = (row.get("title") or "").strip()
                    authors = (row.get("authors") or "").strip()

                    if not title or not authors:
                        skipped_count += 1
                        continue

                    raw_category = (row.get("category") or "").strip()
                    category_name = CATEGORY_NAMES.get(
                        raw_category.lower(),
                        raw_category or "Uncategorized",
                    )
                    category, _ = Category.objects.get_or_create(
                        name=category_name
                    )

                    expense_text = (
                        (row.get("distribution_expense") or "0")
                        .strip()
                        .replace(",", "")
                    )
                    expense = Decimal(expense_text or "0")

                    _, was_created = Book.objects.get_or_create(
                        title=title,
                        subtitle=(row.get("subtitle") or "").strip(),
                        authors=authors,
                        publisher=(row.get("publisher") or "").strip(),
                        publish_date=parse_date(row.get("published_date")),
                        category=category,
                        distribution_expenses=expense,
                    )

                    if was_created:
                        created_count += 1
                    else:
                        skipped_count += 1

                except (ValueError, InvalidOperation, KeyError) as error:
                    error_count += 1
                    self.stderr.write(
                        self.style.WARNING(
                            f"Row {row_number} skipped: {error}"
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS(
                f"Import finished: {created_count} added, "
                f"{skipped_count} already present or incomplete, "
                f"{error_count} errors."
            )
        )
# Generated by Django 3.2.22 on 2023-12-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discount", "0074_promotionrule_checkout_and_order_predicate"),
    ]

    operations = [
        migrations.AddField(
            model_name="promotionrule",
            name="reward_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("subtotal_discount", "subtotal_discount"),
                    ("total_discount", "total_discount"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]

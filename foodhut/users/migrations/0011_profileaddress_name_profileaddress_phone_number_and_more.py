# Generated by Django 4.2.1 on 2023-06-06 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_profileaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileaddress',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profileaddress',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='mobile number'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_no', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(max_length=50)),
                ('payment_status', models.CharField(max_length=50)),
                ('total_mrp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('offer_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupon_discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('to_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profileaddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
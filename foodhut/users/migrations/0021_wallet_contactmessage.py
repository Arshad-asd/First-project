# Generated by Django 4.2.1 on 2023-07-05 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_cart_coupon_applied'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(choices=[('cancellation', 'Cancellation'), ('return', 'Return'), ('payment_issue', 'Payment Issue'), ('delivery_issue', 'Delivery Issue'), ('reservation', 'Table Reservation'), ('menu_inquiry', 'Menu Inquiry'), ('food_delivery', 'Food Delivery'), ('takeaway', 'Takeaway'), ('billing_issue', 'Billing Issue'), ('feedback', 'Feedback'), ('other', 'Other')], max_length=200)),
                ('message', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

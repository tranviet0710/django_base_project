# Generated by Django 3.2.8 on 2022-06-17 17:51
import os
import uuid

from django.contrib.auth.hashers import make_password
from django.db import migrations
from rest_framework.utils import json

from api_account.constants import RoleData


def initial_admin_data(apps, self):
    account_model = apps.get_model('api_account', 'Account')
    accounts = []
    json_data = json.load(open('api_account/constants/admin.json', encoding="utf8"))
    default_admin_password = make_password(os.getenv('DEFAULT_ADMIN_PASSWORD'))
    admin_role = RoleData.ADMIN.value.get('id')
    for account_data in json_data:
        account = account_model(id=uuid.uuid4(),
                                username=account_data['username'],
                                email=account_data['email'],
                                password=default_admin_password,
                                role_id=admin_role)
        accounts.append(account)
    account_model.objects.bulk_create(accounts)


class Migration(migrations.Migration):
    dependencies = [
        ('api_account', '0004_alter_account_info'),
    ]
    operations = [
        migrations.RunPython(initial_admin_data, migrations.RunPython.noop)
    ]

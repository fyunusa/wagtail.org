# Generated by Django 3.2.16 on 2022-10-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0053_streamfield_use_json_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signupformsnippet",
            name="mailchimp_newsletter_id",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Mailchimp Audience ID"
            ),
        ),
    ]

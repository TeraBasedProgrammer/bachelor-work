# Generated by Django 5.1.1 on 2024-10-12 11:45

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="ActivityCategory",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "activity_categories",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_admin",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=25)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=20, unique=True),
                ),
                ("name", models.CharField(max_length=50)),
                ("profile_picture", models.URLField()),
                ("id_card_photo", models.URLField(null=True)),
                ("is_verified", models.BooleanField(default=False)),
                ("balance", models.PositiveSmallIntegerField(default=0)),
                ("cv_link", models.URLField(null=True)),
                ("about_me_text", models.TextField(blank=True)),
                ("about_me_video_link", models.URLField(null=True)),
                ("service_price", models.FloatField()),
                (
                    "service_price_type",
                    models.CharField(
                        choices=[("PH", "Per hour"), ("PL", "Per lesson")], max_length=2
                    ),
                ),
                ("longitude", models.CharField(max_length=25)),
                ("latitude", models.CharField(max_length=25)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "db_table": "users",
            },
        ),
        migrations.CreateModel(
            name="UserVerifications",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PD", "Pending"),
                            ("AP", "Approved"),
                            ("DC", "Declined"),
                        ],
                        max_length=2,
                    ),
                ),
                ("admin_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "user_verifications",
            },
        ),
        migrations.CreateModel(
            name="ActivityCategoryUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("S", "Seeking"), ("P", "Providing")], max_length=2
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.activitycategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "activity_categories_users",
                "unique_together": {("user", "type", "category")},
            },
        ),
    ]
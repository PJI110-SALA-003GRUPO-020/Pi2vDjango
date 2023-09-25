# Generated by Django 4.2.4 on 2023-09-25 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                    "categoria",
                    models.CharField(
                        choices=[
                            ("Fundadores", "Fundadores"),
                            ("Presidência", "Presidência"),
                            ("Vice-Presidência", "Vice-Presidência"),
                            ("Área Administrativa", "Área Administrativa"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contato",
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
                ("nome", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("mensagem", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Subcategoria",
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
                    "sub_categoria",
                    models.CharField(
                        choices=[
                            ("IA", "IA"),
                            ("RH", "RH"),
                            ("Projetos", "Projetos"),
                            ("FinQuant", "FinQuant"),
                            ("Marketing", "Marketing"),
                            ("The Office", "The Office"),
                            ("Contagramação", "Contagramação"),
                            ("Machine Learning", "Machine Learning"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Membro",
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
                ("nome", models.CharField(max_length=255)),
                ("ativo", models.BooleanField(default=True)),
                ("inativo", models.BooleanField(default=False)),
                ("info", models.TextField()),
                (
                    "imagem",
                    models.ImageField(blank=True, null=True, upload_to="membros"),
                ),
                ("ano", models.IntegerField(default=2023)),
                (
                    "categoria",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="feadev.categoria",
                    ),
                ),
                (
                    "sub_categoria",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="feadev.subcategoria",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0027_auto_20210501_0839"),
    ]

    operations = [
        migrations.AlterField(
            model_name="citycouncilagenda",
            name="event_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("sessao_ordinaria", "Sessão Ordinária"),
                    ("ordem_do_dia", "Ordem do Dia"),
                    ("sessao_solene", "Sessão Solene"),
                    ("sessao_especial", "Sessão Especial"),
                    ("audiencia_publica", "Audiência Pública"),
                    ("sessao_extraordinaria", "Sessão Extraordinária"),
                    ("termo_de_encerramento", "Termo de Encerramento"),
                ],
                db_index=True,
                max_length=30,
                null=True,
                verbose_name="Tipo do evento",
            ),
        ),
        migrations.AlterField(
            model_name="citycouncilminute",
            name="event_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("sessao_ordinaria", "Sessão Ordinária"),
                    ("ordem_do_dia", "Ordem do Dia"),
                    ("sessao_solene", "Sessão Solene"),
                    ("sessao_especial", "Sessão Especial"),
                    ("audiencia_publica", "Audiência Pública"),
                    ("sessao_extraordinaria", "Sessão Extraordinária"),
                    ("termo_de_encerramento", "Termo de Encerramento"),
                ],
                db_index=True,
                max_length=30,
                null=True,
                verbose_name="Tipo de evento",
            ),
        ),
    ]
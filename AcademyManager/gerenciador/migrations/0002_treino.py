# Generated by Django 4.0.5 on 2022-06-17 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=1)),
                ('regiao', models.CharField(max_length=50)),
                ('Aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciador.aluno')),
            ],
        ),
    ]
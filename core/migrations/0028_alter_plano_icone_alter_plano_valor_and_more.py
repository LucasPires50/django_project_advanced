# Generated by Django 5.0 on 2024-01-11 15:07

import djmoney.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_plano_alter_recurso_icone_alter_servico_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='icone',
            field=models.CharField(choices=[('lni-laptop-phone', 'Celular'), ('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-mobile', 'Mobile'), ('lni-layers', 'Camadas'), ('lni-leaf', 'Folha'), ('lni-drop', 'Gota'), ('lni-layers', 'Design'), ('lni-package', 'Caixa'), ('lni-star', 'Estrela'), ('lni-users', 'Usuários'), ('lni-rocket', 'Foguete')], max_length=16, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='plano',
            name='valor',
            field=djmoney.models.fields.MoneyField(decimal_places=0, default_currency='BRL', max_digits=4, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-laptop-phone', 'Celular'), ('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-mobile', 'Mobile'), ('lni-layers', 'Camadas'), ('lni-leaf', 'Folha'), ('lni-drop', 'Gota'), ('lni-layers', 'Design'), ('lni-package', 'Caixa'), ('lni-star', 'Estrela'), ('lni-users', 'Usuários'), ('lni-rocket', 'Foguete')], max_length=16, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-laptop-phone', 'Celular'), ('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-mobile', 'Mobile'), ('lni-layers', 'Camadas'), ('lni-leaf', 'Folha'), ('lni-drop', 'Gota'), ('lni-layers', 'Design'), ('lni-package', 'Caixa'), ('lni-star', 'Estrela'), ('lni-users', 'Usuários'), ('lni-rocket', 'Foguete')], max_length=16, verbose_name='Icone'),
        ),
    ]

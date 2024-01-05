# Generated by Django 5.0 on 2024-01-05 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_recurso_descricao_alter_recurso_icone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-layers', 'Camadas'), ('lni-rocket', 'Foguete'), ('lni-mobile', 'Mobile'), ('lni-layers', 'Design'), ('lni-stats-up', 'Gráfico'), ('lni-leaf', 'Folha'), ('lni-users', 'Usuários'), ('lni-laptop-phone', 'Celular')], max_length=16, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-layers', 'Camadas'), ('lni-rocket', 'Foguete'), ('lni-mobile', 'Mobile'), ('lni-layers', 'Design'), ('lni-stats-up', 'Gráfico'), ('lni-leaf', 'Folha'), ('lni-users', 'Usuários'), ('lni-laptop-phone', 'Celular')], max_length=16, verbose_name='Icone'),
        ),
    ]

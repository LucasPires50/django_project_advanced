# Generated by Django 5.0 on 2024-01-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_alter_plano_icone_alter_recurso_icone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='icone',
            field=models.CharField(choices=[('lni-leaf', 'Folha'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-star', 'Estrela'), ('lni-rocket', 'Foguete'), ('lni-layers', 'Design'), ('lni-laptop-phone', 'Celular'), ('lni-cog', 'Engrenagem'), ('lni-mobile', 'Mobile'), ('lni-package', 'Caixa'), ('lni-drop', 'Gota'), ('lni-layers', 'Camadas')], max_length=16, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-leaf', 'Folha'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-star', 'Estrela'), ('lni-rocket', 'Foguete'), ('lni-layers', 'Design'), ('lni-laptop-phone', 'Celular'), ('lni-cog', 'Engrenagem'), ('lni-mobile', 'Mobile'), ('lni-package', 'Caixa'), ('lni-drop', 'Gota'), ('lni-layers', 'Camadas')], max_length=16, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-leaf', 'Folha'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-star', 'Estrela'), ('lni-rocket', 'Foguete'), ('lni-layers', 'Design'), ('lni-laptop-phone', 'Celular'), ('lni-cog', 'Engrenagem'), ('lni-mobile', 'Mobile'), ('lni-package', 'Caixa'), ('lni-drop', 'Gota'), ('lni-layers', 'Camadas')], max_length=16, verbose_name='Icone'),
        ),
    ]

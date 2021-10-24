# Generated by Django 3.2.8 on 2021-10-24 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название класса')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.CreateModel(
            name='CircleToSpell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(verbose_name='Круг заклинания')),
                ('character_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser.characterclass', verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Круг',
                'verbose_name_plural': 'Круги',
            },
        ),
        migrations.CreateModel(
            name='FocusedSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название подшколы')),
            ],
            options={
                'verbose_name': 'Подшкола',
                'verbose_name_plural': 'Подшколы',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название школы')),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школа',
            },
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название заклинания')),
                ('source', models.CharField(blank=True, max_length=256, null=True, verbose_name='Источник')),
                ('time', models.CharField(blank=True, max_length=256, null=True, verbose_name='Время сотворения')),
                ('components', models.CharField(blank=True, max_length=256, null=True, verbose_name='Компоненты')),
                ('distance', models.CharField(blank=True, max_length=256, null=True, verbose_name='Дистанция')),
                ('effect', models.CharField(blank=True, max_length=256, null=True, verbose_name='Эффект')),
                ('duration', models.CharField(blank=True, max_length=256, null=True, verbose_name='Длительносты')),
                ('challenge', models.CharField(blank=True, max_length=256, null=True, verbose_name='Испытание')),
                ('resist', models.CharField(blank=True, max_length=256, null=True, verbose_name='Устойчивость к магии')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('raw_data', models.TextField(blank=True, null=True, verbose_name='Дамп данных')),
                ('circles', models.ManyToManyField(related_name='spell_circles', through='parser.CircleToSpell', to='parser.CharacterClass', verbose_name='Круги')),
                ('focused_schools', models.ManyToManyField(to='parser.FocusedSchool', verbose_name='Подшколы')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser.school', verbose_name='Школа')),
            ],
            options={
                'verbose_name': 'Заклинание',
                'verbose_name_plural': 'Заклинания',
            },
        ),
        migrations.AddField(
            model_name='circletospell',
            name='spell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parser.spell', verbose_name='Заклинание'),
        ),
    ]

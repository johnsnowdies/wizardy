from django.db import models


class NameBasedModel(models.Model):
    name = ''

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class CharacterClass(NameBasedModel):
    name = models.CharField(max_length=256, verbose_name='Название класса')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class School(NameBasedModel):
    name = models.CharField(max_length=256, verbose_name='Название школы')

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школа'


class FocusedSchool(NameBasedModel):
    name = models.CharField(max_length=256, verbose_name='Название подшколы')

    class Meta:
        verbose_name = 'Подшкола'
        verbose_name_plural = 'Подшколы'


class CircleToSpell(models.Model):
    level = models.PositiveIntegerField(verbose_name='Круг заклинания')
    character_class = models.ForeignKey(CharacterClass, verbose_name='Класс', on_delete=models.CASCADE)
    spell = models.ForeignKey('parser.Spell', verbose_name='Заклинание', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.character_class.name} ({self.level})'

    class Meta:
        verbose_name = 'Круг'
        verbose_name_plural = 'Круги'


class Spell(NameBasedModel):
    name = models.CharField(max_length=256, verbose_name='Название заклинания')

    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Школа')
    focused_schools = models.ManyToManyField(FocusedSchool, verbose_name='Подшколы')

    source = models.CharField(max_length=256, blank=True, null=True, verbose_name='Источник')

    time = models.CharField(max_length=256, blank=True, null=True, verbose_name='Время сотворения')
    components = models.CharField(max_length=256, blank=True, null=True, verbose_name='Компоненты')
    distance = models.CharField(max_length=256, blank=True, null=True, verbose_name='Дистанция')
    effect = models.CharField(max_length=256, blank=True, null=True, verbose_name='Эффект')
    duration = models.CharField(max_length=256, blank=True, null=True, verbose_name='Длительносты')
    challenge = models.CharField(max_length=256, blank=True, null=True, verbose_name='Испытание')
    resist = models.CharField(max_length=256, blank=True, null=True, verbose_name='Устойчивость к магии')

    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    circles = models.ManyToManyField(CharacterClass, through=CircleToSpell, related_name='spell_circles',
                                     verbose_name='Круги')

    raw_data = models.TextField(blank=True, null=True, verbose_name='Дамп данных')

    class Meta:
        verbose_name = 'Заклинание'
        verbose_name_plural = 'Заклинания'


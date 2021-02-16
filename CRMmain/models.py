from django.db import models
from CRMcontacts.models import CRM_Contacts , CRM_Kompani 
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

STATUS = [
    ('ACT','В работе'),
    ('RES','Приостановлен'),
    ('OTC','Отказ'),
    ('ZVR','Завершен'),
]


PRITHOTKAZ = [
    ('ACT','Изменение приоритетов у клиента '),
    ('RES','Не договорились по сумме'),
    ('OTC','Не договорились по срокам поставки'),
    ('KLD', 'Клиент отказывается от общения'),
    ('VBK', 'Выбрали конкурента'),
]


# Продукт 
 

class CRM_Product(models.Model):
    # Название
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )


    objects = models.Manager()

    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.title


# Запрос ЛИД
class CRM_Lid_Zapros(models.Model):
    # Название
    title = models.CharField(
        max_length=200,
        
        default='',
    )
    kompani = models.ForeignKey(
        CRM_Kompani,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    contacts = models.ForeignKey(
        CRM_Contacts,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    users = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    opisanie = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    status= models.CharField(
        max_length=10,
        choices=STATUS,
        blank=True,
        null=True,
        default='ACT'
    )
    
    postavshik = models.CharField(
        'Поставщик',
        max_length=100,
        blank=True,
        null=True,
        default=''
    )
    otkaz_prith = models.TextField(
        'Комментарий',
        blank=True,
        null=True,
        default=''
    )
    otkaz_tip= models.CharField(
        'Причина отказа',
        max_length=10,
        choices=PRITHOTKAZ,
        default='ACT'
    )
    

    prov_na_sklade = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    prov_na_nom = models.FloatField(
        max_length=10,
        blank=True,
        null=True,
        default=1
    )

    
    
    objects = models.Manager()

    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.title


class CRM_Docs(models.Model):
    # Название
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    opisanie = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    filefild = models.FileField(
        upload_to='file',
    )
    projects = models.ForeignKey(
        CRM_Lid_Zapros,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    objects = models.Manager()

    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.title


class CRM_Histori(models.Model):
    # Название
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # Комент 
    komentrp = models.TextField(
        blank=True,
        null=True,
        default='',
    )

    projects = models.ForeignKey(
        CRM_Lid_Zapros,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    objects = models.Manager()

    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.title


class CRM_Positions(models.Model):
    
    proz_nadb = models.FloatField(
        max_length=10,
        blank=True,
        null=True,
        default=1
    )
    # Номер позиции 
    nomerpositin = models.CharField(
        'Номер позиции',
        max_length=100,
    )
    # Код ТПЛ
    kod_TPL = models.CharField(
        'Код ТПЛ',
        max_length=50,
        blank=True,
        null=True,
    )
    # ИЗДЕЛИЕ
    izdelie = models.CharField(
        'Изделие',
        max_length=10,
        choices=[
            ('SLIT','Слитки'),
            ('LIST','Листы'),
            ('ELIC','Электроды'),
            ('PLIT','Плиты'),
            ('LENT','Лента'),
            ('FOLG','Фольга'),
            ('PRYT','Прутки'),
            ('TRUB','Трубы'),
            ('PRIO','Припой'),
        ],
        blank=True,
        null=True,
    )
    # СПЛАВ
    splav = models.CharField(
        'Cплав',
        max_length=10,
        choices=[
            ('1','ВТ 1-00'),
            ('2','ВТ 1-0'),
            ('3','ОТ 4-0'),
            ('4','ОТ 4'),
            ('5','ОТ 4-1'),
            ('6','ВТ 3-1'),
            ('7','ВТ 5'),
            ('8','ВТ 5-1'),
            ('9','ВТ 6'),
            ('10','ВТ 6ч'),
            ('11','ВТ 6с'),
            ('12','ВТ 16'),
            ('13','ВТ 18'),
            ('14','ВТ 8,ВТ8-1'),
            ('15','ВТ 9'),
            ('16','ВТ 14'),
            ('17','ВТ 18у'),
            ('18','ВТ 20'),
            ('19','ВТ 22'),
            ('20','ВТ 23'),
            ('21','ВТ 25'),
            ('22','ВТ 25у'),
            ('23','ТС 6'),
            ('24','VST-2'),
        ],
        
    )
    # НАИМЕНОВАНИЕ ТПЛ
    naimenovanie_TPL = models.CharField(
        'Наименование ТПЛ',
        max_length=50,
        blank=True,
        null=True,
    )
    # ФОРМАИЗДЕЛИЯ
    izdelie_form = models.CharField(
        'Стандарты',
        max_length=100,
        choices=[
           ('SLIT','ОСТ 1-90218-76'),
            ('LIST','ТУ 1-5-093-77'),
            ('ELIC','ГОСТ 22178-76'),
        ],
        blank=True,
        null=True,
    )
    # ДОП К сплаву
    dop_k_splavy = models.CharField(
        'Доп к сплаву',
        max_length=100,
        blank=True,
        null=True,
    )
    # ШИФР
    # shifr = models.CharField(
    #     'Шифр',
    #     max_length=100,
    #     blank=True,
    #     null=True,
    # )
    # Класификация продуката
    # ДИАМЕТР ВНЕШНИЙ
    diametr_vne = models.FloatField(
        'Внешний',
        max_length=100,
        blank=True,
        null=True,
    )
    # ДИАМЕТР Внутненний
    diametr_vnut = models.FloatField(
        'Внутренний',
        max_length=100,
        blank=True,
        null=True,
    )
    # ДИАМЕТР Доп(+) внешний
    # ДИАМЕТР Доп(-) внешний
    # ДИАМЕТР Доп(+) внут
    # ДИАМЕТР Доп(-) внут
    # ДИАМЕТР Доп(+)%
    # ДИАМЕТР Доп(-)%
    # ТОЛЩИНА 
    tolshina = models.FloatField(
        'Толщина',
        max_length=100,
        blank=True,
        null=True,
    )
    # ТОЛЩИНА Доп(+)%
    # ТОЛЩИНА Доп(-)%
    # ТОЛЩИНА Код неполос
    # ТОЛЩИНА Призн
    # ШИРИНА Огранич. по ширине
    # ШИРИНА min
    shirina_min = models.FloatField(
        'min',
        max_length=100,
        blank=True,
        null=True,
    )
    # ШИРИНА max
    shirina_max = models.FloatField(
        'max',
        max_length=100,
        blank=True,
        null=True,
    )
    # ШИРИНА Доп(+)
    # ШИРИНА Доп(-)
    # ШИРИНА Призн
    # ТОЛЩИНА И ШИРИНА Примичание к размеру 
    # ДЛИННА Огранич. по длинне
    # ДЛИННА min
    dlinna_min = models.FloatField(
        'min',
        max_length=100,
        blank=True,
        null=True,
    )
    # ДЛИННА max
    dlinna_max = models.FloatField(
        'max',
        max_length=100,
        blank=True,
        null=True,
    )
    # ДЛИННА Доп(+)
    # ДЛИННА Доп(-)
    # ДЛИННА Призн
    # КОЛЛИЧЕСТВО Кол-во
    kollitsh = models.FloatField(
        'Кол-во',
        max_length=100,
        blank=True,
        null=True,
    )
    # КОЛЛИЧЕСТВО Вес 1 шт.
    # КОЛЛИЧЕСТВО Вес, кг
    kollitsh_kg = models.FloatField(
        'Вес, кг',
        max_length=100,
        blank=True,
        null=True,
    )
    # КОЛЛИЧЕСТВО Пог.м
    # КОЛЛИЧЕСТВО Ед. Изм
    # КОЛЛИЧЕСТВО Допуск(+)
    # КОЛЛИЧЕСТВО Допуск(-)
    # КОЛЛИЧЕСТВО Размер Дюйм
    # 
    # 
    # 
    # 
    # Дополнительные требования
    dop_trebovaniy = models.TextField(
        'Дополнительные требования',
        blank=True,
        null=True,
        default=''
    )
    # Состояние поверхности
    sostoyniy_pov = models.TextField(
        'Состояние поверхности',
        blank=True,
        null=True,
        default=''
    )     
    # Метод плавления
    metod_plav = models.TextField(
        'Метод плавления',
        blank=True,
        null=True,
        default=''
    ) 
    # Требования по УЗ контролю
    trebovan_US = models.TextField(
        'Требования по УЗ контролю',
        blank=True,
        null=True,
        default=''
    ) 
    # Требования к макроструктуре
    trebov_k_makr = models.TextField(
        'Требования к макроструктуре',
        blank=True,
        null=True,
        default=''
    ) 
    # Определение микроструктуры
    opred_k_mukr = models.TextField(
        'Определение микроструктуры',
        blank=True,
        null=True,
        default=''
    ) 
    # Маркировка
    markirov = models.TextField(
        'Маркировка',
        blank=True,
        null=True,
        default=''
    ) 
    # Требования к оформлению сертификатов
    trebov_k_of_sert = models.TextField(
        'Требования к оформлению сертификатов',
        blank=True,
        null=True,
        default=''
    ) 
    # 
    # Процент (+/-5%)
    # 
    #  

    projects = models.ForeignKey(
        CRM_Lid_Zapros,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    objects = models.Manager()

    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.projects


class CRM_P_Postavka(models.Model):
    status = models.CharField(
        'Статус',
        max_length=100,
        blank=True,
        null=True,
    )
    #График отгрузки
    data = models.DateField(
        #data = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    #График сдачи
    data_sdad = models.DateField(
        #data = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    ves = models.FloatField(
        'Вес',
        max_length=100,
        blank=True,
        null=True,
    )
    kollitsh = models.FloatField(
        'Кол-во',
        max_length=100,
        blank=True,
        null=True,
    )
    posi = models.ForeignKey(
        CRM_Positions,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    objects = models.Manager()

    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.status
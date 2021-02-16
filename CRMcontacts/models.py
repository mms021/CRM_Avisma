from django.db import models
TIP = [
    ('pr','Партнер'),
    ('ps','Поставщик'),
    ('kl','Клиент'),

]

OTRSL = [
    ('AVI5','Обрабатывающие производства'),
    ('PRE4','Оптовая и розничная торговля'),
    ('PRE3','Добыча полезных ископаемых'),
    ('PRE2','Сельское хозяйство, охота и лесное хозяйство'),
    ('PRE1','Финансовая деятельность'),
    ('PRE9','Государственное управление и обеспечение военной безопасности'),
    ('PRE8','Строительство'),
    ('PRE7','Транспорт и связь'),
    ('НДА6','Производство и распределение электроэнергии,газа и воды'),
    ('НДА5','Образование'),
    ('НДА4','Гостиницы и рестораны'),
    ('НДА3','Здравоохранение и предоставление социальных услуг'),
    ('НДА2','Рыболовство, рыбоводство'),
    ('НДА1','Предоставление услуг по ведению домашнего хозяйства'),




]


class CRM_Kompani(models.Model):
    # Название
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # Наименовение на англ 
    title_eng = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # Код WMS
    kod_WMS = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # Код ERP
    kod_ERP = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # Тип
    tip =  models.CharField(
        max_length=10,
        choices=TIP,
        blank=True,
        null=True,
    )
    # Место государственной регистрации
    registr =  models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='',
    )
    # Сфера деятельности
    sfera =  models.CharField(
        max_length=10,
        choices=OTRSL,
        blank=True,
        null=True,
    )
    # Сайт
    saits =  models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='',
    )
    # Телефон
    telefon =  models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='',
    )
    # Описане 
    opisanie = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # страна
    contru = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # город
    siti = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # Адрес
    adress = models.CharField(
        "Адрес",
        max_length=300,
        blank=True,
        null=True,
        default='',
    )
    # почта 
    email = models.EmailField(
        blank=True,
        null=True,
        default='',
    ) 
    # ПЛАТЕЖНЫЕ РЕКВЕЗИТЫ
    # ОГРН
    ogrn = models.CharField(
        'ОГРН',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # Дата записи ОГРН ДАТА
    data_ogrn = models.DateField(
        "Дата записи ОГРН",
        blank=True,
        null=True,
    )
    # ИНН
    inn = models.CharField(
        'ИНН',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # ОКАТО
    okato =models.CharField(
        'ОКАТО',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # КПП
    kpp =models.CharField(
        'КПП',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # ОКВЭД
    okved =models.CharField(
        'ОКВЭД',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # ОКПО
    okpo =models.CharField(
        'ОКПО',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # Банк получателя
    bank_title = models.CharField(
        'Банк получателя',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # БИК
    big =models.CharField(
        'БИК',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # Корреспондентский счет
    ks =models.CharField(
        'Корреспондентский счет',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # Расчетный счет
    ps =models.CharField(
        'Расчетный счет',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # ФИО Руководителя:
    fio_Ruc =models.CharField(
        'ФИО Руководителя',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # ФИО Бухгалтера
    fio_Buh =models.CharField(
        'ФИО Бухгалтера',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # Действует на основании:
    deust = models.CharField(
        'Действует на основании',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # Документ, подтверждающий наличие полномочий:
    doc_polm = models.CharField(
        'Документ, подтверждающий наличие полномочий',
        max_length=250,
        blank=True,
        null=True,
        default='',
    )
    # Срок полномочий, до: ДАТА
    srok_dok = models.DateField(
        "Срок полномочий, до:",
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



# Create your models here.
class CRM_Contacts(models.Model):
    # ФИО
    title = models.CharField(
        max_length=200,
        default='',
    )
    # Должность 
    doljnost = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # номер телефона
    tel_nomber = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    # Почта
    email = models.EmailField(
        blank=True,
        null=True,
        default='',
    )   
    # Компани 
    compani = models.ForeignKey(
        CRM_Kompani,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    # Пол 
    sex = models.CharField(
        'Пол',
        max_length=5,
        choices=[('M','Мужской'),('F',"Женский")],
        blank=True,
        null=True,
        default='',
    )
    #язык
    lang = models.CharField(
        "Язык обращения",
        max_length=5,
        choices=[('E','English'),('R',"Русский")],
        blank=True,
        null=True,
        default='',
    )

    
    birthday = models.DateField(
        "Дата рождения",
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


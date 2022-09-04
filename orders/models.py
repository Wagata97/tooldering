from django.db.models import Model, CharField, DecimalField, ForeignKey, DO_NOTHING

CURRENCY = (
    ('pln', 'PLN'),
    ('eur', 'EUR'),
)

CONFRIM = (
    ('tak', 'TAK'),
    ('nie', 'NIE')
)


class Associates(Model):
    name = CharField(max_length=100)
    password = CharField(max_length=50)   #tu bedą forms.py

    def __str__(self):
        return self.name


class Orders(Model):
    associate = ForeignKey(Associates, on_delete=DO_NOTHING)
    product_num = CharField(max_length=20)
    product = CharField(max_length=100)
    price = DecimalField(max_digits=8, decimal_places=2)
    currency = CharField(choices=CURRENCY, max_length=10, default='PLN')
    status = CharField(choices=CONFRIM, max_length=3, default='nie')









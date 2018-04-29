import moneyed
import datetime
import random
import string
from django.utils.text import slugify


def sme_choices():
    """
        Helper function to retrieve all listed choices for the SME model
    """
    money_currencies = moneyed.CURRENCIES
    CURRENCIES = [(cur.code, cur.name + " (" + cur.code + ")") for cur in list(money_currencies.values())]
    LEGAL_STRUCT = (
        ('BC', 'Benefit Corporation'),
        ('CO', 'Co-op'),
        ('CR', 'Corporation'),
        ('LL', 'Limited Liability Company'),
        ('NP', 'Non-Profit/Non-Governmental Organization'),
        ('PT', 'Partnership'),
        ('SP', 'Sole-Proprietorship'),
        ('OT', 'Other'),
    )
    OWNERSHIP = (
        ('WO', 'Woman Owned'),
        ('YO', 'Youth Owned'),
        ('LO', 'Local Owned'),
        ('IO', 'International Owned'),
        ('OT', 'Other'),
    )
    SECTOR = (
        ('Agriculture', (
            ('fruit', 'Fruit'),
            ('coffee', 'Coffee'),
            ('nuts', 'Nuts'),
            ('tea', 'Tea'),
            ('cocoa', 'Cocoa'),
            ('sugar', 'Sugar'),
            ('forest', 'Forest'),
            ('bamboo', 'Bamboo'),
            ('vegetables', 'Vegetables'),
            ('meat', 'Meat'),
            ('fish', 'Fish'),
            ('shea', 'Shea'),
            ('moringa', 'Moringa'))
         ),
        ('Energy & Water', (
            ('stoves', 'Stoves'),
            ('solar', 'Solar'),
            ('lamps', 'Lamp/Kits'),
            ('bio', 'Bio/Gar'),
            ('wind', 'Wind/Hydro'),
            ('mini-grid', 'Mini-Grid'),
            ('water-filt', 'Water filtration'),
            ('briquettes', 'Briquettes/Pellets'))
         ),
        ('Waste Management', (
            ('recycling', 'Recycling'),
            ('sewerage', 'Sewerage'),
            ('collection', 'Collection'))
         ),
        ('Health & Social', (
            ('health', 'Health Foods/Products'),
            ('excercise', 'Excercise Items'),
            ('medical', 'Medical Facilities/Treatment'),
            ('care', 'Care Provision'))
         ),
        ('Tourism', (
            ('conservation', 'Conservation'),
            ('community', 'Community Engagement'))
         ),
        ('Craft', (
            ('leather', 'Leather/Textiles/Plant Fibres'),
            ('wood', 'Wood'),
            ('cosmetics', 'Cosmetics'),
            ('accessories', 'Accessories'),
            ('household', 'Household Items'),
            ('jewellery', 'Jewellery'),
            ('coffins', 'Coffins'),
            ('fashion', 'Fashion'))
         ),
        ('Finance', (
            ('provision', 'Finance Provision to Individuals'),
            ('micro-leasing', 'Micro-leasing'))
         ),
        ('Education', (
            ('low', 'Low Fee Private Schooling'),
            ('training', 'Vocational Training'))
         ),
        ('Construction & Manufacturing', (
            ('building', 'House Building'),
            ('roads', 'Roads'),
            ('manufacturing', 'Technical Manufacturing'))
         ),
        ('Accomodation & Food Services', (
            ('hotels', 'Hotels'),
            ('restaurants', 'Restaurants'),
            ('catering', 'Catering'),
            ('bakery', 'Bakery'),
            ('delivery', 'Food Delivery'))
         ),
        ('Professional & Support Services', (
            ('law', 'Law'),
            ('pr', 'PR'),
            ('real', 'Real Estate'))
         ),
        ('Other', (
            ('entertainment', 'Entertainment & Arts'),
            ('tech', 'Technology'))
         )
    )
    YEAR_CHOICES = []
    for r in range(1970, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    return LEGAL_STRUCT, OWNERSHIP, YEAR_CHOICES, CURRENCIES, SECTOR


DONT_USE = ['create']
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.get_user().email)
    if slug in DONT_USE:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def add_filter_choices(context, user):
    LEGAL_STRUCT, OWNERSHIP, YEAR_CHOICES, CURRENCIES, SECTOR = sme_choices()
    context['legal_choices'] = LEGAL_STRUCT
    context['ownership'] = OWNERSHIP
    context['currencies'] = CURRENCIES
    context['sectors'] = SECTOR
    context['years'] = YEAR_CHOICES
    return context

def filter_search(self, qs):
    legal = self.request.GET.get('legal')
    owner = self.request.GET.get('owner')
    currency = self.request.GET.get('currency')
    sector = self.request.GET.get('sector')
    year = self.request.GET.get('year')
    country = self.request.GET.get('country')
    if legal:
        qs = qs.filter(legal_struct__iexact=legal)
    if owner:
        qs = qs.filter(ownership__iexact=owner)
    if currency:
        qs = qs.filter(currency__iexact=currency)
    if sector:
        qs = qs.filter(sector__iexact=sector)
    if year:
        qs = qs.filter(year__iexact=year)
    if country:
        for q in qs:
            if q.get_country().name != country:
                qs = qs.exclude(user=q.get_user())
    return qs

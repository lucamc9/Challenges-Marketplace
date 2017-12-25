from djmoney.models.fields import CurrencyField
import moneyed
import datetime

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

from django.contrib import admin
import inflect
from lettings.models import Letting
from lettings.models import Address
#from profiles.models import Profile
#from .models import Letting
#from .models import Address
from .models import Profile

admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)

"""
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'zip_code')
"""
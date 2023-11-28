from django.contrib import admin

# Register your models here.
from AppHse.models import analisis_De_Riesgo, permiso_de_trabajo, trabajo_altura

admin.site.register(trabajo_altura)
admin.site.register(permiso_de_trabajo)


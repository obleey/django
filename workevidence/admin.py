from django.contrib import admin
from .models import WorkEvidence,Worker
from reversion.admin import VersionAdmin

admin.site.site_header="Worker admin"
admin.site.site_title="Worker Admin Adreas"
admin.site.index_title="Welcome to Worker Admin"
@admin.register(Worker)
class ClientModelAdmin(VersionAdmin):
      pass

admin.site.register(WorkEvidence)


from copy import deepcopy
from django.contrib import admin

from mezzanine.forms.admin import FormAdmin
from mezzanine.forms.models import Form
from mezzanine.galleries.admin import GalleryAdmin
from mezzanine.galleries.models import Gallery
from mezzanine.pages.admin import PageAdmin, LinkAdmin
from mezzanine.pages.models import RichTextPage, Link


page_fieldsets = deepcopy(PageAdmin.fieldsets)
page_fieldsets[0][1]["fields"].insert(1, "in_opd")
PageAdmin.fieldsets = page_fieldsets
GalleryAdmin.fieldsets = page_fieldsets

link_fieldsets = deepcopy(LinkAdmin.fieldsets)
link_fieldsets[0][1]["fields"].insert(1, "in_opd")
LinkAdmin.fieldsets = link_fieldsets

form_fieldsets = deepcopy(FormAdmin.fieldsets)
form_fieldsets[0][1]["fields"].insert(1, "in_opd")
FormAdmin.fieldsets = form_fieldsets

admin.site.unregister(Form)
admin.site.register(Form, FormAdmin)
admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)
admin.site.unregister(RichTextPage)
admin.site.register(RichTextPage, PageAdmin)
admin.site.unregister(Link)
admin.site.register(Link, LinkAdmin)

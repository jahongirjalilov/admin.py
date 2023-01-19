from django.contrib import admin, messages
from django.contrib.auth.models import Group, User
from django.forms import ModelForm
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin

from app.models import Category, Product
from django.contrib.admin import AdminSite, ModelAdmin

# admin.site.register(Category)
# admin.site.register(Product)

admin.site.site_header = "Panda"
admin.site.site_title = "Admin"
admin.site.index_title = "H_O_M_E"

# ---------------------------------------------------------------------

class ProductAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"
product_admin_site = ProductAdminSite(name='product_admin')
product_admin_site.register(Product)

# -------------------------------------------------------------------

admin.site.unregister(Group)
# admin.site.unregister(User)

# --------------------------------------------------------------------
class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Product image'
        self.fields['title'].help_text = 'Product title'
        self.fields['text'].help_text = 'Product description'
        self.fields['price'].help_text = 'Product price'
        self.fields['category'].help_text = 'Product category'

    class Meta:
        model = Product
        exclude = ()
# --------------------------------------------------------------------
MAX_OBJECTS = 5
@admin.register(Product)
class ProductAdmin(ModelAdmin):
    form = ProductForm
    list_display = ('image_tag', 'title','price','text')  # table kurinishida chiqarish
    list_filter = ('title', 'price', 'text')              # filter qilish
    list_per_page = 5                                     # pagenation qilish
    """readonly_fields --> da berilgan fieldlar adminda ishlamaydi"""
    # readonly_fields = ['title', 'price']
    search_fields = ('title',)                            # search qilish
    ordering = ('title', )                                # order by
    autocomplete_fields = ['category',]                   # Category buyicha search qilish

    def image_tag(self, obj):
        return format_html('<img src="{}" width= "70"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return True
        return super().has_add_permission(request)

"""    Berilgan funksiyalardagi requestlar django adminda ishlamaydi

def has_module_permission(self, request):
    return False

def has_delete_permission(self, request, obj=None):
if obj != None and request.POST.get('action') == 'delete selected':
    messages.add_message(request, messages.ERROR,
                        'Rostdan ham  o`chirmoqchimisiz ? ')
return True

def has_view_permission(self, request, obj=None):
    return False

def has_change_permission(self, request, obj=None):
    return False

"""

# --------------------------------------------------------------------

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

    # def children_display(self, obj):
    #     return ", ".join([
    #         child.name for child in obj.children.all()
    #     ])
    # children_display.short_description = "Children"

# --------------------------------------------------------------------
"""Product show/hide"""

# @admin.register(Product)
# class ProductAdmin(ModelAdmin):
#     fieldsets = (
#         ('1- qism', {
#             'fields': ('title','price', 'text'),
#             'description': 'Product model',
#             'classes': ('collapse', )
#         }),
#         ('2- qism', {
#             'fields': ('category', ),
#             'description': 'Product model'
#         }),
#     )

#--------------------------------------------------------------------

"""Yozuvlarimizni chiroyli pechatlab beradi"""

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


# admin.site.register(Product, SummerAdmin)

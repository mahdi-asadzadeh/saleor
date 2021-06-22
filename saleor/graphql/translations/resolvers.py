from ...attribute import models as attribute_models
from ...core.tracing import traced_resolver
from ...discount import models as discount_models
from ...menu import models as menu_models
from ...page import models as page_models
from ...product import models as product_models
from ...shipping import models as shipping_models
from ...site import models as site_models
from . import dataloaders


def resolve_translation(instance, info, language_code):
    """Get translation object from instance based on language code."""
    loader = None
    if isinstance(instance, attribute_models.Attribute):
        loader = dataloaders.AttributeTranslationByIdAndLanguageCodeLoader
    elif isinstance(instance, attribute_models.AttributeValue):
        loader = dataloaders.AttributeValueTranslationByIdAndLanguageCodeLoader
    elif isinstance(instance, product_models.Category):
        loader = dataloaders.CategoryTranslationByIdAndLanguageCodeLoader
    elif isinstance(instance, product_models.Collection):
        loader = dataloaders.CollectionTranslationByIdAndLanguageCodeLoader
    elif isinstance(instance, menu_models.MenuItem):
        loader = dataloaders.MenuItemTranslationByIdAndLanguageCodeLoader
    elif isinstance(instance, page_models.Page):
        loader = dataloaders.PageTranslationByIdAndLanguageCodeLoader
    elif isinstance(instance, product_models.Product):
        loader = dataloaders.ProductTranslationByIdAndLanguageCodeLoader
    elif isinstance(instance, product_models.ProductVariant):
        loader = dataloaders.ProductVariantTranslationByIdAndLanguageCodeLoader
    elif isinstance(instance, discount_models.Sale):
        loader = dataloaders.SaleTranslationByIdAndLanguageCodeLoader
    elif isinstance(instance, shipping_models.ShippingMethod):
        loader = dataloaders.ShippingMethodTranslationByIdAndLanguageCodeLoader
    elif isinstance(instance, site_models.SiteSettings):
        loader = dataloaders.SiteSettingsTranslationByIdAndLanguageCodeLoader
    elif isinstance(instance, discount_models.Voucher):
        loader = dataloaders.VoucherTranslationByIdAndLanguageCodeLoader
    if loader:
        return loader(info.context).load((instance.pk, language_code))
    return None


@traced_resolver
def resolve_shipping_methods(info):
    return shipping_models.ShippingMethod.objects.all()


@traced_resolver
def resolve_attribute_values(info):
    return attribute_models.AttributeValue.objects.all()


@traced_resolver
def resolve_products(_info):
    return product_models.Product.objects.all()


@traced_resolver
def resolve_product_variants(_info):
    return product_models.ProductVariant.objects.all()


@traced_resolver
def resolve_sales(_info):
    return discount_models.Sale.objects.all()


@traced_resolver
def resolve_vouchers(_info):
    return discount_models.Voucher.objects.all()


@traced_resolver
def resolve_collections(_info):
    return product_models.Collection.objects.all()

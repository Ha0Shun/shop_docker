from django.db import models
from core.helpers import upload_handle
# Create your models here.
class Product(models.Model):
    '''
    商品模型
    '''
    name = models.CharField('商品名稱', max_length=50)
    description = models.TextField('商品描述', max_length=500, null=True, blank=True)
    price = models.PositiveIntegerField('商品價格', default=0)
    created = models.DateTimeField('建立日期', auto_now_add=True)
    modified = models.DateTimeField('修改日期', auto_now=True)
    category = models.ForeignKey(
        'products.ProductCategory', blank=True, null=True, 
        on_delete=models.RESTRICT, verbose_name='商品分類', related_name='product_set'
    ) # 新增 category 欄位
    image = models.ImageField("圖片", null=True, blank=True, upload_to='core_helpers.upload_handle')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
        ordering = ['-created']

    def __str__(self):
        return f'{self.name}'
    
    

class ProductCategory(models.Model):
    '''
    商品分類模型
    '''
    name = models.CharField('商品分類名稱', max_length=50)
    description = models.TextField('商品分類描述', max_length=500, null=True, blank=True)
    created = models.DateTimeField('建立日期', auto_now_add=True)
    modified = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        verbose_name = '商品分類'
        verbose_name_plural = '商品分類'
        ordering = ['-created']

    def __str__(self):
        return f'{self.name}'
    
class ProductImage(models.Model):
    name = models.CharField('商品圖片說明', max_length=50)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='product_image_set')
    image = models.ImageField("圖片", null=True, blank=True, upload_to=upload_handle)
    order = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name = '商品圖片'
        verbose_name_plural = '商品圖片'
        ordering = ['order']

    def __str__(self):
        return f'{self.name}'


class ProductOption(models.Model):
    product = models.ForeignKey(Product, related_name='options', on_delete=models.CASCADE)
    size = models.CharField(max_length=50)  # 例如，衣服尺寸
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 每個尺寸的價格

    
class RelationalProduct(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name='商品名稱')
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    number = models.IntegerField('數量', default=1)
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    
    @property
    def name(self):
        return self.product.name
    

    @property
    def price(self):
        return self.product.price

    def __str__(self):
        return ""



# 新增的圖片模型類別
class frontpageImage(models.Model):
    '''
    首頁圖片模型
    '''
    CATEGORY_CHOICES = [
        ('carousel', '輪播圖片'),
        ('banner', '橫幅圖片'),
        ('thumbnail', '縮略圖'),
        ('other', '其他'),
    ]

    name = models.CharField('圖片名稱', max_length=50)
    image = models.ImageField("圖片", upload_to=upload_handle)
    category = models.CharField('圖片分類', max_length=20, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField('圖片描述', max_length=500, null=True, blank=True)
    created = models.DateTimeField('建立日期', auto_now_add=True)
    modified = models.DateTimeField('修改日期', auto_now=True)
    is_active = models.BooleanField('是否啟用', default=True)

    class Meta:
        verbose_name = '首頁圖片'
        verbose_name_plural = '首頁圖片'
        ordering = ['-created']

    def __str__(self):
        return self.name
    

class GeneralImage(models.Model):
    '''
    通用圖片模型
    '''
    name = models.CharField('圖片名稱', max_length=50)
    image = models.ImageField("圖片", upload_to=upload_handle)
    category = models.ForeignKey(
        'products.ProductCategory', blank=True, null=True, 
        on_delete=models.RESTRICT, verbose_name='品牌分類', related_name='Image_set'
    )
    description = models.TextField('圖片描述', max_length=500, null=True, blank=True)
    created = models.DateTimeField('建立日期', auto_now_add=True)
    modified = models.DateTimeField('修改日期', auto_now=True)
    is_active = models.BooleanField('是否啟用', default=True)

    class Meta:
        verbose_name = '通用圖片'
        verbose_name_plural = '通用圖片'
        ordering = ['-created']

    def __str__(self):
        return self.name
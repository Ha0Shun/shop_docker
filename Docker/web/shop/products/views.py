from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from products.models import Product,ProductCategory,ProductOption, frontpageImage, GeneralImage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from django.db.models import Min
from django.core.paginator import Paginator
from django.utils.html import format_html

class HomeView(TemplateView):
    model = Product
    template_name = "products/home.html"
    context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        # 取得分類 ID，若未提供則為 None
        category_id = request.GET.get('category')

        # 篩選商品，並透過 `annotate` 找到最低價格
        products = Product.objects.all().annotate(
            lowest_price=Min('options__price')  # 使用 ORM 聚合查找最低價格
        )
        if category_id:
            products = products.filter(category_id=category_id)

        # 商品分類分組
        product_categories = ProductCategory.objects.all()

        # 分類顯示商品數量限制為最多 4 個
        category_items = {}
        for category in product_categories:
            category_items[category] = products.filter(category=category)[:4]  # 每個分類最多顯示四個商品

        # 取得輪播圖片，僅取啟用的輪播圖片
        carousel_images = frontpageImage.objects.filter(category='carousel', is_active=True)

        # 上下文資料
        context = self.get_context_data(**kwargs)
        context.update({
            'items': products,
            'category_items': category_items,  # 分組後的商品
            'categories': product_categories,
            'carousel_images': carousel_images,  # 傳遞輪播圖片
        })

        return self.render_to_response(context)
    
    
class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'items'

    def get_queryset(self):
        category_id = self.request.GET.get('category')
        products = Product.objects.all()

        if category_id:
            products = products.filter(category_id=category_id)

        # 使用 annotate 計算最低價格
        products = products.annotate(
            lowest_price=Min('options__price')
        )
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 獲取所有商品分類並進行分組
        all_categories = ProductCategory.objects.all()
        context['left_product_categories'] = all_categories[:2]
        context['right_product_category'] = all_categories[2:3].first()
        context['categories'] = all_categories

        # 獲取所選分類的輪播圖片
        category_id = self.request.GET.get('category')
        if category_id and category_id.isdigit():
            category_id = int(category_id)
            category_images = GeneralImage.objects.filter(is_active=True, category_id=category_id)
            uncategorized_images = GeneralImage.objects.filter(is_active=True, category__isnull=True)
            context['carousel_images'] = list(category_images) + list(uncategorized_images)
            context['current_category'] = ProductCategory.objects.get(id=category_id)
        else:
            context['carousel_images'] = frontpageImage.objects.filter(category='carousel', is_active=True)
            context['current_category'] = None

        # 分頁處理
        product_list = self.get_queryset()
        paginator = Paginator(product_list, 9)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)

        return context




    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        # 先取得父類別的 context
        context = super().get_context_data(**kwargs)
        # 新增 categories 到 context
        context['categories'] = ProductCategory.objects.all()

        # 格式化描述內容，將換行符轉為 <br>，並加入到 item.description
        item = context['item']
        if item.description:
            item.description = format_html(item.description.replace("\n", "<br>"))
        
        return context

def search_orders(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        # 在這裡通過搜尋資料庫，獲取相應的訂單數據，這裡僅為示例
        # 假設你已經定義了一個 Order 模型
        # orders = Order.objects.filter(phone=phone, email=email)

        # 為了示例，這裡直接返回一些假數據
        orders = [{'id': 1, 'product': 'Product A', 'quantity': 2}, {'id': 2, 'product': 'Product B', 'quantity': 1}]

        return JsonResponse({'orders': orders})
    return JsonResponse({'error': 'Invalid request method'})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'item': product,
    }
    return render(request, 'products/detail.html', context)
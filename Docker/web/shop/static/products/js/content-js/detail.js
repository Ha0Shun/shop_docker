document.getElementById('toggleButton').addEventListener('click', function() {
    var content = document.getElementById('collapseContent');
    var buttonText = document.getElementById('toggleButtonText');        
    if (content.style.maxHeight === '200px') {
        content.style.maxHeight = 'none';  
        buttonText.textContent = '▲ 收起';  
    } else {
        content.style.maxHeight = '200px';  
        buttonText.textContent = '▼ 展開';  
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.getElementById('carouselExample');
    const thumbnails = document.querySelectorAll('.thumbnail');
    
    carousel.addEventListener('slid.bs.carousel', function (event) {            
        const activeIndex = event.to;            
        thumbnails.forEach(thumb => thumb.classList.remove('border-primary'));            
        thumbnails[activeIndex].classList.add('border-primary');
    });        
    thumbnails[0].classList.add('border-primary');
});    
document.getElementById('increment').addEventListener('click', function() {
    var quantityInput = document.getElementById('product-quantity');
    quantityInput.value = parseInt(quantityInput.value) + 1;
    updatePrice();
});

document.getElementById('decrement').addEventListener('click', function() {
    var quantityInput = document.getElementById('product-quantity');
    if (parseInt(quantityInput.value) > 1) {
        quantityInput.value = parseInt(quantityInput.value) - 1;
        updatePrice();
    }
});
    // 默认显示基础价格
// 默认显示基础价格
var defaultPrice = parseFloat(document.querySelector('input[name="options"]:checked').getAttribute('data-price'));
document.getElementById('product-price').innerText = '$' + defaultPrice;

// 更新尺寸选择时的价格显示
document.querySelectorAll('input[name="options"]').forEach(function(option) {
    option.addEventListener('change', function() {
        updatePrice();
    });
});
// 更新價格的函數
function updatePrice() {
    var selectedOption = document.querySelector('input[name="options"]:checked');
    if (!selectedOption) {
        return; // 如果沒有選擇尺寸，什麼也不做
    }
    var price = parseFloat(selectedOption.getAttribute('data-price')); // 單價
    var quantity = parseInt(document.getElementById('product-quantity').value); // 數量
    var totalPrice = (price * quantity); // 總價
    document.getElementById('product-price').innerText = '$' + totalPrice;
}


// 獲取滾動容器和按鈕
const thumbnails = document.getElementById('thumbnails');
const scrollLeft = document.getElementById('scrollLeft');
const scrollRight = document.getElementById('scrollRight');

// 左箭頭按下事件
scrollLeft.addEventListener('click', () => {
    thumbnails.scrollBy({ left: -100, behavior: 'smooth' });
});

// 右箭頭按下事件
scrollRight.addEventListener('click', () => {
    thumbnails.scrollBy({ left: 100, behavior: 'smooth' });
});


function addToCart(productId) {
    // 获取尺寸ID
    var selectedOption = document.querySelector('input[name="options"]:checked');
    if (!selectedOption) {
        alert('請選擇一個尺寸。');
        return;
    }
    var sizeId = selectedOption.value;

    // 获取数量
    var quantityInput = document.getElementById('product-quantity');
    var quantity = parseInt(quantityInput.value);
    if (isNaN(quantity) || quantity < 1) {
        alert('請輸入有效的數量。');
        return;
    }

    // 构建URL
    var url = "/orders/add_cart/" + productId + "/" + sizeId + "/" + quantity + "/";

    // 使用Ajax发送请求
    getAjax(url, '已加入購物車', 'false');
}    
function showImageModal(imageUrl, index) {
    // 更新主圖片
    const modalImage = document.getElementById('modalImage');
    modalImage.src = imageUrl;

    // 顯示 Modal
    const imageModal = new bootstrap.Modal(document.getElementById('imageModal'));
    imageModal.show();

    // 等待 Modal 顯示後，再選擇並高亮當前的縮略圖
    const thumbnails = document.querySelectorAll('.modal-thumbnail');
    
    // 先移除所有縮略圖的高亮
    thumbnails.forEach(thumb => thumb.classList.remove('border-primary'));

    // 根據圖片 URL 找到對應的縮略圖並添加高亮
    const selectedThumbnail = Array.from(thumbnails).find(thumb => thumb.src.includes(imageUrl));
    if (selectedThumbnail) {
        selectedThumbnail.classList.add('border-primary'); // 高亮當前縮略圖
    }
}

function updateModalImage(imageUrl) {
    // 更新主圖片
    const modalImage = document.getElementById('modalImage');
    modalImage.src = imageUrl;

    // 高亮對應的縮略圖
    const thumbnails = document.querySelectorAll('.modal-thumbnail');
    thumbnails.forEach(thumb => thumb.classList.remove('border-primary'));

    // 找到對應的縮略圖並添加高亮邊框
    const selectedThumbnail = Array.from(thumbnails).find(thumb => thumb.src.includes(imageUrl));
    if (selectedThumbnail) {
        selectedThumbnail.classList.add('border-primary');
    }
}
document.addEventListener('DOMContentLoaded', function() {
    const priceElements = document.querySelectorAll('.product-price, #total-price');

    priceElements.forEach(function(priceElement) {
        let priceText = priceElement.innerText.trim();

        // 只處理價格部分，確保不影響其他內容（如 "1 x $100"）
        let priceMatch = priceText.match(/\$(\d+(\.\d+)?)/);

        if (priceMatch) {
            let price = parseFloat(priceMatch[1]); // 提取價格
            price = formatPrice(price); // 格式化價格

            // 替換舊價格部分為新價格
            priceText = priceText.replace(priceMatch[0], `$${price}`);
            priceElement.innerText = priceText;
        }
    });
});
// 获取指定名称的 cookie 值
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  // 更新數量並更新購物車
    function updateQuantityAndUpdateCart(productoption_id, change) {
        var quantityElement = document.querySelector('#quantity_' + productoption_id);
        var currentQuantity = parseInt(quantityElement.innerText);  // 取得當前顯示的數量
        var newQuantity = currentQuantity + change;
    
        if (newQuantity >= 1) {
            quantityElement.innerText = newQuantity;  // 更新顯示的數量
    
            // 使用 GET 請求來更新購物車
            var url = '/orders/update-cart/' + productoption_id + '/' + newQuantity + '/';
            fetch(url, {
                method: 'GET',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 200) {
                    // 如果更新成功，更新頁面（例如更新總金額等）
                    location.reload();  // 重新載入頁面
                } else {
                    alert('更新購物車失敗: ' + data.message);
                }
            })
            .catch(error => {
                console.error('錯誤:', error);
                alert('更新購物車時出現錯誤');
            });
        }
    }

  // 更新購物車視圖
  function updateCartView(cart) {
    var totalAmount = 0;
    // 遍歷每個商品並更新頁面元素
    Object.keys(cart).forEach(function(productoption_id) {
      var item = cart[productoption_id];
      var itemTotal = item.count * item.price;
      totalAmount += itemTotal;

      // 更新數量
      document.querySelector('#quantity_' + productoption_id).value = item.count;

      // 更新每個商品的總價
      document.querySelector('#total_' + productoption_id).innerText = "$" + itemTotal.toFixed(2);
    });

    // 更新總金額
    document.querySelector('#total-amount').innerText = "$" + totalAmount.toFixed(2);
  }
    // 移除購物車商品並檢查重定向
    function removeFromCartAndCheckRedirect(url, successMessage, reloadPage) {
        fetch(url, {
            method: 'GET',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 200) {
                alert(successMessage);  // 顯示成功訊息
                if (reloadPage === 'true') {
                    location.reload();  // 重新載入頁面
                }
            } else {
                alert('移除商品失敗: ' + data.message);
            }
        })
        .catch(error => {
            console.error('錯誤:', error);
            alert('移除商品時出現錯誤');
        });
    }
    
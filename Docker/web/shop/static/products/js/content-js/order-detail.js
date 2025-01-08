document.getElementById('toggleButton').addEventListener('click', function() {
    var table = document.getElementById('orderTable');
    var arrowIcon = document.getElementById('arrowIcon');
    
    // 統一檢查 table 的初始顯示狀態
    if (table.style.display === 'none') {
        table.style.display = 'table';  // 顯示表格
        arrowIcon.classList.remove('fa-chevron-down');  // 移除向下箭頭
        arrowIcon.classList.add('fa-chevron-up');       // 顯示向上箭頭            
    } else {
        table.style.display = 'none';  // 隱藏表格
        arrowIcon.classList.remove('fa-chevron-up');  // 移除向上箭頭
        arrowIcon.classList.add('fa-chevron-down');   // 顯示向下箭頭
    }
});

// 確保初始狀態正確，防止瀏覽器的默認樣式干擾
document.addEventListener('DOMContentLoaded', function() {
    var table = document.getElementById('orderTable');
    var arrowIcon = document.getElementById('arrowIcon');

    table.style.display = 'table';  // 初始展開
    arrowIcon.classList.remove('fa-chevron-down');  // 確保箭頭正確
    arrowIcon.classList.add('fa-chevron-up');
});
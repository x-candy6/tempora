window.onload = function() {
    var selItem = sessionStorage.getItem("SelItem");  
    $('#select-item').val(selItem);
    }
    $('#select-item').change(function() { 
        var selVal = $(this).val();
        sessionStorage.setItem("SelItem", selVal);
    });
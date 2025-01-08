function getAjax(url, msg, reload) {
    $.get(url, function (data, status) {
        Swal.fire({
            icon: 'success',
            title: msg,
            showConfirmButton: false,
            timer: 1500
        }).then((result) => {
            if (reload == 'true') {
                location.reload()
            }
        })
    });
}


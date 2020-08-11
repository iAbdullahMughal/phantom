$(function () {
    $body = $("body");
    $("#request").on("submit", function (e) {
        e.preventDefault();
        $.ajax({
            url: '/search/username/',
            type: 'post',
            data: new FormData(this),
            processData: false,
            contentType: false,
            success: function (data) {
                var has_error = data['has_error'];
                if (has_error)
                {
                    var title = data['error_message']['title'];
                    var description = data['error_message']['description'];
                    toastr.options = {
                        "closeButton": true,
                        "debug": false,
                        "newestOnTop": true,
                        "progressBar": true,
                        "positionClass": "toast-top-right",
                        "preventDuplicates": true,
                        "onclick": null,
                        "showDuration": "300",
                        "hideDuration": "1000",
                        "timeOut": "5000",
                        "extendedTimeOut": "1000",
                        "showEasing": "swing",
                        "hideEasing": "linear",
                        "showMethod": "fadeIn",
                        "hideMethod": "fadeOut"
                    };
                    toastr.error(description, title);

                } else
                    {
                        if (data["id"]){
                        window.location.href = "/user_details/?user_id=" + data['id'];
                        }

                }
            }
        });
    });
});


$(document).on({
    ajaxStart: function () {
        $body.addClass("loading");


    },
    ajaxStop: function () {
        $body.removeClass("loading");
    }
});
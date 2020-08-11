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
                if (has_error) {
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

                } else {

                    var buffer = "";
                    if (data['site_results']) {

                        for (var i = 0; i < data['site_results'].length; i++) {
                            var content = data['site_results'][i];
                            buffer += "                    <li class=\"list-separated-item\">\n" +
                                "                        <div class=\"row align-items-center\">\n" +
                                "                            <div class=\"col-auto\">\n" +
                                "                                    <span class=\"avatar avatar-md d-block\"\n" +
                                "                                          style=\"background-image: url(demo/faces/female/12.jpg)\"></span>\n" +
                                "                            </div>\n" +
                                "                            <div class=\"col\">\n" +
                                "                                <div>\n" +
                                "                                    <big class=\"d-block item-except text-sm text-muted h-2x\">" + content["site_name"] + "</big>\n" +
                                "                                </div>\n" +
                                "                            </div>\n" +
                                "                            <div class=\"col\">\n" +
                                "                                <div>\n" +
                                "                                <small class=\"d-block item-except text-sm text-muted h-1x\">" + content["site_url_user"] + "</small>\n" +
                                "                                </div>\n" +
                                "                            </div>\n" +
                                "                            <div class=\"col-auto\">\n" +
                                "                                <div class=\"item-action dropdown\">\n" +
                                "                                    <a href=\"" + content["site_url_user"] + "\" target=\"_blank\" class=\"icon\"><i\n" +
                                "                                            class=\"fa fa-external-link\"></i></a>\n" +
                                "                                </div>\n" +
                                "                            </div>\n" +
                                "                        </div>\n" +
                                "                    </li>\n";

                        }
                        var username_list = document.getElementById("username_list");
                        username_list.innerHTML = buffer;

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
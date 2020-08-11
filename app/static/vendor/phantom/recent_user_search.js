$(document).ready(function () {
    var dt_table = $('#recent_search_username').DataTable({

        "bFilter": true,
        "aLengthMenu": [[25, 50, 100, 200], [25, 50, 100, 200]],
        "iDisplayLength": 25,
        "aaSorting": [[0, "desc"]],
        "bAutoWidth": true,
        "aoColumns": [

            {"bSortable": true, "bSearchable": true, "sClass": "center"},
            {
                "created_at": "created_at",
                "sClass": "left",
                "mRender": function (dateTime, type, row) {
                    const startDate = moment(dateTime).format("HH:mm DD/MM/YYYY");
                    return startDate;
                }
            },
            {
                "search_status": "search_status",
                "sClass": "left",
                "mRender": function (data, type, row) {
                    if (data ==='True') {
                        return "<p style=\"color: green\" ><i class='fa fa-check-circle-o'>" +
                            "</i> Completed</p>";
                    } else {
                        return '<i class="fa fa-circle-o-notch fa-spin fa-fw"></i> In progress ';
                    }


                }
            },
            {
                "id": "id",
                "sClass": "left",
                "mRender": function (data, type, row) {
                    return "<a class=\"btn btn-secondary btn-sm\" href='/user_details/?user_id=" + data + "' target=\"_blank\" >" +
                        "<i class=\"fa fa-share\" aria-hidden=\"true\"></i> View Details </a> ";
                }
            },
        ],
        "bProcessing": true,
        "bServerSide": true,
        "sAjaxSource": '/search/recent_user_search/',
    });
});

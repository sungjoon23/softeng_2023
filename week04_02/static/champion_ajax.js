function post_query() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/champ",
        data: $("#form_id").serialize(),
        success: update_result,
        dataType: "html"
    });
}

function update_result(data) {
    $("#results").html(data);
}
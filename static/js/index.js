$("#corpus-file").change(function() {
    var corpus = $("#corpus-form")[0];
    var data = new FormData(corpus);
    $.ajax({
        type:"POST",
        enctype:"multipart/form-data",
        data:data,
        processData: false,
        contentType: false,
        cache: false,
        url: "http://127.0.0.1:5000/getpcfg",
        timeout: 0,
        success:function(response_data) {
            alert("response_data.send");
        }
    });
});

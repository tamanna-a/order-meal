$(document).ready(function () {
    $('.btn').click(function(){
        //get ajax function
        $.ajax({
            url: "",
            type: "get",
            contentType: "application/json",
            //front end sends button_text
            data: {
                button_text: $(this).text() //refers to button element
            },
            //success when status 200
            success: function(response) {
                $('.btn').text(response.seconds)
            }
        })
    })
})
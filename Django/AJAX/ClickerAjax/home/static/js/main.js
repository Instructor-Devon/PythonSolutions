$(document).ready(function() {
    $.ajax({
        url: "/clicks/get",
        method: "GET"
    })
    .done(function(res) {
        $("#clicks").text(res);
    })
})

$('#clicker').click(function() {
    $.ajax({
        url: "/clicks/set",
        method: "GET"
    })
    .done(function(res) {
        console.log(res);
        $("#clicks").text(res);
    })
})
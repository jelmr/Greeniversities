$(".remove").click(function (e) {
    var url = $(this).attr('href');
    $(this).parent().remove();
    console.log(url);
    $.ajax({
        url: url,
        type: 'DELETE'
    })
        .done(function (data) {
            console.log("DONE")
        });
    return false;
});


//$("#add_feedback_submit").click(function(e){
//    $.ajax({
//        url: window.location.pathname,
//        type: 'POST',
//        data: 'name='+ $("#name").val() + '&feedback=' + $("#feedback").val()
//    })
//        .done(function (data) {
//            console.log("DONE")
//        })
//        .always(function(data){
//            console.log($(this).parent().serialize);
//        });
//
//
//   return false;
//});
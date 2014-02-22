function submit_feedback_form(id, university_id) {
    var data = Sijax.getFormValues(id);
    Sijax.request('add_post', [data.name, data.feedback, university_id]);
}

function delete_feedback(id) {
    Sijax.request('delete_post', [id]);
}


$(document).on('click', "#submit_feedback",function () {
    return false;
});

$(document).on('click', ".remove", function(){
   return false;
});



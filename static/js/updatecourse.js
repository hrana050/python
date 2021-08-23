$(document).ready(function () {
  $("#cancel").hide();
  $("#update").hide();
});
function getfunction(clicked) {
  $.ajax({
      type: "GET",
      url: "/editcourse/" + clicked,
      datatype:'json',
      success: function(data) {
       var coursename = data.my_data[1];
       var status = data.my_data[2];
       var sno = data.my_data[0];
      $("#txt_course").val(coursename);
      $('#status').val(status);
      $("#courseid").val(sno);
      $("#cancel").show();
      $("#update").show();
      $("#submit").hide();
      }
});
}
function cancelfunction() {
  $('#txt_course').val('').empty();
  $('#status').val('2');
  $("#cancel").hide();
  $("#update").hide();
  $("#submit").show();
}

function updatefunction() {
  courseupdate= {coursename:$('#txt_course').val(),status:$('#status').val(),sno:$('#courseid').val()};
  alert(courseupdate);
  var sno=$('#courseid').val();
      $.ajax({
        type: 'POST',
        url: "/updatecourse/" + sno,
        data: {
          'csrfmiddlewaretoken' : "{{  csrf_token  }}",
           coursedata:courseupdate
        },
        cache: false,
        processData: false,
        contentType: false,
        success: function (data){
            alert(data);
        },
        error: function(xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
}



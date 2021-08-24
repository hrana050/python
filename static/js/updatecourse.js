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
  var $coursevalue = $('#txt_course').val();
  var $status = $('#status').val();
  var $sno= $('#courseid').val();
  $.ajax({
      type:'POST',
      url:'{% url "updatecourse" %}',
      data:{
        coursevalue: $coursevalue,
        status:$status,
        sno:$sno,
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success:function(data){
        if(data.my_data>0)
        {
        $("#updatediv").append("<div class='alert alert-success alert-dismissible fade show' role='alert'>Course updated Successfully <button type='button' class='close' data-dismiss='alert' aria-label='Close'> <span aria-hidden='true'>&times;</span></button></div>");
        $("#updatediv").show();
        updatediv()
      }
      else
      {
        $("#updatediv").append("<div class='alert alert-danger alert-dismissible fade show' role='alert'>Could't updated..! <button type='button' class='close' data-dismiss='alert' aria-label='Close'> <span aria-hidden='true'>&times;</span></button></div>");
        $("#updatediv").show();
        updatediv()
      }
      },
      error : function(xhr,errmsg,err) {
        $("#updatediv").append("<div class='alert alert-danger alert-dismissible fade show' role='alert'>Course could't updated..! <button type='button' class='close' data-dismiss='alert' aria-label='Close'> <span aria-hidden='true'>&times;</span></button></div>");
        $("#updatediv").show();
        updatediv()
      }
  });
}
function updatediv() {
  $("#updatediv").delay(1000).fadeOut(500);   
}





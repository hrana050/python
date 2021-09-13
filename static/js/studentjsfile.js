
$(document).ready(function () {
var url = (window.location).href; // You can also use document.URL
var getsno = url.substring(url.lastIndexOf('/') + 1);

if(getsno !='addstudent')
{
    $("#cancel").show();
    $("#update").show();
    $("#submit").hide();
$.ajax({
    type: "GET",
    url: "/editstudent/" + getsno,
    datatype:'json',
    success: function(data) {

    $("#txt_f_name").val(data.my_data[1]);
    $('#txt_l_name').val(data.my_data[2]);
    $("#txt_id").val(data.my_data[3]);
    $("#txt_userid").val(data.my_data[4]);
    $('#txt_email').val(data.my_data[5]);
    $("#txt_pwd").val(data.my_data[6]);
    $("#txt_contact").val(data.my_data[7]);
    $('#txt_dob').val(data.my_data[9]);
    $("#stu_course").val(data.my_data[10]);
    $("#stu_year").val(data.my_data[8]);
    $('#address').val(data.my_data[11]);
    $("#stu_status").val(data.my_data[13]);
    $("#studentid").val(data.my_data[0]);
    $("#studentimg").attr("src",data.my_data[15]);
    $("#cancel").show();
    $("#update").show();
    $("#submit").hide();
    }
});
}
else
{
    $("#cancel").hide();
    $("#update").hide();
}
});
function cancelfunction() {
    $("#txt_f_name").val('').empty();
    $('#txt_l_name').val('').empty();
    $("#txt_id").val('').empty();
    $("#txt_userid").val('').empty();
    $('#txt_email').val('').empty();
    $("#txt_pwd").val('').empty();
    $("#txt_contact").val('').empty();
    $('#txt_dob').val('').empty();
    $("#stu_course").val(0);
    $("#stu_year").val('0');
    $('#address').val('').empty();
    $("#stu_status").val('').empty();
    $("#studentimg").val('').empty();
    $('#status').val('2');
    $("#cancel").hide();
    $("#update").hide();
    $("#submit").show();
  }

  function updatefunction() {
//   $(document).on('click', '#update', function(e) {

    //csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
    var formData = new FormData();
    formData.append('txt_f_name', $('#txt_f_name').val())
    formData.append('txt_l_name', $('#txt_l_name').val())
    formData.append('txt_id', $('#txt_id').val())
    formData.append('txt_userid', $('#txt_userid').val())
    formData.append('txt_email', $('#txt_email').val())
    formData.append('txt_pwd', $('#txt_pwd').val())
    formData.append('txt_contact', $('#txt_contact').val())
    formData.append('txt_dob', $('#txt_dob').val())
    formData.append('stu_course', $('#stu_course').val())
    formData.append('stu_year', $('#stu_year').val())
    formData.append('address', $('#address').val())
    formData.append('stu_status', $('#stu_status').val())
    formData.append('profilepic',  $('#profile')[0].files[0])
    formData.append('sno', $('#studentid').val())
    formData.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val())
    // $("#cancel").hide();
    // $("#update").hide();
    // $("#submit").show();
    $.ajax({
        type: 'POST',
       // url: '/update/',
        url:'{% url "update" %}',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        success: function (){
            $("#updatediv").append("<div class='alert alert-success alert-dismissible fade show' role='alert'>Detail updated Successfully <button type='button' class='close' data-dismiss='alert' aria-label='Close'> <span aria-hidden='true'>&times;</span></button></div>");
            $("#updatediv").show();
            updatediv()
           
        },
        error: function(xhr, errmsg, err) {
            $("#updatediv").append("<div class='alert alert-danger alert-dismissible fade show' role='alert'>Could't updated..! <button type='button' class='close' data-dismiss='alert' aria-label='Close'> <span aria-hidden='true'>&times;</span></button></div>");
            $("#updatediv").show();
            updatediv()
        }
    })
  }
  function updatediv() {
    $("#updatediv").delay(3000).fadeOut(500);   
  }
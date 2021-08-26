var formData = new FormData();
   
$(document).on('click', '#btn_submit', function(e) {
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
  formData.append('profilepic',  $('#profilepic')[0].files[0])
  formData.append('csrfmiddlewaretoken', '{{ csrf_token }}')

  var name=$('#fname').val();
//   alert(name);
    $.ajax({
        type: 'POST',
        url: '127.0.0.1:8000/storeprocedureuse',
        data: formData,
        headers:{"X-CSRFToken": "{{csrf_token}}"} ,
         
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (){
            alert('The post has been created!')
        },
        error: function(xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
})

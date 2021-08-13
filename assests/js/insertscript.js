var formData = new FormData();
   
$(document).on('click', '#btn_submit', function(e) {
  formData.append('fname', $('#fname').val())
  formData.append('emailid', $('#emailid').val())
  formData.append('contactno', $('#contactno').val())
  formData.append('username', $('#username').val())
  formData.append('profilepic',  $('#profilepic')[0].files[0])
 // formData.append('csrfmiddlewaretoken', '{{ csrf_token }}')

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

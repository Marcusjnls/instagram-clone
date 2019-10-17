$(document).ready(function(){
   $('form').submit(function(event){
     event.preventDefault()
     form = $("form")

     $.ajax({
       'url':'ajax/comment/',
       'type':'POST',
       'data':form.serialize(),
       'dataType':'json',
       'success': function(data){
         alert(data['success'])
       },
     })
     .done(function(data){
       alert('success')
     })
     $('#id_comment').val('')
    
  })

})

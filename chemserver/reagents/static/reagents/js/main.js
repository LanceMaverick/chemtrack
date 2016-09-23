$(document).ready( function() {
    $('#main_container').hide().fadeIn('slow');

});


$('#suggestion').keyup(function(){
    var query;
    query = $(this).val();
    $.get('reagents/search', {suggestion: query}, function(data){
        $('#res').html(data);
    });
});

$(function () {
    $('#datetimepicker1').datetimepicker({
        format: 'YYYY-MM-DD' //This is the default date format Django will accept, it also disables the time in the datepicker.
    })
});

$(document).ready(function(){
    
    $("#v-pills-tab").children().each(function(index){
        $(this).click(function(){
            console.log(index)
            new_content('items')
        })
    })

    function new_content(modelName) {
        var hasForm = $('.form').length;
        console.log("2",hasForm);
        if (!hasForm) {
            renderForm(modelName);
        }
        renderList(modelName);
    }

    function renderForm() {
        var url = '/new_item'; 
        $.ajax({
            type: 'GET',
            contentType: 'text/html; charset=UTF-8',
            url: url,
            success: function(result){
                // console.log('result',result)
                $('.col-9').prepend(result);
                $('.form').on('submit', function(event){
                    event.preventDefault();
                    console.log('hhhhhhhhhhhh');
                    var desc = $("#id_desc").val()
                    $.ajaxSetup({data:{csrfmiddlewaretoken:'{% csrf_token %}'}})
                    $.ajax({
                        type: 'POST',
                        // contentType: 'text/html; charset=UTF-8',
                        url: '/new_item/',
                        dataType: 'json',
                        data: {'desc': desc},
                        success: function (data) { 
                            console,log(data);
                         }
                    })
                })

            }
        })

    }
    function renderList(modelName) {
        console.log('wo run lfasdfsadf');
        var url = '/' + modelName;
        $.ajax({
            type: 'GET',
            contentType: 'text/html; charset=UTF-8',
            url: url,
            success: function(result){
                $('#table')[0].innerHTML = result;
            },
            error: function (e) { 
                console.log(e);
             }
        })
    }
})
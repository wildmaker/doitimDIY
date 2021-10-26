$(document).ready(function () {

    $("#v-pills-tab").children().each(function (index) {
        $(this).click(function () {
            new_content('items');
        })
    })

    function new_content(modelName) {
        var hasForm = $('.form').length;
        console.log("has form: ", Boolean(hasForm));
        if (!hasForm) {
            renderForm(modelName);
        }
        renderList(modelName);
    }

    function refreshHtml($htmlNode, viewURL) {
        // 刷新部分视图
        try {
            var htmlString = getHtml(viewURL);
            $htmlNode.replaceWith($.parseHTML(htmlString)[0]);
        } catch (error) {
            alert(error);
        }
    }

    function getHtml(viewURL) {
        $.ajax({
            type: 'GET',
            contentType: 'text/html; charset = UTF-8',
            url: viewURL,
            success: function (data) {
                return data;
            },
            error: function (e) {
                console.log(e);
                throw new Error("function_getHtml failed.")
            }
        })
    }

    function submitForm($form, formURL, successCallback) {
        var data = serializeJson($form)
        $form.submit(function (event) {
            event.preventDefault();
            $.ajaxSetup({ data: { csrfmiddlewaretoken: '{% csrf_token %}' } })
            $.ajax({
                type: 'POST',
                url: formURL,
                dataType: 'json',
                contentType: 'application/json; charset=UTF-8',
                data: data,
                success: successCallback(data),
                error: (e) => { throw e; }
            })
        })
    }

    function serializeJson($form) {
        // TODO: 序列化表单数据
    }

    function renderForm() {
        var url = '/new_item';
        $.ajax({
            type: 'GET',
            contentType: 'text/html; charset=UTF-8',
            url: url,
            success: function (result) {
                // console.log('result',result)
                $('.col-9').prepend(result);
                $('.form').on('submit', function (event) {
                    event.preventDefault();
                    console.log('hhhhhhhhhhhh');
                    var desc = $("#id_desc").val();
                    $.ajaxSetup({ data: { csrfmiddlewaretoken: '{% csrf_token %}' } })
                    $.ajax({
                        type: 'POST',
                        // contentType: 'text/html; charset=UTF-8',
                        url: '/new_item/',
                        dataType: 'json',
                        contentType: 'application/json; charset=UTF-8',
                        data: JSON.stringify({ 'desc': desc }),
                        success: function (re) {
                            console.log('data added!');
                            new_content('items');
                            // new_content('items');
                        },
                        error: function (e) {
                            console.log(e);
                        }
                    })
                })

            }
        })

    }
    function renderList(modelName) {
        console.log('刷新了列表！');
        var url = '/' + modelName;
        $.ajax({
            type: 'GET',
            contentType: 'text/html; charset=UTF-8',
            url: url,
            success: function (result) {
                $('#table')[0].innerHTML = result;
            },
            error: function (e) {
                console.log(e);
            }
        })
    }
})
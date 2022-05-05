$(document).ready(function() {
    $(".component").each(function(index, element) {
        // element == this
        const URL = $(element).attr("href");
        $(element).attr("style", "display:none;")
        rendertHtml($(element), URL);
    });

    function rendertHtml(htmlNode, URL) {
        $.ajax({
            type: 'GET',
            contentType: 'text/html; charset = UTF-8',
            url: URL,
            success: function(data) {
                htmlNode.prepend($.parseHTML(data));
            },
            error: function(e) {
                console.log(e);
                throw new Error("function_getHtml failed.")
            }
        })
    }
});

// 如果不加载，就生成铆点，否则，就返回组件本身
// 过程：获取所有元素，渲染元素
// input: URL
// output: render html to html node
$(document).ready(function() {
    $(".element").each(function(index, element) {
        // element == this
        const URL = $(element).attr("href");
        $(element).attr("style", "display:none;")
        rendertHtml($('main'), URL);
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
(function($){
    $("a.toggle").on('click', function(e){
        e.preventDefault();

        var $next_code_block = $(this).parent().next("pre");
        $next_code_block.toggle();

        $(this).toggleClass("displaying_code");
        if($(this).hasClass("displaying_code")){
            $(this).html("hide output &uArr;");
        }
        else{
            $(this).html("show output &dArr;");
        }
    });

    // Make all toggleable code blocks hidden on page load
    $("a.toggle").parent().next("pre").hide();
})(jQuery);

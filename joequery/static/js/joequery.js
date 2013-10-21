(function($){
    $("a.toggle").on('click', function(e){
        var $next_code_block = $(this).parent().next("pre");
        $next_code_block.toggle();
        e.preventDefault();
    });

    // Make all toggleable code blocks hidden on page load
    $("a.toggle").parent().next("pre").hide();
})(jQuery);

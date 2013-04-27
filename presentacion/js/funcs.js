$(document).ready(function() {
    $("#next-slide").click(function() {
        var slides = $(".slide");
        for(i in slides){
            var slide = $(slides[i]);
            if(slide.hasClass('active')){
                slide.removeClass('active');
                $(slides[parseInt(i) + 1]).addClass('active');
                break;
            }
        }
    });
    $("#prev-slide").click(function() {
        var slides = $(".slide");
        for(i in slides){
            var slide = $(slides[i]);
            if(slide.hasClass('active')){
                slide.removeClass('active');
                console.log(i);
                $(slides[parseInt(i) - 1]).addClass('active');
                break;
            }
        }
    });
});

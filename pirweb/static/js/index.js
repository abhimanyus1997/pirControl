$(function () {
    $("#pir-searchBtn").mouseenter(function () {
        $("#pir-home").hide();
    });
    $("#pir-searchBtn").mouseleave(function () {
        $("#pir-home").show();
    });

    //COMMAND TO CONTROL SPEED
    $(".dial").knob({
        'min': 0,
        'max': 10
    });

});


//COMMAND TO CONTROL MOVEMENT
$(document).keydown(function (e) {
    switch (e.which) {
        case 37:    //left arrow key
            $(".box").finish().animate({
                left: "-=1"
            });
            break;
        case 38:    //up arrow key
            $(".box").finish().animate({
                top: "-=1"
            });
            break;
        case 39:    //right arrow key
            $(".box").finish().animate({
                left: "+=1"
            });
            break;
        case 40:    //bottom arrow key
            $(".box").finish().animate({
                top: "+=1"
            });
            break;
    }
});
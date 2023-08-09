$(document).ready(function(){
    $('.slider').slick({
        arrows:false,
        dots:false,
        adaptiveHeight:true,
        slidesToShow:6,
        infinite:false, 
        touchThreshold: 90,
        swipeToSlide:true,
        touchMove: true,
        responsive: [
            {
              breakpoint: 1150,
              settings: {
                slidesToShow: 4.5,
                slidesToScroll: 4,
              }
            },
            {
              breakpoint: 900,
              settings: {
                slidesToShow: 3.3,
                slidesToScroll: 3
              }
            },
            {
              breakpoint: 700,
              settings: {
                slidesToShow: 2.7,
                slidesToScroll: 2
              }
            },
            {
                breakpoint:570,
                settings: {
                    slidesToShow: 2.3,
                    slidesToScroll:2
                }
            },
            {
                breakpoint:490,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll:2
                }
            },
            {
                breakpoint: 450,
                settings: {
                    slidesToShow:1.7,
                    slidesToScroll:1
                }
            },
            {
                breakpoint: 390,
                settings: {
                    slidesToShow:1.5,
                    slidesToScroll:1
                }
            },
            {
                breakpoint:350,
                settings: {
                    slidesToShow: 1.3
                }
            },
            {
                breakpoint: 310,
                settings: {
                    slidesToShow:1.1,
                }
            }
        ]
    });
});
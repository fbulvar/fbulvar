var INSPIRO = {};
(function($) {
    "use strict";
    var $window = $(window),
        $document = $(document),
        $body = $('body'),
        $topbar = $('#topbar'),
        $header = $('#header'),
        $transparentHeader = $header.hasClass('header-transparent') || $header.hasClass('header-light-transparent') || $header.hasClass('header-dark-transparent'),
        defaultLogo = $('#logo').find('.logo'),
        defaultLogoImg = defaultLogo.find('img').attr('src'),
        defaultlogoDark = defaultLogo.attr('data-dark-logo'),
        mainmenu = $('#mainMenu'),
        mainmenuitems = mainmenu.find('li.dropdown > a'),
        mainsubmenuitems = mainmenu.find('li.dropdown-submenu > a, li.dropdown-submenu > span'),
        sidePaneldefaultLogo = $('#panel-logo').find('.logo'),
        sidePaneldefaultLogoImg = sidePaneldefaultLogo.find('img').attr('src'),
        sidePaneldefaultlogoDark = sidePaneldefaultLogo.attr('data-dark-logo'),
        $topSearch = $('#top-search'),
        $parallax = $('.parallax'),
        $mouseScroll = $('.mouse-scroll'),
        dataAnimation = $("[data-animation]"),
        classFinder = ".";
    $.fn.exists = function() {
        return this.length > 0;
    };
    var isMobile = {
        Android: function() {
            return navigator.userAgent.match(/Android/i);
        },
        BlackBerry: function() {
            return navigator.userAgent.match(/BlackBerry/i);
        },
        iOS: function() {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i);
        },
        Opera: function() {
            return navigator.userAgent.match(/Opera Mini/i);
        },
        Windows: function() {
            return navigator.userAgent.match(/IEMobile/i);
        },
        any: function() {
            return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
        }
    };
    INSPIRO.responsiveClasses = function() {
        var jRes = jRespond([{
            label: 'smallest',
            enter: 0,
            exit: 479
        }, {
            label: 'handheld',
            enter: 480,
            exit: 767
        }, {
            label: 'tablet',
            enter: 768,
            exit: 991
        }, {
            label: 'laptop',
            enter: 992,
            exit: 1199
        }, {
            label: 'desktop',
            enter: 1200,
            exit: 10000
        }]);
        jRes.addFunc([{
            breakpoint: 'desktop',
            enter: function() {
                $body.addClass('device-lg');
            },
            exit: function() {
                $body.removeClass('device-lg');
            }
        }, {
            breakpoint: 'laptop',
            enter: function() {
                $body.addClass('device-md');
            },
            exit: function() {
                $body.removeClass('device-md');
            }
        }, {
            breakpoint: 'tablet',
            enter: function() {
                $body.addClass('device-sm');
            },
            exit: function() {
                $body.removeClass('device-sm');
            }
        }, {
            breakpoint: 'handheld',
            enter: function() {
                $body.addClass('device-xs');
            },
            exit: function() {
                $body.removeClass('device-xs');
            }
        }, {
            breakpoint: 'smallest',
            enter: function() {
                $body.addClass('device-xxs');
            },
            exit: function() {
                $body.removeClass('device-xxs');
            }
        }]);
    };
    INSPIRO.loader = function() {
        if ($(".loader-wrapper").exists()) {
            $('#mainMenu a:not([target="_blank"]):not([href^=#]), a.animation-link').on("click", function() {
                var href = this.href;
                $(".loader").fadeIn(300);
                $(".loader-wrapper").fadeIn(function() {
                    location.href = href;
                });
                return false;
            });
            $window.load(function() {
                $(".loader:not(.demo-loader)").fadeOut(200);
                $(".loader-wrapper:not(.demo-loader)").delay(100).fadeOut(400);
            });
        }
    };
    INSPIRO.carouselInspiro = function() {
        var $sliderCarousel = $('.carousel') || $('.owl-carousel'),
            $postCarousel = $(".post-mini-slider");
        if ($sliderCarousel.exists()) {
            $sliderCarousel.each(function() {
                var element = $(this),
                    sliderCarouselColumns = element.attr('data-carousel-col') || "4",
                    sliderCarouselColumnsMedium = element.attr('data-carousel-col-md') || "4",
                    sliderCarouselColumnsSmall = element.attr('data-carousel-col-sm') || "3",
                    sliderCarouselColumnsExtraSmall = element.attr('data-carousel-col-xs') || "1",
                    $sliderCarouselMargins = element.attr('data-carousel-margins') || "20",
                    $sliderCarouseDots = element.attr('data-carousel-dots') || false,
                    $sliderCarouseNav = false,
                    $sliderCarouseAutoPlay = element.attr('data-carousel-autoplay') || false,
                    $sliderCarouseVideo = element.attr('data-carousel-video') || false;
                if ($sliderCarouseDots === false) {
                    $sliderCarouseNav = true;
                } else {
                    $sliderCarouseDots = true;
                }
                if (sliderCarouselColumns == 1) {
                    element.owlCarousel({
                        margin: Number($sliderCarouselMargins),
                        nav: $sliderCarouseNav,
                        navText: ['<i class="fa fa-arrow-left icon-white"></i>', '<i class="fa fa-arrow-right icon-white"></i>'],
                        autoplay: $sliderCarouseAutoPlay,
                        autoplayHoverPause: true,
                        dots: $sliderCarouseDots,
                        items: 1,
                        autoHeight: false,
                        video: $sliderCarouseVideo,
                    });
                } else {
                    element.owlCarousel({
                        margin: Number($sliderCarouselMargins),
                        nav: $sliderCarouseNav,
                        navText: ['<i class="fa fa-arrow-left icon-white"></i>', '<i class="fa fa-arrow-right icon-white"></i>'],
                        autoplay: $sliderCarouseAutoPlay,
                        autoplayHoverPause: true,
                        dots: $sliderCarouseDots,
                        video: $sliderCarouseVideo,
                        responsive: {
                            0: {
                                items: sliderCarouselColumnsExtraSmall
                            },
                            600: {
                                items: sliderCarouselColumnsSmall
                            },
                            1000: {
                                items: sliderCarouselColumnsMedium
                            },
                            1200: {
                                items: sliderCarouselColumns
                            }
                        }
                    });
                }
            });
        }
        if ($postCarousel.exists()) {
            $postCarousel.each(function() {
                $postCarousel.owlCarousel({
                    autoplay: true,
                    autoplayHoverPause: true,
                    dots: true,
                    mouseDrag: false,
                    touchDrag: false,
                    items: 1,
                });
            });
        }
        if ($("#slider-carousel").exists()) {
            $("#slider-carousel").each(function() {
                $("#slider-carousel").owlCarousel({
                    margin: 0,
                    loop: true,
                    nav: true,
                    navText: ['<i class="fa fa-arrow-left icon-white"></i>', '<i class="fa fa-arrow-right icon-white"></i>'],
                    autoplay: true,
                    dots: false,
                    autoplayHoverPause: true,
                    navigation: true,
                    items: 1,
                    animateOut: 'fadeOut'
                });
                var owl = $("#slider-carousel");
                $('.owl-item.active .slider-content').addClass("animated fadeIn");
                owl.on('changed.owl.carousel', function(event) {
                    $('.owl-item:not(.active)').siblings().find(".slider-content").removeClass("animated fadeIn");
                    setTimeout(function() {
                        $('.owl-item.active .slider-content').addClass("animated fadeIn");
                    }, 300);
                    if ($("#slider-carousel .owl-item.active .slider-content iframe").length) {
                        var url = $("#slider-carousel .owl-item.active .slider-content iframe").attr("src");
                        $('iframe').attr('src', '');
                        $('iframe').attr('src', url);
                    }
                });
            });
        }
    };
    INSPIRO.naTo = function() {
        $('a.scroll-to, a.nav-to').on('click', function() {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 1500, 'easeInOutExpo');
            event.preventDefault();
            return false;
        });
    };

    INSPIRO.goToTop = function() {
        var $goToTop = $('.gototop');
        if ($window.scrollTop() > 450) {
            $goToTop.fadeIn();
        } else {
            $goToTop.fadeOut();
        }
        $goToTop.on("click", function() {
            $('body,html').stop(true).animate({
                scrollTop: 0
            }, 1500, 'easeInOutExpo');
            return false;
        });
    };
    INSPIRO.logoStatus = function() {
        if ($header.hasClass('header-navigation-light') && $window.width() < 991) {
            defaultLogo.find('img').attr('src', defaultLogoImg);
        } else {
            if ($header.hasClass('header-dark')) {
                if (defaultlogoDark) {
                    defaultLogo.find('img').attr('src', defaultlogoDark);
                } else {
                    defaultLogo.find('img').attr('src', defaultLogoImg);
                }
            } else {
                defaultLogo.find('img').attr('src', defaultLogoImg);
            }
        }
    };
    INSPIRO.stickyHeaderStatus = function() {
        if ($header.exists()) {
            var headerOffset = $header.offset().top;
            if ($window.scrollTop() > headerOffset) {
                if ($body.hasClass('device-lg') || $body.hasClass('device-md')) {
                    $header.addClass('header-sticky');
                    if ($header.hasClass('header-navigation-light')) {
                        defaultLogo.find('img').attr('src', defaultLogoImg);
                    }
                } else {
                    $header.removeClass('header-sticky');
                }
            } else {
                $header.removeClass('header-sticky');
            }
        }
    };
    INSPIRO.stickyHeader = function() {
        $window.on('scroll', function() {
            INSPIRO.logoStatus();
            INSPIRO.stickyHeaderStatus();
        });
    };

    $("#top-search-trigger").on("click", function() {
        $body.toggleClass('top-search-open');
        $topSearch.find('input').focus();
        return false;
    });
    mainmenuitems.on('click', function() {
        $(this).parent('ul li').toggleClass("resp-active", 1000, "easeOutSine");
        return false;
    });
    mainsubmenuitems.on('click', function() {
        $(this).parent('li').toggleClass('resp-active');
        return false;
    });
    INSPIRO.menuFix = function() {
        if ($body.hasClass('device-lg') || $body.hasClass('device-md')) {
            $('ul.main-menu .dropdown:not(.mega-menu-item) ul ul').each(function(index, element) {
                if ($window.width() - ($(element).width() + $(element).offset().left) < 0) {
                    $(element).addClass('menu-invert');
                }
            });
        }
    };
    $(".lines-button").on("click", function() {
        $(this).toggleClass("lines-button-close");
        return false;
    });


    INSPIRO.animations = function() {
        if (dataAnimation.exists() && $body.hasClass('device-lg') || $body.hasClass('device-md')) {
            dataAnimation.each(function() {
                $(this).addClass("animated");
                var $elem = $(this),
                    animationType = $elem.attr("data-animation") || "fadeIn",
                    animationDelay = $elem.attr("data-animation-delay") || 200,
                    animationDirection = ~animationType.indexOf("Out") ? "back" : "forward";
                if (animationDirection == "forward") {
                    $elem.appear(function() {
                        setTimeout(function() {
                            $elem.addClass(animationType + " visible");
                        }, animationDelay);
                    }, {
                        accX: 0,
                        accY: -120
                    }, 'easeInCubic');
                } else {
                    $elem.addClass("visible");
                    $elem.on("click", function() {
                        $elem.addClass(animationType);
                        return false;
                    });
                }
                if ($elem.parents('.demo-play-animations').length) {
                    $elem.on("click", function() {
                        $elem.removeClass(animationType);
                        setTimeout(function() {
                            $elem.addClass(animationType);
                        }, 50);
                        return false;
                    });
                }
            });
        }
    };
    INSPIRO.parallax = function() {
        if ($parallax.exists() || $(".page-title-parallax")) {
            if ($body.hasClass('device-lg') || $body.hasClass('device-md')) {
                $.stellar({
                    horizontalScrolling: false,
                    verticalOffset: 0,
                    horizontalOffset: 0
                });
            } else {
                $parallax.addClass('mobile-parallax');
            }
        }
    };


    INSPIRO.masonryIsotope = function() {
        var $isotops = $(".isotope");
        $isotops.each(function() {
            var isotopeTime, $elem = $(this),
                defaultFilter = $elem.data("isotopeDefaultFilter") || 0,
                id = $elem.attr("id"),
                mode = $elem.attr('data-isotope-mode') || "masonry",
                columns = $elem.attr('data-isotope-col') || "4",
                $elemContainer = $elem,
                itemElement = $elem.attr('data-isotope-item') || ".isotope-item",
                itemElementSpace = $elem.attr('data-isotope-item-space') || 0;
            $elem.isotope({
                filter: defaultFilter,
                itemSelector: itemElement,
                layoutMode: mode,
                transitionDuration: '0.6s',
                resizesContainer: true,
                resizable: true,
                animationOptions: {
                    duration: 400,
                    queue: !1
                }
            }), $window.resize(function() {
                $elemContainer.css('margin-right', '-' + itemElementSpace + '%');
                if ($body.hasClass('device-sm') || $body.hasClass('device-xs')) {
                    itemWidth(2, $elemContainer, itemElement, itemElementSpace);
                } else if ($body.hasClass('device-xxs')) {
                    itemWidth(1, $elemContainer, itemElement, itemElementSpace);
                } else {
                    itemWidth(columns, $elemContainer, itemElement, itemElementSpace);
                }
                if (columns == 1 && $body.hasClass('device-sm') || columns == 1 && $body.hasClass('device-xs')) {
                    itemWidth(1, $elemContainer, itemElement, itemElementSpace);
                }
                clearTimeout(isotopeTime), isotopeTime = setTimeout(function() {
                    $elem.isotope("layout");
                }, 300);
            });
            var $menu = $('[data-isotope-nav="' + id + '"]');
            $menu.length && $menu.find("li").on("click", function(e) {
                var $link = $(this);
                $(".filter-active-title").empty().append($link.text());
                if (!$link.hasClass("ptf-active")) {
                    var selector = $link.attr("data-filter");
                    $link.parents(".portfolio-filter").eq(0).find(".ptf-active").removeClass("ptf-active"), $link.addClass("ptf-active"), $elem.isotope({
                        filter: selector
                    });
                }
                e.preventDefault();
                return false;
            }), $window.resize();
        });
    };
    var itemWidth = function(columns, $elemContainer, itemElement, itemElementSpace) {
        var $findElement = $elemContainer.find(itemElement);
        var $findElementLarge = $elemContainer.find(".large-item");
        var itemElementMargins = {
            "margin-right": itemElementSpace + "%",
            "margin-bottom": itemElementSpace + "%",
        };
        if (columns == 1) {
            $findElement.width('100%');
            $findElementLarge.width('100%');
        }
        if (columns == 2) {
            $findElement.width(50 - itemElementSpace + '%').css(itemElementMargins);
            $findElementLarge.width(50 - itemElementSpace + '%').css(itemElementMargins);
        }
        if (columns == 3) {
            $findElement.width(33.333333 - itemElementSpace + '%').css(itemElementMargins);
            $findElementLarge.width(66.666666 - itemElementSpace + '%').css(itemElementMargins);
        }
        if (columns == 4) {
            $findElement.width(25 - itemElementSpace + '%').css(itemElementMargins);
            $findElementLarge.width(50 - itemElementSpace + '%').css(itemElementMargins);
        }
        if (columns == 5) {
            $findElement.width(20 - itemElementSpace + '%').css(itemElementMargins);
            $findElementLarge.width(40 - itemElementSpace + '%').css(itemElementMargins);
        }
        if (columns == 6) {
            $findElement.width(16.666666 - itemElementSpace + '%').css(itemElementMargins);
            $findElementLarge.width(33.333333 - itemElementSpace + '%').css(itemElementMargins);
        }
    };


    INSPIRO.lightBoxInspiro = function() {
        var $lightboxImageEl = $('[data-lightbox="image"]'),
            $lightboxGalleryEl = $('[data-lightbox="gallery"]'),
            $lightboxIframeEl = $('[data-lightbox="iframe"]'),
            $lightboxAjaxEl = $('[data-lightbox="ajax"]'),
            $lightboxAjaxGalleryEl = $('[data-lightbox="ajax-gallery"]');
        if ($lightboxImageEl.length > 0) {
            $lightboxImageEl.magnificPopup({
                type: 'image',
                closeOnContentClick: true,
                closeBtnInside: false,
                fixedContentPos: true,
                image: {
                    verticalFit: true
                }
            });
        }
        if ($lightboxGalleryEl.length > 0) {
            $lightboxGalleryEl.each(function() {
                var element = $(this);
                if (element.find('a[data-lightbox="gallery-item"]').parent('.clone').hasClass('clone')) {
                    element.find('a[data-lightbox="gallery-item"]').parent('.clone').find('a[data-lightbox="gallery-item"]').attr('data-lightbox', '');
                }
                element.magnificPopup({
                    delegate: 'a[data-lightbox="gallery-item"]',
                    type: 'image',
                    closeOnContentClick: true,
                    closeBtnInside: false,
                    fixedContentPos: true,
                    image: {
                        verticalFit: true
                    },
                    gallery: {
                        enabled: true,
                        navigateByImgClick: true,
                        preload: [0, 1]
                    }
                });
            });
        }
        if ($lightboxIframeEl.length > 0) {
            $lightboxIframeEl.magnificPopup({
                disableOn: 600,
                type: 'iframe',
                removalDelay: 160,
                preloader: false,
                fixedContentPos: false
            });
        }
        if ($lightboxAjaxEl.length > 0) {
            $lightboxAjaxEl.magnificPopup({
                type: 'ajax',
                callbacks: {
                    ajaxContentAdded: function(mfpResponse) {
                        INSPIRO.carouselInspiro();
                        INSPIRO.resposniveVideos();
                        INSPIRO.accordion();
                    },
                    open: function() {
                        $body.addClass('lightbox-open');
                    },
                    close: function() {
                        $body.removeClass('lightbox-open');
                    }
                }
            });
        }
        if ($lightboxAjaxGalleryEl.length > 0) {
            $lightboxAjaxGalleryEl.magnificPopup({
                delegate: 'a[data-lightbox="ajax-gallery-item"]',
                type: 'ajax',
                closeBtnInside: false,
                gallery: {
                    enabled: true,
                    preload: 0,
                    navigateByImgClick: false
                },
                callbacks: {
                    ajaxContentAdded: function(mfpResponse) {
                        INSPIRO.carouselInspiro();
                        INSPIRO.resposniveVideos();
                        INSPIRO.accordion();
                    },
                    open: function() {
                        $body.addClass('ohidden');
                    },
                    close: function() {
                        $body.removeClass('ohidden');
                    }
                }
            });
        }
    }


    INSPIRO.smothScroll = function() {
        if (!$mouseScroll.exists() && !$('#multiscroll').length) {
            $.srSmoothscroll({
                step: 140,
                speed: 600,
                ease: 'swing',
                target: $('body'),
                container: $window
            })
        }
    };
    INSPIRO.mouseScroll = function() {
        if ($mouseScroll.exists()) {
            $.scrollify({
                section: "section",
                sectionName: "section-name",
                scrollSpeed: 1100,
                offset: -90,
                scrollbars: true
            });
        }
    }
    $window.load(function() {
        INSPIRO.masonryIsotope(), INSPIRO.carouselInspiro(), INSPIRO.animations()
    });
    $document.ready(INSPIRO.lightBoxInspiro(), INSPIRO.loader(), INSPIRO.responsiveClasses(), INSPIRO.stickyHeader(), INSPIRO.logoStatus(), INSPIRO.menuFix(), INSPIRO.parallax(), INSPIRO.naTo(), INSPIRO.smothScroll(), INSPIRO.mouseScroll(), INSPIRO.goToTop());
    $window.resize(function() {
        INSPIRO.logoStatus(), INSPIRO.menuFix()
    });
    $window.scroll(function() {
        INSPIRO.goToTop()
    });

    $('.carousel-customer-adv').owlCarousel({
        loop:true,
        items:1,
        smartSpeed:1700,
        responsiveClass:true,
        responsive:{
            0:{
                items:1
            }
        },
       // autoplay: true,
       // autoplayTimeout:3000,
    });

    $('.carousel-facts').owlCarousel({
        loop:true,
        dots:false,
        responsiveClass:true,
        responsive:{
            0:{
                items:1
            },
            760:{
                items:2
            },
            1200:{
                items:3
            },
        },

    });

    $('.news-text-block h3').equalHeights();
    $('.news-description p').equalHeights();

})(jQuery);
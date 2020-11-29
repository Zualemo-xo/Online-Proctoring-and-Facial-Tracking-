const initBg = (autoplay = true) => {
  const bgImgsNames = ['bg_img_4.jpg', 'bg_img_2.jpg', 'bg_img_3.jpg'];
  const bgImgs = bgImgsNames.map(img => {{ url_for('img',filename='') }} + img);

    $.backstretch(bgImgs, {duration: 4000, fade: 500});

    if(!autoplay) {
      $.backstretch('pause');
    }
}

const setBg = id => {
    $.backstretch('show', id);
}

const setBgOverlay = () => {
    const windowWidth = window.innerWidth;
    const bgHeight = $('body').height();
    const tmBgLeft = $('.tm-bg-left');

    $('.tm-bg').height(bgHeight);

    if(windowWidth > 768) {
        tmBgLeft.css('border-left', `0`)
                .css('border-top', `${bgHeight}px solid transparent`);
    } else {
        tmBgLeft.css('border-left', `${windowWidth}px solid transparent`)
                .css('border-top', `0`);
    }
}

$(document).ready(function () {
    const autoplayBg = true;	// set Auto Play for Background Images
    initBg(autoplayBg);
    setBgOverlay();

    const bgControl = $('.tm-bg-control');
    bgControl.click(function() {
        bgControl.removeClass('active');
        $(this).addClass('active');
        const id = $(this).data('id');
        setBg(id);
    });

    $(window).on("backstretch.after", function (e, instance, index) {
        const bgControl = $('.tm-bg-control');
        bgControl.removeClass('active');
        const current = $(".tm-bg-controls-wrapper").find(`[data-id=${index}]`);
        current.addClass('active');
    });

    $(window).resize(function() {
        setBgOverlay();
    });
});

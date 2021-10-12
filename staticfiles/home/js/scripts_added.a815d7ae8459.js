// スクロール時にnavbarの背景色を変更
$(window).scroll(function(){
    $('nav').toggleClass('scrolled', $(this).scrollTop() > 0);
});
// ハンバーガーボタン挙動
$(function() {
    $('.hamburger').click(function() {
        $(this).toggleClass('active');

        if ($(this).hasClass('active')) {
            $('.nav-link').addClass('active');
            $('.nav').addClass('scrolled');
        } else {
            $('.nav-link').removeClass('active');
            $('.nav').removeClass('scrolled');
        }
    });
});
// オープニングにロゴを表示
$(function() {
    setTimeout(function(){
        $('.start p').fadeIn(1600);
    },0); //0.5秒後にロゴをフェードイン!
    setTimeout(function(){
        $('.start').fadeOut(500);
    },2500); //2.5秒後にロゴ含め真っ白背景をフェードアウト！
});
// スクロール時にアイテムをフェードイン
$(function(){
    $(window).on('load scroll', function(){
        $('.scrollanime').each(function(){
            //ターゲットの位置を取得
            var target = $(this).offset().top;
            //スクロール量を取得
            var scroll = $(window).scrollTop();
            //ウィンドウの高さを取得
            var height = $(window).height();
            //ターゲットまでスクロールするとフェードインする
            if (scroll > target - height){
                //クラスを付与
                $(this).addClass('fadeInDown');
            }
        });
    });
});
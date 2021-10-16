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
        } else {
            $('.nav-link').removeClass('active');
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

// TIMELINE用
(function($) {
    $.fn.timeline = function() {
      var selectors = {
        id: $(this),
        item: $(this).find(".timeline-item"),
        activeClass: "timeline-item--active",
        img: ".timeline__img"
      };
      selectors.item.eq(0).addClass(selectors.activeClass);
      selectors.id.css("background-image", "url(" + selectors.item.first().find(selectors.img).attr("src") + ")");
  
      var itemLength = selectors.item.length;
      $(window).scroll(function() {
        var max, min;
        var pos = $(this).scrollTop() + 300;
        selectors.item.each(function(i) {
          min = $(this).offset().top;
          max = ($(this).height() + $(this).offset().top);
          var that = $(this)
          if (i == itemLength - 2 && pos > min + $(this).height() / 2) {
            selectors.item.removeClass(selectors.activeClass);
            selectors.id.css("background-image", "url(" + selectors.item.last().find(selectors.img).attr('src') + ")");
            selectors.item.last().addClass(selectors.activeClass)
          } else if (pos <= max - 40 && pos >= min) {
              selectors.id.css("background-image", "url(" + $(this).find(selectors.img).attr('src') + ")");
              selectors.item.removeClass(selectors.activeClass);
              $(this).addClass(selectors.activeClass);
            }
          
        });
      });
  
    }
  })(jQuery);
  $("#timeline-1").timeline();


  //初回のみモーダルをすぐ出す判定。flagがモーダル表示のstart_open後に代入される
  var access = $.cookie('access')
  if(!access){
    flag = true;
    $.cookie('access', false);
  }else{
    flag = false  
  }
  
  //モーダル表示
  $(".video-open").modaal({
  start_open:flag, // ページロード時に表示するか
  overlay_close:true,//モーダル背景クリック時に閉じるか
  type: 'video',
  background: '#28BFE7', // 背景色
  overlay_opacity:0.8, // 透過具合
  before_open:function(){// モーダルが開く前に行う動作
    $('html').css('overflow-y','hidden');/*縦スクロールバーを出さない*/
  },
  after_close:function(){// モーダルが閉じた後に行う動作
    $('html').css('overflow-y','scroll');/*縦スクロールバーを出す*/
  }
  });
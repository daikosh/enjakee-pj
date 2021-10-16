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


// モーダルウィンドウ
//IFrame Player API の読み込み
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

//YouTubeの埋め込み
var ytPlayer;
function onYouTubeIframeAPIReady() {
	ytPlayer = new YT.Player('movie-content01', {
		width: 800,
		height: 450,
		videoId: 'ZRCdORJiUgU',
		events: {
			'onReady': onPlayerReady,
		},
		playerVars: {
			rel: 0, //再生動画と同じチャンネルから関連動画を選択
			modestbranding: 1 //YouTubeロゴを表示しない
		}
	});
}

function onPlayerReady(event) {
	event.target.mute(); //音声をミュートに
	event.target.playVideo(); //動画再生
}

$(function() {
	$.magnificPopup.open({
		items: {
			src: '#movie01'
		},
		mainClass: 'mfp-fade01',
		removalDelay: 200
	});
});
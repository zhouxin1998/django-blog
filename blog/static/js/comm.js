$(document).ready(function () {
	//banner
    $('#banner').easyFader();
	
    //nav
	$("#mnavh").click(function(){
        $("#starlist").toggle();
        $("#mnavh").toggleClass("open");
	});
	  
	  
	 //nav 		
    var obj=null;
    var As=document.getElementById('starlist').getElementsByTagName('a');
    obj = As[0];
    for(i=1;i<As.length;i++){if(window.location.href.indexOf(As[i].href)>=0)
    obj=As[i];}
    obj.id='selected';
   /*
  
  search
  

    $('.search_ico').click(function () {
        $('.search_bar').toggleClass('search_open');
        if ($('#keyboard').val().length > 2) {
            $('#searchform').submit();
        } else {
            return false;
        }
    });
    if(!$('#search_bar').hasClass('search_open')){
        $('#keyboard').val('');
    }
  */

    //header
	var new_scroll_position = 0;
	var last_scroll_position;
	var header = document.getElementById("header");

	window.addEventListener('scroll', function(e) {
	  last_scroll_position = window.scrollY;

	  if (new_scroll_position < last_scroll_position && last_scroll_position > 80) {
		header.classList.remove("slideDown");
		header.classList.add("slideUp");

	  } else if (new_scroll_position > last_scroll_position) {
		header.classList.remove("slideUp");
		header.classList.add("slideDown");
	  }

	  new_scroll_position = last_scroll_position;
	});
	
	
	
	
		$('.fenlei li').click(function(){
                $(this).addClass('flselect').siblings().removeClass('flselect');
                $('.newstw>ul:eq('+$(this).index()+')').show().siblings().hide();
            });

	
	//aside
    var Sticky = new hcSticky('aside', {
      stickTo: 'main',
      innerTop: 200,
      followScroll: false,
      queries: {
        480: {
          disable: true,
          stickTo: 'body'
        }
      }
    });
	
	
	//scroll to top
    var offset = 300,
        offset_opacity = 1200,
        scroll_top_duration = 700,
        $back_to_top = $('.cd-top');

    $(window).scroll(function () {
        ($(this).scrollTop() > offset) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
        if ($(this).scrollTop() > offset_opacity) {
            $back_to_top.addClass('cd-fade-out');
        }
    });
    $back_to_top.on('click', function (event) {
        event.preventDefault();
        $('body,html').animate({
                scrollTop: 0
            }, scroll_top_duration
        );
    });
	
	
		
	});
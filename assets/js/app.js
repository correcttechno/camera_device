$(function () {
	"use strict";
	
	
	// search bar
	$(".search-btn-mobile").on("click", function () {
		$(".search-bar").addClass("full-search-bar");
	});
	$(".search-arrow-back").on("click", function () {
		$(".search-bar").removeClass("full-search-bar");
	});
	$(document).ready(function () {
		$(window).on("scroll", function () {
			if ($(this).scrollTop() > 60) {
				$('.top-header').addClass('bg-dark sticky-top-header');
			} else {
				$('.top-header').removeClass('bg-dark sticky-top-header');
			}
		});
		$('.back-to-top').on("click", function () {
			$("html, body").animate({
				scrollTop: 0
			}, 600);
			return false;
		});
	});
	$(function () {
		if($('.metismenu-card').html()!=undefined)
		$('.metismenu-card').metisMenu({
			toggle: false,
			triggerElement: '.card-header',
			parentTrigger: '.card',
			subMenu: '.card-body'
		});
	});
	// Tooltips 
	$(function () {
		if($('[data-toggle="tooltip"]').html()!=undefined)
		$('[data-toggle="tooltip"]').tooltip()
	})
	// Metishmenu card collapse
	$(function () {
		if($('.card-collapse').html()!=undefined)
		$('.card-collapse').metisMenu({
			toggle: false,
			triggerElement: '.card-header',
			parentTrigger: '.card',
			subMenu: '.card-body'
		});
	});
	// toggle menu button
	$(".toggle-btn").click(function () {
		if ($(".wrapper").hasClass("toggled")) {
			// unpin sidebar when hovered
			$(".wrapper").removeClass("toggled");
			$(".sidebar-wrapper").unbind("hover");
		} else {
			$(".wrapper").addClass("toggled");
			$(".sidebar-wrapper").hover(function () {
				$(".wrapper").addClass("sidebar-hovered");
			}, function () {
				$(".wrapper").removeClass("sidebar-hovered");
			})
		}
	});
	$(".toggle-btn-mobile").on("click", function () {
		$(".wrapper").removeClass("toggled");
	});
	// chat toggle
	$(".chat-toggle-btn").on("click", function () {
		$(".chat-wrapper").toggleClass("chat-toggled");
	});
	$(".chat-toggle-btn-mobile").on("click", function () {
		$(".chat-wrapper").removeClass("chat-toggled");
	});
	// email toggle
	$(".email-toggle-btn").on("click", function () {
		$(".email-wrapper").toggleClass("email-toggled");
	});
	$(".email-toggle-btn-mobile").on("click", function () {
		$(".email-wrapper").removeClass("email-toggled");
	});
	// compose mail
	$(".compose-mail-btn").on("click", function () {
		$(".compose-mail-popup").show();
	});
	$(".compose-mail-close").on("click", function () {
		$(".compose-mail-popup").hide();
	});
	// === sidebar menu activation js
	$(function () {
		for (var i = window.location, o = $(".metismenu li a").filter(function () {
			return this.href == i;
		}).addClass("").parent().addClass("mm-active");;) {
			if (!o.is("li")) break;
			o = o.parent("").addClass("mm-show").parent("").addClass("mm-active");
		}
	}),
	// metismenu
	$(function () {
		if($('#menu').html()!=undefined)
			$('#menu').metisMenu();
	});
	/* Back To Top */
	$(document).ready(function () {
		$(window).on("scroll", function () {
			if ($(this).scrollTop() > 300) {
				$('.back-to-top').fadeIn();
			} else {
				$('.back-to-top').fadeOut();
			}
		});
		$('.back-to-top').on("click", function () {
			$("html, body").animate({
				scrollTop: 0
			}, 600);
			return false;
		});
	});
	/*switcher*/
	$(".switcher-btn").on("click", function () {
		$(".switcher-wrapper").toggleClass("switcher-toggled");
	});
	$('#theme1').click(theme1);
    $('#theme2').click(theme2);
    $('#theme3').click(theme3);
    $('#theme4').click(theme4);
    $('#theme5').click(theme5);
    $('#theme6').click(theme6);
    $('#theme7').click(theme7);
    $('#theme8').click(theme8);
    $('#theme9').click(theme9);
    $('#theme10').click(theme10);
    $('#theme11').click(theme11);
    $('#theme12').click(theme12);

    function theme1() {
      $('body').attr('class', 'bg-theme bg-theme1');
    }

    function theme2() {
      $('body').attr('class', 'bg-theme bg-theme2');
    }

    function theme3() {
      $('body').attr('class', 'bg-theme bg-theme3');
    }

    function theme4() {
      $('body').attr('class', 'bg-theme bg-theme4');
    }
	
	function theme5() {
      $('body').attr('class', 'bg-theme bg-theme5');
    }
	
	function theme6() {
      $('body').attr('class', 'bg-theme bg-theme6');
    }

    function theme7() {
      $('body').attr('class', 'bg-theme bg-theme7');
    }

    function theme8() {
      $('body').attr('class', 'bg-theme bg-theme8');
    }

    function theme9() {
      $('body').attr('class', 'bg-theme bg-theme9');
    }

    function theme10() {
      $('body').attr('class', 'bg-theme bg-theme10');
    }

    function theme11() {
      $('body').attr('class', 'bg-theme bg-theme11');
    }

    function theme12() {
      $('body').attr('class', 'bg-theme bg-theme12');
    }
});



var ip_address=''

$.fn.StartWebSocket=function(myip){
	ip_address=myip
	socket=new WebSocket('ws://'+myip+':8082')
		socket.onopen=function(e){
			console.log("Socket Connected");
		}
		var say=0;
		socket.onmessage=function(e){
			console.log(e.data)
			say++;
			json=JSON.parse(e.data)
			$('#lisence_plates').prepend('<li class="d-flex my-plate align-items-center bg-transparent"><p class="'+(json[1]==true?'text-success':'text-danger')+' mb-0">'+say+"| "+json[0]+'</p></li>');
		}
}


$('#save_plate').click(function(){
	var plate=$('#lisence_plate').val();
	if(plate!=''){
		$.post('/addplate',{'plate':plate},function(e){
			alert(e);
		})
	}
})

$('.deleteplate[id]').click(function(){
	var id=$(this).attr('id');
	if(id!=''){
		$.post('/deleteplate',{'id':id},function(e){
			alert(e);
			window.location.reload()
		})
	}
})

$('#display_mode').change(function(){
	$.post('/changedisplay',{'mode':$(this).val()},function(e){
		
	})
})


$('#save_api').click(function(){
	var request_url=$('#request_url').val();

	var plate=0,date=0,scaned_image=0,cropped_image=0;

	if($('#plate').prop('checked'))
	plate=$('#plate').val();
	if($('#date').prop('checked'))
	date=$('#date').val();
	if($('#scaned_image').prop('checked'))
	scaned_image=$('#scaned_image').val();
	if($('#cropped_image').prop('checked'))
	cropped_image=$('#cropped_image').val();

	$.post('/saveapi',
	{
		'request_url':request_url,
		'plate':plate,
		'date':date,
		'scaned_image':scaned_image,
		'cropped_image':cropped_image
	}
	,function(e){
		alert(e);
	})
})


$('#login_btn').click(function(){
	var username=$('#username').val();
	var password=$('#password').val();
	
	$.ajax({
		url:'/setlogin',
		data:{
		'username':username,
		'password':password
		},
		dataType:'Json',
		type:'post',
		success:function(myjson){
			console.log(myjson);
			if(myjson.status==true){
				localStorage.setItem('uid',myjson.uid);
				window.location.href="/index.html?token="+myjson.uid;
			}
			else{
				$('#msg').html(myjson.msg);
			}
		},
	});
})

var token=localStorage.getItem('uid');
$(function(){
	if(token!=null && token!=undefined){
		$.each($('a'),function(index,val){
			$('a').eq(index).attr('href',val+'?token='+token);
		})
		setTimeout(function(){
			$('#realtime_stream').attr('src','/realtime.mjpg?token='+token);
			$('#cropped_stream').attr('src','/cropped.mjpg?token='+token);
			$('#_stream').attr('src','/stream.mjpg?token='+token);
		})
	}
})


$('#save_password').click(function(){
	var password=$('#password').val();
	var retrypassword=$('#retrypassword').val();
	if(password!='' && retrypassword!='' && (password==retrypassword)){
		$.post('/setrootpassword',{
			'password':password,
			'token':token
		},function(e){
			$('#password').val('');
			$('#retrypassword').val('');
			$('#msg').html(e);
		});
	}
	else{
		$('#msg').html("Passwords are not the same");
	}
})
window.onscroll = function() {
                                scrollFunction();
                                header_fixed();
                                scrollIndicator();
                                pay()};

function scrollFunction() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        document.getElementById("back-to-top").style.display = "block";
    } else {
        document.getElementById("back-to-top").style.display = "none";
    }
}

// scroll to the top
function topFunction(){
    $("html, body").animate({ scrollTop: 0 }, "slow");
}

// header-fixed
function header_fixed(){
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("header-fixed").style.position = "fixed"
        document.getElementById("header-fixed").style.width = "100%"
        document.getElementById("header-fixed").style.zIndex = "1000000"
        document.getElementById("header-fixed").style.top = "0%"
    } else {
        document.getElementById("header-fixed").style.position = "initial";
    }
}


function scrollIndicator() {
      var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      var scrolled = (winScroll / height) * 100;
      document.getElementById("myBar").style.width = scrolled + "%";
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("scrollIndicator").style.top = "13.2%" ;
        document.getElementById("scrollIndicator").style.position = "fixed";
        document.getElementById("scrollIndicator").style.zIndex = "10000";
      }else {
        document.getElementById("scrollIndicator").style.position = "initial";
    }
}

function pay(){
    if (document.body.scrollTop > 160 || document.documentElement.scrollTop > 160) {
        document.getElementById("pay").style.position = "fixed"
        document.getElementById("pay").style.zIndex = "10000"
        document.getElementById("pay").style.top = "5%"
        document.getElementById("pay").style.left = "57%"
        document.getElementById("pay").style.width = "380px"

    } else {
        document.getElementById("pay").style.position = "initial";
    }
}


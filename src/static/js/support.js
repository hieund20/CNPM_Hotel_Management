window.onscroll = function() {
                                scrollFunction();
                                header_fixed();
                                scrollIndicator()};

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
      if (document.body.scrollTop > 45 || document.documentElement.scrollTop > 45) {
        document.getElementById("header-top").style.display = "none";
      }else {
        document.getElementById("header-top").style.display = "";
    }
}


function deleteBookingRoom(){
    event.preventDefault();
    fetch('/check-in', {
        method: 'post',
        body: JSON.stringify({
        }),
        headers: {
            'Context-Type': 'application/json'
        }
    }).then(
    res => {
        if (res) {
            if (res?.status !== 500) {
                console.log("Thao tác thành công")
                return res.json()
            }
            else {
                console.log("Thao tác thất bại", res?.statusText)
            }
        }
    }
    ).then(data => {
        if(data == true){
            document.getElementById("border-history").style.display = "none"
            document.getElementById("tb-his").style.display = ""
        }
    }
    ).catch(err => {
            console.log(err);
        }
    );
}



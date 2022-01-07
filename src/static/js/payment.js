const payment_success = () => {
     // Redirect to payment success page
     console.log(window.location.pathname)
     window.location.href="/payment/success";
}

const url = window.location.pathname
if (url === "/payment/success"){
     console.log("url", url)
     setInterval(() => {
        var spanEl = document.querySelector("#counter-countdown");
        var count = spanEl.textContent * 1 - 1;
        spanEl.textContent = count;
        if (count <= 0) {
            window.location.href="/";
        }
     }, 1000);
}

/* UI button payment brand handle */
window.onload = () => {
   document.getElementById("momo-button").disabled = true
   document.getElementById("zalo-button").disabled = true
   document.getElementById("paypal-button").disabled = true
};

const offlineRadioCheck = () => {
    document.getElementById("momo-button").disabled = true
    document.getElementById("zalo-button").disabled = true
    document.getElementById("paypal-button").disabled = true
}

const onlineRadioCheck = () => {
    document.getElementById("momo-button").disabled = false
    document.getElementById("zalo-button").disabled = false
    document.getElementById("paypal-button").disabled = false
}



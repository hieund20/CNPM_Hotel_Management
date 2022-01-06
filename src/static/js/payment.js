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


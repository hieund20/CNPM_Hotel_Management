const addToCart = (id, name, price, receiveDay, payDay, personAmount) => {
    event.preventDefault();

    fetch('/api/cart', {
        method: 'post',
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price,
            "receive-day": receiveDay,
            "pay-day": payDay,
            "person-amount": personAmount,
        }),
        headers: {
            'Context-Type': 'application/json'
        }
    }).then(
    res => {
        if (res) {
            if (res?.status !== 500) {
                console.log("Thao tác thành công")
                console.log("res", res)
                return res.json()
            }
            else {
                console.log("Thao tác thất bại", res?.statusText)
            }
        }
    }
    ).then(data => {
            console.log('data', data);
        }
    ).catch(err => {
            console.log(err);
        }
    );
}

function addComment(productId) {
    let content = document.getElementById('commentId')
    if (content !== null) {
        fetch('/api/comments', {
            method: 'post'
            body: JSON.stringify({
                'product_id': productId,
                'content': content.value
            })
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.json()).then(data => {
            if (data.status == 201) {
                let c = data.comment

                let area = getElementById('commentArea')
                area.innerHTML = `
                <div class="cmt comment">
                    <div class="col-md-1 col-xs-4 flex">
                        <p><b>${c.user.username}</b></p>
                    </div>
                    <div class="col-md-11 col-xs-8">
                        <p>${c.content}</p>
                        <p><em>${c.created_date}</em></p>
                    </div>
                </div>
                ` + area.innerHTML
            } else if (data.status == 404)
                alert(data.err_msg)
        })
    }
}
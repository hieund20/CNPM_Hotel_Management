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

//const filterRoomFormSubmit = (typeRoomId, quantityBed, priceSort) => {
//    console.log('hellp', typeRoomId, quantityBed, priceSort)
//    document.getElementsByName('type-room-id')[0].value.innerHTML = typeRoomId
//    document.getElementsByName('type-room-id')[0].value.innerHTML = typeRoomId
//    document.getElementsByName('price-sort')[0].value.innerHTML = typeRoomId
//}

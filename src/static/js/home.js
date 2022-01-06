const handleFilterRoom = () => {
    event.preventDefault();
    let type_room_id = document.getElementsByName('type-room-id')[0].value
    let quantity_bed = document.getElementsByName('quantity-bed')[0].value
    let price_sort = document.getElementsByName('price-sort')[0].value

    console.log("hello", price_sort)

    fetch('/api/home', {
        method: 'post',
        body: JSON.stringify({
            "type_room_id": type_room_id,
            "quantity_bed": quantity_bed,
            "price_sort": price_sort,
        }),
        headers: {
          'Accept': 'application/json',
            'Context-Type': 'application/json',
        }
    }).then(
    res => {
        if (res) {
            if (res?.status === 200) {
                console.log("Thao tác thành công")
                console.log("res", res)
                return res.text()
            }
            else {
                console.log("Thao tác thất bại", res?.statusText)
            }
        }
    }).then(data => {
        console.log('data', data);
    }).catch(err => {
        console.log(err);
    });
}
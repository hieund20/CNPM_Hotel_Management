//function order(id, name, price){
//    event.preventDefault();
//    fetch('/api/add-cart', {
//        method: 'post',
//        body: JSON.stringify ({
//            'id': id,
//            'name': name,
//            'price': price
//        }),
//        headers: {
//            'Content-Type': 'application/json'
//        }
//    }).then(function(res){
//    console.info(res)
//        return res.json();
//    }).then(function(data){
//        let order = document.getElementById('countCart')
//        order.innerText = data.totalQuantity
//    })

function order(room_id, name_room, price, name_user){
    event.preventDefault();
    fetch('/api/add-cart', {
        method: 'post',
        body: JSON.stringify ({
            'id': room_id,
            'name': name_room,
            'price': price,
            'name_user': name_user
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
}

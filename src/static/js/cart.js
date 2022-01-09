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
            total_quantity = document.getElementById("countCart");
            total_quantity.innerHTML = data[3];
            //Show toast message
            handleShowToast();
        }
    ).catch(err => {
            console.log(err);
        }
    );
}

const handleShowToast = () => {
    var toastEl = document.getElementById("toast-message");
    toastEl.className = "show";
    setTimeout(() => { toastEl.className = toastEl.className.replace("show", ""); }, 3000);
}


function searchCart(element){
    text = element.value.toUpperCase();
    l = document.getElementById("list-room");
    listRoom = l.getElementsByClassName("room-cart")
//    listName = listRoom.getElementsByClassName("name-cart")
    for (i= 0; i < listRoom.length; i++){
        nameRoom = listRoom[i].getElementsByTagName("span")[0].innerHTML;
        if(nameRoom.toUpperCase().indexOf(text) > -1){
            listRoom[i].style.display = "";
        } else{
            listRoom[i].style.display = "none";
        }
    }
}
function confirmDelete(element){
//    var result = confirm("Bạn có muốn xóa phòng này?");
//        if (result == true) {
//            deleteCart(element);
//        }
    swal({
      title: "Bạn có chắc chắn muốn xóa phòng này?",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
    .then((willDelete) => {
      if (willDelete) {
        deleteCart(element);

      } else {
        swal("Hủy xóa !!!");
      }
    });
}

function deleteCart(element){
    event.preventDefault();
    fetch('/delete-cart', {
        method: 'post',
        body: JSON.stringify({
            "id": element.name
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
//            if (data[0] == true){
//                swal("Đã xóa thành công!!!", {
//                  icon: "success",
//                });
//            }
//            else{
//                 swal("Hệ thống đang bảo trì! Vui lòng quay lại sau!", {
//                  icon: "error",
//                });
//            }
//            alert(data[0]);
            total_quantity = document.getElementById("countCart");
            total_quantity.innerHTML = data[1];

            total_money = document.getElementById("total_money");
            total_money.innerHTML = (data[2].toFixed(1)) + "$";
            hideRoomDeleted(element);
        }
    ).catch(err => {
            console.log(err);
        }
    );
}


function hideRoomDeleted(element){
    roomIdDelete = element.name;
    l = document.getElementById("list-room");
    listRoom = l.getElementsByClassName("room-cart")
//    listName = listRoom.getElementsByClassName("name-cart")
    for (i= 0; i < listRoom.length; i++){
        roomId = listRoom[i].getElementsByTagName("input")[0].name;
        if(roomIdDelete == roomId ){
            listRoom[i].style.display = "none";
        }
    }
}

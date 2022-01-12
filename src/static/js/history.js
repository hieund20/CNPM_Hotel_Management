let name;
let list_id = [];

function searchBookingRoom(e, element,user_role){
    if(e.keyCode == 13){
        hideRoom(user_role);
        text = element.value;
        element.value = "";
        l = document.getElementById("list-room");
        listRoom = l.getElementsByClassName("room-cart");
        flag = true;
        if(listRoom.length == 0){
            $('#exampleModalError').modal('show');
        }
        else{
            for (i= 0; i <= listRoom.length; i++){
            if(listRoom[i].name == text && list_id.indexOf(text) == -1){ // update 11/01/2020
                showInfoPayer(listRoom[i].name);
                listRoom[i].style.display = "";
                id =text;
                flag = false;
                if (user_role == 3){
                    document.getElementById("btn-check-in").disabled = false;
                }
            }
            if(i == listRoom.length -1 && flag == true){
                $('#exampleModalError').modal('show');
            }
        }
        }


    }


}


function hideRoom(user_role){
    l = document.getElementById("list-room");
    listRoom = l.getElementsByClassName("room-cart");
    for (i= 0; i < listRoom.length; i++){
        listRoom[i].style.display = "none";
    }
    if(user_role == 3){
        document.getElementById("btn-check-in").disabled = true;
    }
    info_default();

}

function info_default(){
    document.getElementById("if-name").innerHTML = ".............................................................";
    document.getElementById("if-numberphone").innerHTML = ".............................................................";
    document.getElementById("if-email").innerHTML = ".............................................................";
    document.getElementById("if-nation").innerHTML = ".............................................................";
    document.getElementById("total-money-history").innerHTML = "... VNĐ";
}

function showInfoPayer(id){
    event.preventDefault();
    fetch('/info-payer', {
        method: 'post',
        body: JSON.stringify({
            "id": id
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
        if(data[0] == true){
            document.getElementById("if-name").innerHTML = data[1];
            document.getElementById("if-numberphone").innerHTML = data[2];
            document.getElementById("if-email").innerHTML = data[3];
            document.getElementById("if-nation").innerHTML = data[4];
            document.getElementById("total-money-history").innerHTML = format(data[5], 'VNĐ');

        }
        else{
            alert("Hệ thống đang bảo trì! Vui lòng thử lại sau!");
        }
    }
    ).catch(err => {
            console.log(err);
        }
    );
}

function deleteBookingRoom(){
    event.preventDefault();
    list_id.push(id);
    fetch('/check-in', {
        method: 'post',
        body: JSON.stringify({
            "id": id
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
        if(data== true){
            room = document.getElementsByClassName("room-cart");
            for(r= 0; r < room.length; r++){
                room[r].style.display = "none";
            }
            document.getElementById("btn-check-in").disabled = true;
            document.getElementsByClassName("search-cart").value = "";
            info_default();
        }
        else{
            alert("Hệ thống đang bảo trì! Vui lòng thử lại sau!");
        }
    }
    ).catch(err => {
            console.log(err);
        }
    );
}

function format(n, currency) {
  return  n.toFixed(0).replace(/./g, function(c, i, a) {
    return i > 0 && c !== "." && (a.length - i) % 3 === 0 ? "," + c : c;
  }) + " " + currency;
}

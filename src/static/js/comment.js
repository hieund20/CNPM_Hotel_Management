function addComment(room_id) {
    let content = document.getElementById('commentId')
    if (content !== null) {
        fetch('/api/comments', {
            method: 'post',
            body: JSON.stringify({
                'room_id': room_id,
                'content': content.value
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => res.json()).then(data => {
            if (data.status == 201) {
                let c = data.comment

                let area = document.getElementById('commentArea')
                area.innerHTML = `
                    <div class="cmt comment flex distance">
                        <div class="col-md-1 col-xs-4 flex distance" style="display: flex;">
                            <p><img width="30" height="30"  class="rounded-circle"
                            src="https://res.cloudinary.com/dwgjmgf6o/image/upload/v1641091873/user_image/images_yjunll.jpg" /></p>
                            <p><b>${c.user.username}</b></p>
                        </div>

                        <div class="col-md-11 col-xs-8" style="display: block;">
                            <p>${ c.content }</p>
                            <p style="font-size: 10px;"><em>${c.created_date}</em></p>
                        </div>
                    </div>
                ` + area.innerHTML
                document.getElementById('commentId').value = ''
            } else if (data.status == 404)
                alert(data.err_msg)
        })
    }
}


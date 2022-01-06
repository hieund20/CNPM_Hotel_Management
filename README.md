# python_hotel_management

Bài tập lớn môn Công nghệ phần mềm

<b>1. Cách download code về, up code lên github</b> 

- Chạy lệnh git clone urlrepo để clone repository về (urlrepo là url của repository này)
  <br/>
  ---> Enter
- Để Push code lên github, chạy các lệnh: 
  <br/>
  git add .
  <br/>
  ---> Enter
  <br/>
  git commit -m"trong này nhớ nhập lý do push code lên nhé (VD: upload code/fix bug gì gì dó/add new featuer, ....)"
  <br/>
  ---> Enter
  <br/>
  git push
  <br/>
  ---> Enter
  <br/>
 Cuối cùng, để kiểm tra code đã lên repo thành công hay chưa, hãy gõ lệnh: git status nhé
- Quan trọng, nhớ chạy lệnh:
   <br/>
  git pull 
  <br/>
  ---> Enter
  <br/>
  để cập nhật code mới trước mỗi lần code nha !!
  
<b>2. Cách tạo nhánh (branch) để code cho tính năng của mình</b> 
- Clone từ nhánh develop: git clone -b <branch> <remote_repo> => Enter
- Đứng từ nhánh develop => Chạy lệnh git checkout -b <your branch> develop => Enter => Tạo hoàn tất
  <br/>
- Switch từ develop sang your branch: git checkout <your branch> => Enter
  <br/>
- Sau khi hoàn thành xong nhánh của mình, thực hiện merge your branch với develop, fix conflict và push lên YOUR BRANCH (Không được push lên develop). Các lệnh:
  <br/>
- git merge develop
  <br/>
- git add .
  <br/>
- git commit -m"write commit content"
  <br/>
- git push origin tên nhánh
  <br/>
- Sau khi push lên, tạo Megre Request (MR) để merge vào develop.

  <b>Lưu ý: Không được push code trực tiếp lên nhánh develop </b>
  <br/>
  <b>Mọi thao tác làm việc đều phải ở trên nhánh của mình</b>
  <br/>
  <b><i>Thanks team !</i></b>



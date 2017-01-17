<?php
namespace Admin\Controller;

use Think\Controller;

class LoginController extends Controller
{
    public function index() {
    $this->display();

    }

    public function login() {
      $admin = M('Admin');
      if(IS_POST) {
        $username = $_POST['username'];
        $password = $_POST['password'];
      }
      $res = $admin->where("username = '$username' && password = '$password'")->find();
     // dump($admin);
      if($res) {
         $this->success('登录成功...','Index/index');
      } else {
         $this->error('登录失败，请重新登录。');
      }
    }
}

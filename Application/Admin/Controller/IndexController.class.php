<?php
namespace Home\Controller;

use Think\Controller;

class IndexController extends Controller
{
    public function index()

    {
       $list = M('fygg')->select();
       $this->assign('list',$list);
       $this->display();
    }
}
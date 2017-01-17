<?php
namespace Home\Controller;

use Think\Controller;

class IndexController extends Controller
{
    public function index(){

    	// echo "chenggong";
       // $list = M('fygg')->limit(0,10)->select();
       // $this->assign('list',$list);
       $this->display();
    }



    public function get (){
    		$num = 1;
    	if ($num <= 1) {
    		$arr = 0;
    	}else{
    		$arr = $num*10;
    	}

    	$ret = M('fygg')->where()->limit($arr,10)->select();
    	// var_dump($ret);
    	$this -> ajaxreturn($ret);

    }
}
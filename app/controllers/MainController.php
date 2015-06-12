<?php 

class MainController extends BaseController{


	public function getMain()
	{
		
		return View::make('main.home');
	}
}
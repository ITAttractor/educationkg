<?php

class RegionController extends BaseController{

	public function allRegions()
	{
		return Region::all();
	}

	public function stats()
	{
		if(Input::get('order_param')){
			$results = Reg_rankings::orderBy(Input::get('order_param'), 'DESC')->get();
		}else{	
			$results = Reg_rankings::get();
		}
		return View::make('region.stats', compact('results'));
	}
}
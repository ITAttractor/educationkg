<?php

class RegionController extends BaseController{

	public function allRegions()
	{
		return Region::all();
	}
}
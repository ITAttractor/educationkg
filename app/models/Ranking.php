<?php

class Ranking extends Eloquent{

	protected $table = 'schools_ranking';

	public $timestamps = false;

	public $guarded = [];

	public function MaxByPlace()
	{
		
	}
}
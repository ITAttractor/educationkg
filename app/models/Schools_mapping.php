<?php

class Schools_mapping extends Eloquent{

	protected $table = 'schools_mapping';

	public $timestamps = false;

	public $guarded = [];

	public function schools2()
	{
		return $this->hasOne('School2', 'id', 'sch2_id');
	}
}
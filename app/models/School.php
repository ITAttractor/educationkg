<?php

class School extends Eloquent{

	public $timestamps = false;

	public $guarded = [];

	public function district()
    {
        return $this->belongsTo('District');
    }

    public function students()
	{
		return $this->hasMany('students');
	}


    public function ranking()
	{
		return $this->hasMany('ranking');
	}

	public function mapping()
	{
		return $this->hasOne('Schools_mapping', 'sch1_id', 'id');
	}

	static function avgBySchool($school_id, $lesson)
	{
		return Student::join('schools', 'schools.id', '=','students.school_id')->where('schools.id', $school_id)->avg($lesson);
	}

	static function avgByPlace($district_id = null, $region_id = null, $lesson)
	{
		$query =  Student::
			join('schools', 'schools.id', '=','students.school_id')
			->join('districts', 'districts.id', '=', 'schools.district_id')
			->join('regions', 'regions.id', '=', 'districts.region_id');
		if($district_id){
			$query = $query->where('districts.id', $district_id);
		}	
		if($region_id){
			$query = $query->where('regions.id', $region_id);
		}	

		return $query->avg($lesson);
	}
}
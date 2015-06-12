<?php

class StudentController extends BaseController{

	public function getGrade()
	{
		$lessons = Student::$lessons;
		return View::make('student.grade', compact('lessons'));
	}

	public function checkGrade()
	{
		$mark = Input::get('mark');
		$lesson = Input::get('lesson');
		$region_ids = Input::get('region') ? [Input::get('region')] : Region::lists('id');
		$dist_ids = District::whereIn('region_id', $region_ids)->lists('id');
		$district_ids = Input::get('district') ? [Input::get('district')] : $dist_ids;
		$sch_ids = School::whereIn('district_id', $district_ids)->lists('id');
		$school_ids = Input::get('school') ? [Input::get('school')] : $sch_ids;
	 	 
	 	$place = Student::whereIn('school_id', $school_ids)->where($lesson, '>', $mark)->count();
	 	$all = Student::whereIn('school_id', $school_ids)->whereNotNull($lesson)->count();
	 	$min = Student::whereIn('school_id', $school_ids)->min($lesson);
	 	$max = Student::whereIn('school_id', $school_ids)->max($lesson);

	 	$result['min'] 		= 	$min;
	 	$result['max'] 		= 	$max;
	 	$result['place'] 	= 	$place + 1; 
	 	$result['all'] 		=	$all ;
	 	return json_encode($result);
	}
}
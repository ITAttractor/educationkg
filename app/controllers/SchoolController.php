<?php

class SchoolController extends BaseController{

	public function showSchool($school_id)
	{
		$result = School::join('students', 'students.school_id', '=', 'schools.id')
					->where('schools.id', $school_id)
					->select('schools.*',
						DB::raw('AVG(students.math) as math'), 
						DB::raw('AVG(students.physics) as physics'),
						DB::raw('AVG(students.chemistry) as chemistry'))->first();
	/*	echo "<pre>"; print_r($result); echo "</pre>";
		exit;*/
		return View::make('school.show', compact('result'));

	}
}
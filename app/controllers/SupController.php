<?php

class SupController extends BaseController{

	public function getStudentsWhereDistrict($dist_id)
	{
		$student =  Student::with(array('schools' => function($query) use ($dist_id) {
	          $query->where('district_id', '=', $dist_id);
		 }))->get();
		echo "<pre>"; print_r($student); echo "</pre>";
		exit;
	}

	public function readPropertyByVar()
	{
		foreach($student->lessons as $lesson){
			print $lesson . ($student->$lesson);
			print '<br>';
		}
	}

	public function loadXcell()
	{
		Excel::load('Dataset.xlsx', function($reader) {
			 $results = $reader->first();
			 echo "<pre>"; print_r($results); echo "</pre>";
			 exit;
		})->get();
	}

	public function countByParams(){
		$dist_id = Input::get('district');
		$lesson = Input::get('lesson');

		$result =  Student::join('schools', 'students.school_id', '=', 'schools.id')
			->where('schools.district_id', $dist_id)
			->avg($lesson);
		echo "<pre>"; print_r($result); echo "</pre>";
		exit;
	}

	public function distStudents($dist_id){
		$result = Student::join('schools', 'students.school_id', '=', 'schools.id')
			->where('schools.district_id', $dist_id)->get();
			echo "<pre>"; print_r($result); echo "</pre>";
			exit;
	}

	public function avgMult($dist_id)
	{
		$result =  Student::join('schools', 'students.school_id', '=', 'schools.id')
			->where('schools.district_id', $dist_id);
		foreach(Student::$lessons as $lesson){

			$results[] = $lesson. ':'.$result->avg($lesson);
		}
		echo "<pre>"; print_r($results); echo "</pre>";
		exit;
	}

	public function avgByDistSchool($dist_id)
	{
		$results = District::where('districts.id', $dist_id)
			->join('schools', 'schools.district_id', '=', 'districts.id')
			->join('students', 'students.school_id', '=', 'schools.id')
			->groupBy('schools.id')
			->select('schools.title', 
				DB::raw('AVG(students.math) as math'), 
				DB::raw('AVG(NULLIF(students.physics ,0)) as physics'),
				DB::raw('AVG(students.chemistry) as chemistry')/*,
				DB::raw('AVG(students.geometry) as geometry'),
				DB::raw('AVG(students.biology) as biology'),
				DB::raw('AVG(students.geography) as geography'),
				DB::raw('AVG(students.history) as history'),
				DB::raw('AVG(students.english_lang) as english_lang'),
				DB::raw('AVG(students.german_lang) as german_lang'),
				DB::raw('AVG(students.french_lang) as french_lang'),
				DB::raw('AVG(students.kyrgyz_lang) as kyrgyz_lang'),
				DB::raw('AVG(students.russian_lang) as russian_lang'),
				DB::raw('AVG(students.uzbek_lang) as uzbek_lang'),
				DB::raw('AVG(students.informatics) as informatics'),
				DB::raw('AVG(students.civics) as civics')*/)
			->get()->toJson();
			echo "<pre>"; print_r($results); echo "</pre>";
			exit;
	}

			
}
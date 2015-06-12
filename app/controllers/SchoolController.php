<?php

class SchoolController extends BaseController{

	public function showSchool($school_id)
	{

		$school = School::find($school_id);
		$map = School::find($school_id)->mapping;
		if($map){
			$school_data = School2::find($map->sch2_Id);
		}else{
			$school_data = null;
		}

		$result = School::join('students', 'students.school_id', '=', 'schools.id')
					->where('schools.id', $school_id)
					->select('schools.*',
						DB::raw('AVG(students.history) as history'), 
						DB::raw('AVG(students.kyrgyz_lang) as kyrgyz_lang'), 
						DB::raw('AVG(students.biology) as biology'), 
						DB::raw('AVG(students.russian_lang) as russian_lang'),
						DB::raw('AVG(students.math) as math'), 
						DB::raw('AVG(students.geography) as geography'),
						DB::raw('AVG(students.chemistry) as chemistry'),
						DB::raw('AVG(students.english_lang) as english_lang'))
					->first();

		$avg = [$result->history, $result->kyrgyz_lang, $result->biology, $result->russian_lang, $result->math, $result->geography, $result->chemistry, $result->english_lang];
		
		$country_avg = Student::select(
						DB::raw('AVG(students.history) as history'), 
						DB::raw('AVG(students.kyrgyz_lang) as kyrgyz_lang'), 
						DB::raw('AVG(students.biology) as biology'), 
						DB::raw('AVG(students.russian_lang) as russian_lang'),
						DB::raw('AVG(students.math) as math'), 
						DB::raw('AVG(students.geography) as geography'),
						DB::raw('AVG(students.chemistry) as chemistry'),
						DB::raw('AVG(students.english_lang) as english_lang'))
			->get()[0];

		$all_avg = [$country_avg->history, $country_avg->kyrgyz_lang, $country_avg->biology, $country_avg->russian_lang, $country_avg->math, $country_avg->geography, $country_avg->chemistry, $country_avg->english_lang];


		$stud_num = Student::where('school_id', $school_id)->count();

		Javascript::put(['average' => $avg, 'all_avg' => $all_avg , 'stud_num' => $stud_num]);

		return View::make('school.show', compact('result', 'school_data'));

	}

	public function getTop()
	{
		$districts = District::get();
		$regions = Region::get();
		foreach(Student::$lessons as $lesson){
			$results[$lesson] = Ranking::select('schools_ranking.*','schools.*',
							DB::raw('MAX(schools_ranking.avg_'.$lesson.') as '.$lesson.''))
			->join('schools', 'schools.id', '=', 'schools_ranking.school_id')
			->first();
		}

	
		/*echo "<pre>"; print_r($results); echo "</pre>";
		exit;*/

		$lessons = Student::$lessons;
		return View::make('school.top' , compact('results', 'districts', 'regions', 'lessons'));
	}

	public function stats()
	{
		return View::make('school.stats');
	}

	public function jsonTop()
	{
		$query = Ranking::join('schools', 'schools.id', '=','schools_ranking.school_id')
			->join('districts', 'districts.id', '=', 'schools.district_id')
			->join('regions', 'regions.id', '=', 'districts.region_id')
			->whereNotNull('schools_ranking.avg_'. Input::get('lesson'))
			->select('schools.*', 'schools_ranking.*');
		if(Input::get('region')){
			$query = $query->where('districts.region_id', Input::get('region'));
		}

		if(Input::get('district') > 0){
			$query = $query->where('districts.id', Input::get('district'));
		}
		return $query->orderBy('avg_' . Input::get('lesson'), 'DESC')->take(10)->get();
	}
}
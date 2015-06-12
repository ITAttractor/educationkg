<?php

class DistrictController extends BaseController{

	public function allDistricts(){
		return District::all();
	}

	public function getDistricts($id)
	{
		return District::where('region_id', $id)->get();
	}

	public function showDistrictData($dist_id)
	{
		$request = District::where('districts.id', $dist_id)
			->join('schools', 'schools.district_id', '=', 'districts.id')
			->join('students', 'students.school_id', '=', 'schools.id')
			->groupBy('schools.id')
			->select('schools.title', 'schools.id',
				DB::raw('AVG(students.math) as math'), 
				DB::raw('AVG(students.physics) as physics'),
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
				DB::raw('AVG(students.civics) as civics')*/);

		if(Input::get('order_param')){
			$results = $request->orderBy(Input::get('order_param'),'DESC')->get();
		}else{
			$results = $request->get();
		}

		return View::make('district.all', compact('results'));
	}

	public function getDistrictSchools($dist_id)
	{
		return School::where('district_id', $dist_id)->get();
	}
}
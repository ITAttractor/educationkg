<?php
use Goodby\CSV\Export\Standard\Exporter;
use Goodby\CSV\Export\Standard\ExporterConfig;
use Goodby\CSV\Import\Standard\Interpreter;
use Goodby\CSV\Import\Standard\Lexer;
use Goodby\CSV\Import\Standard\LexerConfig;
/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the Closure to execute when that URI is requested.
|
*/

Route::get('/', 'MainController@getMain');

Route::get('/districtstuds/{id}', 'SupController@getStudentsWhereDistrict');
Route::get('distMax', 'SupController@countByParams');
Route::get('district/students/{id}', 'SupController@distStudents');
Route::get('all/average/{id}', 'SupController@avgMult');
Route::get('district/show/{id}', 'DistrictController@showDistrictData');
Route::get('district/avg/{id}', 'SupController@avgByDistSchool');
Route::get('district/all', 'DistrictController@allDistricts');
Route::get('district/{id}', 'DistrictController@getDistricts');
Route::get('region/all', 'RegionController@allRegions');
Route::get('school/{id}',['uses' => 'SchoolController@showSchool', 'as' => 'school']);

Route::get('student/grade', 'StudentController@getGrade');
Route::get('district/schools/{id}', 'DistrictController@getDistrictSchools');
Route::get('student/checkgrade', 'StudentController@checkGrade');
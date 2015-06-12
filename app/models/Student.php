<?php 

class Student extends Eloquent{

	public $timestamps = false;

	public $guarded = ['id'];

	public static $lessons = ['math', 'physics', 'chemistry', 'geometry', 'biology', 'geography', 'history', 'english_lang', 'german_lang', 'french_lang', 'kyrgyz_lang', 'russian_lang', 'uzbek_lang', 'informatics', 'civics'];

	public function schools()
    {
        return $this->belongsTo('School');
    }
}
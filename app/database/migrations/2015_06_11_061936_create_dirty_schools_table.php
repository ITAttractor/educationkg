<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateDirtySchoolsTable extends Migration {

	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up()
	{
		Schema::create('dirty_schools', function($table)
		{
		    $table->integer('id');
		    $table->string('col1')->nullable();
		    $table->string('col2')->nullable();
		    $table->string('col3')->nullable();
		    $table->string('col4')->nullable();
		    $table->string('col5')->nullable();
		    $table->string('col6')->nullable();
		    $table->string('col7')->nullable();
		    $table->string('col8')->nullable();
		    $table->string('col9')->nullable();
		    $table->string('col10')->nullable();
		    $table->string('col11')->nullable();
		});
	}

	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down()
	{
		//
	}

}

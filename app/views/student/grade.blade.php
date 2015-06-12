@extends('layout')

@section('content')
	
	<br><br><br>
	<div class="col-md-4"></div>
	<div class="col-md-4 theapp">
		
		
		<form class="form-inline">
		  <div class="form-group">
		    <input type="text" class="mark form-control" placeholder="оценка">
		  </div>
		  <div class="form-group">
		    <select class="lessons form-control">
				@foreach($lessons as $lesson)
				<option value="{{$lesson}}">{{$lesson}}</option>
				@endforeach
			</select>
		  </div>
		</form>
		<select class="regions form-control">
			
		</select> 
		<p></p>

		<p></p>

		<button class="check btn btn-default">check</button><br><br>
	</div>

	<script>
		$(document).ready(function(){
			$.get(school.home_url + '/region/all', function(data){
				$('.regions').append('<option value="null"></option>')
				$.each(data, function(key, value){
					$('.regions').append('<option value=' + value.id + '>' + value.title + '</option>')
				})
			});

			$('.regions').change(function(){
				$('.districts')
				    .remove()
				    .end()

				$('.schools')
				    .remove()
				    .end()    
				$('.regions').after('<select class="districts form-control app-districts"></select>')
				
				$.get(school.home_url + '/district/' + $(this).val(), function(data){
					$('.districts').append('<option value=""></option>')
					$.each(data, function(key, value){
						$('.districts').append('<option value=' + value.id + '>' + value.title + '</option>')
					})
				});
			})

			$(document).on('change', '.districts', function(){

				$('.schools')
				    .remove()
				    .end()
				$('.app-districts').after('<select class="schools form-control"></select>')
				
				$.get(school.home_url + '/district/schools/' + $(this).val(), function(data){
					$.each(data, function(key, value){
						$('.schools').append('<option value=' + value.id + '>' + value.title + '</option>')
					})
				});
			})

			$('.mark').on('input', function(){
				var info = {
					mark : $('.mark').val(),
					lesson : $('.lessons').val(),
					region : $('.regions').val(),
					district: $('.districts').val(),
					school: $('.schools').val()
				}

				$.get(school.home_url + '/student/checkgrade', info, function(result){
					data = $.parseJSON(result);
					$('.the-result').remove();
					$('.check').after('<p class="the-result" >Ваш результат занимает ' + data.place + ' место среди ' + data.all + ' сдавших</p>');
				});
			})
		});
	</script>
@stop
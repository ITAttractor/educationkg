@extends('layout')

@section('stylesheets')
	<!-- <link rel="stylesheet" type="text/css" href="{{asset('css/datatables.css')}}"> -->
@stop
@section('content')
	
	<br>
	<div class="rsr"></div>
	<div class="col-md-4"></div>
	<div class="col-md-4">

		<select class="regions form-control">
			
		</select>

		<br>
		<select class="districts form-control">
			
		</select>

	</div>
	<script type="text/javascript">
		$(document).ready(function(){
			$.get(school.home_url + '/region/all', function(data){
				window.data = data;
				$.each(data, function(key, value){
					$('.regions').append('<option value=' + value.id + '>' + value.title + '</option>')
				})


			});

			$('.regions').change(function(){
				$('.districts')
				    .find('option')
				    .remove()
				    .end()
				$.get(school.home_url + '/district/' + $(this).val(), function(data){
					$.each(data, function(key, value){
						$('.districts').append('<option value=' + value.id + '>' + value.title + '</option>')
					})
				});
			})

			$('.districts').change(function(){
				window.location.href = (school.home_url + '/district/show/' + $(this).val());
					
			})

		});
	</script>
@stop
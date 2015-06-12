@extends('layout')

@section('content')
	
	
	<br><br><br>
	<div class="col-md-4"></div>
	<div class="col-md-4 theapp">
		
		
		<div class="form-inline">
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
		</div>
		<select class="regions form-control">
			
		</select> 
		<p></p>

		<p></p>

		<button class="check btn btn-default">Найти своё место в рейтинге</button><br><br>

		<canvas id="myChart" width="400" height="400"></canvas>
		<p style="color:white" height="400">as</p>
	</div>
	<p></p>
	<script>
		
	var data = {
    labels: ["Результаты - Мин, Ваш, Макс"],
    datasets: [
        {
            label: "Минимум",
            fillColor: "red",
            data: [0]
        },
        {
            label: "Ваш результат",
            fillColor: "yellow",
            data: [0]
        },
        {
            label: "Максимум",
            fillColor: "green",
            data: [0]
        }
    ]
};
	var ctx = document.getElementById("myChart").getContext("2d");
	var myBarChart = new Chart(ctx).Bar(data);

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
					$('.schools').append('<option value=""></option>')
					$.each(data, function(key, value){
						$('.schools').append('<option value=' + value.id + '>' + value.title + '</option>')
					})
				});
			})


			$('.check').on('click', function(e){

				var info = {
					mark : $('.mark').val(),
					lesson : $('.lessons').val(),
					region : $('.regions').val(),
					district: $('.districts').val(),
					school: $('.schools').val()
				}

				$.get(school.home_url + '/student/checkgrade', info, function(result){
					data = $.parseJSON(result);
					console.log(data);
					$('.the-result').remove();
					myBarChart.datasets[0].bars[0].value = data.min;
					myBarChart.datasets[1].bars[0].value = $('.mark').val();
					myBarChart.datasets[2].bars[0].value = data.max;
					myBarChart.update();
					$('.check').after('<p class="the-result" >Ваш результат занимает ' + data.place + ' место среди ' + data.all + ' сдавших</p>');
				});
			});
			

		});
	</script>

@stop
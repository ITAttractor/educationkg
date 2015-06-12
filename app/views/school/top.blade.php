@extends('layout')

@section('content')
	
	<div class="col-md-2"></div>
	<div class="col-md-8">

	    <select type="text" class="regions form-control"  >
	    	<option value="">Выберите Регион</option>
	    	@foreach($regions as $region)
	    		<option value="{{$region->id}}">{{$region->title}}</option>
	    	@endforeach
	    </select>

		<br><br>
	    <select name="" class="lessons form-control">
	    	<option value="">Выберите предмет</option>
			@foreach($lessons as $lesson)
				<option value="{{$lesson}}">{{$lesson}}</option>
			@endforeach
		</select> 
		<br><br>
		<p class="results">
			<table class="table table-bordered">
				<thead>
					<tr>
						<td>Место</td>
						<td>Школа</td>
						<td>Ср. Бал</td>
					</tr>
				</thead>
				<tbody>
					
				</tbody>
			</table>
		</p>
	</div>
	<p style="color:white" height="400">as</p>
	<script>

	$(document).ready(function(){
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


		});

		$('.lessons').on('change',function(){

			var info = {
					lesson : $('.lessons').val(),
					region : $('.regions').val(),
					district: $('.districts').val()
				}

			$.get(school.home_url + '/school/jsonGetTop', info,function(result){
				console.log(result);
				$('tbody').empty();
				$.each(result, function(key, value){
					key += 1;
					var lesson = 'avg_' + $('.lessons').val();
					console.log(value);
					$('tbody').append('<tr><td>'+ key +' <td> <a href="'+school.home_url+'/school/'+value.id+'">' + value.title + ' </a>  <td>'+ value[lesson] +'</tr>')
				})
			})
		})
	});
	</script>
@stop
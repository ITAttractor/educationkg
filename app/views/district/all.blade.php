@extends('layout')


@section('content')
	<br><br><br>
	<div class="col-md-2"></div>
	<div class="col-md-8">
		<table class="table">
			<thead>
				<td><a href="#">Имя</a></td>
				<td><a href="?order_param=math">Математика</a></td>
				<td><a href="?order_param=physics">Физика</a></td>
				<td><a href="?order_param=chemistry">Химия</a></td>
			</thead>
			@foreach($results as $result)
			<tr>
				<td><a href="{{route('school', $result->id)}}">{{$result->title}}</a></td>
				<td>{{$result->math}}</td>
				<td>{{$result->physics}}</td>
				<td>{{$result->chemistry}}</td>
			</tr>
			@endforeach
		</table>
	</div>
@stop
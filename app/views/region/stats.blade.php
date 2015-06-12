@extends('layout')

@section('content')
<style>
	.table td {
   text-align: center;   
}
</style>
	<div class="col-md-1"></div>
	<div class="col-md-10">
		<table class="table table-bordered">
		
		<thead>
			<tr class="active">
				<td><a href="?order_param=region_title">Область</a></td>
				<td><a href="?order_param=school_total">Кол-во школ</a></td>
				<td><a href="?order_param=sum_total_students">Кол-во учеников</a></td>
				<td><a href="?order_param=sum_total_teachers">Кол-во учителей</a></td>
				<td><a href="?order_param=students_per_teacher">Кол-во учеников <br> на 1 учителя</a></td>
				<td><a href="?order_param=sum_total_budget">Суммарный бюджет области</a></td>
				<td><a href="?order_param=budget_per_student">Бюджет на одного ученика</a></td>
			</tr>
		</thead>
		<tbody>
			@foreach($results as $result)
				<tr>
					<td>{{$result->region_title}}</td>
					<td>{{$result->school_total}}</td>
					<td>{{$result->sum_total_students}}</td>
					<td>{{$result->sum_total_teachers}}</td>
					<td>{{$result->students_per_teacher}}</td>
					<td>{{number_format($result->sum_total_budget, 2)}}</td>
					<td>{{number_format($result->budget_per_student, 2)}}</td>
				</tr>
			@endforeach
		</tbody>
	</table>
	</div>
@stop
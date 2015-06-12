@extends('layout')

@section('content')
	<p></p><p></p><p></p>
	<div class="col-md-2"></div>
	<div class="col-md-8">
		<div class="panel panel-primary">
			<div class="panel-heading">{{$result->title}}</div>
			<div class="panel-body">
				<p><i class="fa fa-building"></i> {{$result->address}}</p>
				<p><i class="fa fa-phone-square"></i> {{$result->phone}}</p>

			</div>
		</div>
	</div>
@stop

@section('stylesheets')
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
@stop
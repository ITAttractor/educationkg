@extends('layout')

@section('content')
	<p></p><p></p><p></p>
	<div class="col-md-2"></div>
	<div class="col-md-8">
		<div class="panel panel-primary">
			<div class="panel-heading">{{$result->title}}</div>
			<div class="panel-body">
				<div class="row">
					<div class="col-md-6">
						@if(@$school_data->dean_name)
						<p><i class="fa fa-suitcase fa-fw"></i> Директор {{@$school_data->dean_name}} </p>
						@else
						<p><i class="fa fa-suitcase fa-fw"></i>Директор -<span style="color:red">  нет данных</span> </p>
						@endif
						@if(@$school_data->total_teachers)
						<p><i class="fa fa-graduation-cap fa-fw"></i> {{@$school_data->total_teachers}} преподавателей</p>
						@else
						<p><i class="fa fa-graduation-cap fa-fw"></i> Преподаватели - <span style="color:red">нет данных</span></p>
						@endif
						@if(@$school_data->total_students)
						<p><i class="fa fa-users fa-fw"></i> {{@$school_data->total_students}} учеников</p>
						@else
						<p><i class="fa fa-users fa-fw"></i> Ученики - <span style="color:red">нет данных</span></p>
						@endif
						<p><i class="fa fa-phone-square fa-fw"></i> 
						@if(@$result->phone)
							{{@$result->phone}}
						@else
							<span style="color:red">нет данных</span>
						@endif	
						</p>
						<p><i class="fa fa-building fa-fw"></i> 
							@if(@$result->address)
								{{@$result->address}}
							@else
								<span style="color:red">нет данных</span>
							@endif	
						</p>
					</div>
					<div class="col-md-6">
						<p> <strong>Местный бюджет</strong>:
							@if(@$school_data->budget_local > 0)
								{{number_format(@$school_data->budget_local)}} тыс. сом  <small style="color:blue">({{number_format(@$school_data->percent_local, 2)
									
									}} %)</small>
							@else
								<span style="color:red">нет данных</span>
							@endif	
							
						</p>
						<p><strong> Республиканский бюджет</strong>:
							@if(@$school_data->budget_capital > 0)
								{{number_format(@$school_data->budget_capital)}} тыс. сом  <small style="color:blue">({{number_format(@$school_data->percent_capital, 2)}} %)</small>
							@else
								<span style="color:red">нет данных</span>
							@endif	
							
						</p>
						<hr>
						<p> <strong>Суммарный бюджет</strong>:
							@if(@$school_data->total_budget > 0)
								{{number_format(@$school_data->total_budget)}} тыс. сом 
							@else
								<span style="color:red">нет данных</span>
							@endif	
							
						</p>
						<p> <strong>Расходы на одного ученика из бюджета</strong>:
							@if(@$school_data->total_budget > 0 & @$school_data->total_students > 0)
								{{number_format($school_data->total_budget * 1000 / $school_data->total_students)}} сом 
							@else
								<span style="color:red">нет данных</span>
							@endif	
							
						</p>
					</div>
				</div>

				<div id="container" style="min-width: 400px; height: 400px; margin: 0 auto">
					
				</div>
			</div>
		</div>
	</div>
<div class="row"></div>
<script>
var averageNums = school.average.map(Number);
var allAvg = school.all_avg.map(Number);
	$(function () {
    $('#container').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Средние результаты НЦТ по школе (сдавало '+ school.stud_num+' учеников)'
        },
        xAxis: {
            categories: ['История', 'Кыргызский язык', 'Биология', 'Русский язык', 'Математика', 'География', 'Химия', 'Английский язык']
        },
        yAxis: {
            allowDecimals: false,
            title: {
                text: 'баллы'
            }
        },
        series: [{
            name: 'Среднее по школе',
            data: averageNums
        }, {
            name: 'Среднее по стране',
            data: allAvg
        }]
    });
});
</script>
	<script src="http://code.highcharts.com/highcharts.js"></script>
	<script src="http://code.highcharts.com/modules/exporting.js"></script>
@stop

@section('stylesheets')
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
@stop
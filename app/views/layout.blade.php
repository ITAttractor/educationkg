<!DOCTYPE html>
<html>
<head>
	<title></title>
	<meta charset="UTF-8">
	<link rel="stylesheet" type="text/css" href="{{asset('css/bootstrap.css')}}">
	@yield('stylesheets')

	<script type="text/javascript" src="{{asset('js/jquery.js')}}"></script>
	
	<script type="text/javascript" src="{{asset('js/raphael.js')}}"></script>
</head>
<body>
	<nav class="navbar navbar-default">
	  <div class="container-fluid">
		  <ul class="nav navbar-nav">
		  	<li><a href="{{URL::to('/')}}">Поиск по району</a></li>
		  	<li><a href="{{URL::to('student/grade')}}">Проверить результат</a></li>
		  	<li><a href="#">Link</a></li>
		  </ul>
	  </div>
	</nav>
	@yield('content')
	<script type="text/javascript" src="{{asset('js/datatables.js')}}"></script>
	<script type="text/javascript" src="{{asset('js/datatables.bootstrap.js')}}"></script>	
	<script type="text/javascript" src="{{asset('js/bootstrap.js')}}"></script>
</body>
</html>
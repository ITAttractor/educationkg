$(document).ready(function () {
        var resultController = new ResultController();
        resultController.searchResultsUrl = urls.searchResult;
        resultController.getResultUrl = urls.getResult;
        resultController.popupContainer = $(".popup-person");
        resultController.searchResultsContainer = $(".pupil-list");
        resultController.init();

        var schoolGeo = new SchoolGeo();
        schoolGeo.url = urls.schoolGeoData;
        schoolGeo.mapLegendContainer = $(".map-legend");
        schoolGeo.init();

        var chartDrawer = new ChartDrawer();
        chartDrawer.popupContainer = $(".popup-school");
        chartDrawer.urlPattern = urls.schoolChartData;
        chartDrawer.initLinks();
        chartDrawer.initCloseButton();

        var topSchools = new TopSchools();
        topSchools.container = $(".block-table-best-school");
        topSchools.getDistrictsUrl = urls.districts;
        topSchools.topSchoolsUrl = urls.topSchoolsUrl;
        topSchools.chartDrawer = chartDrawer;
        topSchools.init();

        var loadAboutInfo = function () {
            $.ajax({
                url: '/pages/about/',
                type: 'get',
                success: function (data) {
                    $(".popup-person").html(data);
                    $(".popup-person").addClass('active');
                }
            })
        };

        $("#about-project").on("click", function (event) {
            loadAboutInfo();
        });

        $.scrollIt({
            upKey: 38,
            downKey: 40,
            easing: 'linear',
            scrollTime: 600,
            onPageChange: null,
            topOffset: -120
        });

        if (window.location.hash) {
            var hash = window.location.hash.substring(1); //Puts hash in variable, and removes the # character
            if (hash == 'about') {
                loadAboutInfo()
            }
        }
    });
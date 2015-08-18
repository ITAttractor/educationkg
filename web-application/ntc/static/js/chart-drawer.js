var ChartDrawer = function () {
    var $this = this;
    this.container = null;
    this.urlPattern = null;
    var options = {
        scaleOverride: true,
        scaleSteps: 5,
        scaleStepWidth: 6,
        scaleFontSize: 10,
        barShowStroke: false,
        barValueSpacing: 20
    };

    var data = {
        labels: null,
        datasets: [
            {
                label: "По стране",
                fillColor: "#666666",
                strokeColor: "#666666",
                highlightColor: "#666666",
                highlightStroke: "#666666",
                data: null
            },
            {
                label: "По школе",
                fillColor: "#ff9d29",
                strokeColor: "#ff9d29",
                highlightColor: "#ff9d29",
                highlightStroke: "#ff9d29",
                data: null
            }

        ]
    };

    this.drawChart = function () {
        var ctx = $this.container.find("canvas").get(0).getContext("2d");
        data.labels = chartData.subjects;
        data.datasets[0].data = chartData.country_averages;
        data.datasets[1].data = chartData.school_averages;
        new Chart(ctx).Bar(data, options)
    };

    this.assignDataAndDraw = function (data) {
        $this.container.html(data);
        $this.drawChart();
    };

    this.loadChartDataForSchool = function (schoolId) {
        var url = $this.urlPattern.replace('0', schoolId);
        $.ajax({
            url: url,
            type: "get",
            success: $this.assignDataAndDraw
        })
    };

    this.initLinks = function() {
        $(".school-link").on("click", function(event) {
            event.preventDefault();
            var schoolId = $(this).data("school-id")
            $this.loadChartDataForSchool(schoolId)
        })
    };


};
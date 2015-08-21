var TopSchools = function () {
    var $this = this;
    this.container = null;
    this.getDistrictsUrl = null;
    this.topSchoolsUrl = null;
    this.chartDrawer = null;

    var selectedRegionSpan = $("#selected-region");
    var selectedDistrictSpan = $("#selected-district");
    var selectedSubjectSpan = $("#selected-subject");

    this.initDropdowns = function () {
        $('.s-filter').on("click", function (event) {
            event.preventDefault();
            $(this).closest(".s-filter").toggleClass('active');
            return false;
        });

        $("body").on("click", function () {
            $(".s-filter").removeClass("active");
        });

        $(".s-dropdown").perfectScrollbar()
    };

    this.initSchoolLinks = function() {
        $(".block-table-best-school").on("click", ".school-name", function(event) {
            event.preventDefault();
            var school_id = $(this).data("school-id");
            $this.chartDrawer.loadChartDataForSchool(school_id);
        })
    };

    this.getDistricts = function (region_id) {
        $.ajax({
            "url": $this.getDistrictsUrl,
            "type": "get",
            data: {
                "region_id": region_id
            },
            success: $this.appendDistricts
        })
    };


    this.appendDistricts = function (districts) {
        var result_html_array = [];
        for (var district in districts) {
            var html = "<li data-district-id='" + districts[district].id + "'>" + districts[district].title + "</li>"
            result_html_array.push(html)
        }
        $("#district-select").html(result_html_array.join(""));
        selectedDistrictSpan.data("district-id", districts[0].id);
        selectedDistrictSpan.html(districts[0].title);
        $this.loadTopSchools();
    };

    this.initRegionDropdownItems = function () {
        $("#region-select").on("click", 'li', function (event) {
            $(this).closest(".s-filter").toggleClass('active');
            var region_id = $(this).data("region-id");
            selectedRegionSpan.data('region-id', region_id);
            selectedRegionSpan.html($(this).html());
            $this.getDistricts(region_id);
            $this.loadTopSchools();
            return false;
        });
    };

    this.initDistrictDropdownItems = function () {
        $("#district-select").on("click", 'li', function () {
            var district_id = $(this).data("district-id");
            selectedDistrictSpan.data('district-id', district_id);
            selectedDistrictSpan.html($(this).html());
            $(this).closest(".s-filter").toggleClass('active');
            $this.loadTopSchools();
            return false;
        });
    };

    this.initSubjectDropdownItems = function() {
        $("#subject-select").on("click", 'li', function() {
            var subject_key = $(this).data('subject-key');
            console.log(subject_key);
            selectedSubjectSpan.data('subject-key', subject_key);
            selectedSubjectSpan.html($(this).html());
            $(this).closest(".s-filter").removeClass('active');
            $this.loadTopSchools();
            return false;
        });
    };

    this.loadTopSchools = function () {
        $.ajax({
            url: $this.topSchoolsUrl,
            type: "get",
            data: {
                "district_id": $("#selected-district").data("district-id"),
                "subject_key": $("#selected-subject").data("subject-key")
            },
            success: $this.showTopSchools
        })
    };

    this.showTopSchools = function (data) {
        $this.container.html(data);
    };

    this.init = function () {
        $this.initDropdowns();
        $this.initRegionDropdownItems();
        $this.initDistrictDropdownItems();
        $this.initSubjectDropdownItems();
        $this.loadTopSchools();
        $this.initSchoolLinks();
    }

};
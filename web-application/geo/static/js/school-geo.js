var SchoolGeo = function () {
    var $this = this;
    this.url = null;
    this.mapLegendContainer = null;

    this.setData = function (data) {
        $this.data = data;
    };

    this.getData = function () {
        $.ajax({
            "type": "get",
            "url": $this.url,
            success: $this.setData
        })
    };

    this.initMap = function () {
        $("path").on("mouseover", function () {
            var slug = $(this).data('slug');
            var school_count = $this.data[slug]['school_count'];
            var _case = $this.data[slug]['case'];
            var total_schools = $this.data['total_schools'];
            var percents = (school_count/total_schools*100).toFixed(2);
            var school_case = $this.data[slug]['school_case'];
            var html = '<div class="map-leg-head"><h3>'+school_count+' '+school_case+'</h3>\
                    <span class="map-distr">' + _case + '</span>\
                    <span>~'+percents+'%</span>\
                </div>\
                <span>от общего количества школ</span>\
                <div class="meter">\
                    <span style="width: '+percents+'%"></span>\
                </div>';
            $this.mapLegendContainer.html(html);
        })
    };

    this.init = function () {
        if (!$this.url) {
            throw "URL was not set";
        }
        if (!$this.mapLegendContainer) {
            throw "mapLegendContainer was not set"
        }

        $this.getData();
        $this.initMap();
    };
};

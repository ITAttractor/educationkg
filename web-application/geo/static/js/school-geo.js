var SchoolGeo = function () {
    var $this = this;
    this.url = null;

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
            var total_schools = $this.data['total_schools'];
            console.log("total:" + total_schools + " region:" + school_count + " slug:"+slug);
        })
    };

    this.init = function () {
        if (!$this.url) {
            throw "URL was not set";
        }

        $this.getData();
        $this.initMap();
    };
};

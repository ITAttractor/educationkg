var SchoolSearcher = {
    params: {
        searchUrl: null,
        schoolsContainer: null,
        titleInput: null,
        regionsInputs: null,
        districtsInputs: null,
        paginationLinkSelector: null
    },

    getDistrictsByRegionId: function (regionId) {
        var selector = '[data-region-id="' + regionId + '"]';
        return this.params.districtsInputs.filter(selector);
    },

    getRegionByRegionId: function (regionId) {
        var selector = '[value="' + regionId + '"]';
        return this.params.regionsInputs.filter(selector);
    },

    init: function (params) {
        $.extend(this.params, params);
        this.bindTitleInput();
        this.bindDistrictsInputs();
        this.bindRegionsInputs();
        this.bindPaginationLinks();
    },

    bindTitleInput: function () {
        this.params.titleInput.on('input', this.search.bind(this));
    },

    bindDistrictsInputs: function () {
        var $this = this;
        this.params.districtsInputs.on('change', this.search.bind(this));
        this.params.districtsInputs.on('change', function () {
            var regionId = $(this).data('region-id');
            var region = $this.getRegionByRegionId(regionId);
            var districtsInputsInRegion = $this.getDistrictsByRegionId(regionId);
            if (districtsInputsInRegion.length == districtsInputsInRegion.filter(':checked').length) {
                region.prop('checked', true);
            } else {
                region.prop('checked', false);
            }
        });
    },

    bindRegionsInputs: function () {
        var $this = this;
        this.params.regionsInputs.on('change', function () {
            var regionId = $(this).val();
            var districtsInputsInRegion = $this.getDistrictsByRegionId(regionId);
            if (this.checked) {
                districtsInputsInRegion.prop('checked', true);
            } else {
                districtsInputsInRegion.prop('checked', false);
            }
            $this.search();
        });
    },

    bindPaginationLinks: function () {
        var $this = this;
        this.params.schoolsContainer.on('click', this.params.paginationLinkSelector, function (e) {
            e.preventDefault();
            var url = $(this).attr('href');
            $.ajax(url, {
                success: function (content) {
                    this.setContent(content);
                }.bind($this)
            });
        });
    },

    search: function () {
        var data = {
            title: this.getTitle(),
            districts: this.getCheckedDistricts()
        };
        $.ajax(this.params.searchUrl, {
            data: data,
            traditional: true,
            success: function (content) {
                this.setContent(content);
            }.bind(this)
        });
    },

    getTitle: function () {
        return this.params.titleInput.val();
    },

    getCheckedDistricts: function () {
        return this.params.districtsInputs.filter(':checked').map(function () {
            return $(this).val();
        }).get();
    },

    setContent: function (content) {
        this.params.schoolsContainer.html(content);
    }
};
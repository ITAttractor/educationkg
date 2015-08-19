var SchoolSearcher = function (params) {
    /**
     * Example params
     *
     * searchUrl: searchUrl - URL для поиска
     * searchBlockContainer: $('[data-content="search-block"]') - контейнер поиска, изначально скрыт
     * schoolsContainer: $('[data-content="schools"]') - контейнер школ, куда будет выводиться результат
     * titleInput: $('input[name="title"]') - поле ввода названия школы
     * regionsInputs: $('input[name="regions"]') - чекбоксы с регионами
     * districtsInputs: $('input[name="districts"]') - чекбоксы с районами
     * paginationLinkSelector: '[data-action="pagination"]' - селектор для ссылки пагинации
     */
    this.params = params;

    this.getDistrictsByRegionId = function (regionId) {
        var selector = '[data-region-id="' + regionId + '"]';
        return this.params.districtsInputs.filter(selector);
    };

    this.getRegionByRegionId = function (regionId) {
        var selector = '[value="' + regionId + '"]';
        return this.params.regionsInputs.filter(selector);
    };

    this.init = function () {
        this.bindTitleInput();
        this.bindDistrictsInputs();
        this.bindRegionsInputs();
        this.bindPaginationLinks();
    };

    this.bindTitleInput = function () {
        this.params.titleInput.on('input', this.search.bind(this));
    };

    this.bindDistrictsInputs = function () {
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
    };

    this.bindRegionsInputs = function () {
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
    };

    this.bindPaginationLinks = function () {
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
    };

    this.search = function () {
        var data = {
            title: this.getTitle(),
            districts: this.getCheckedDistricts()
        };
        if (data.title) {
            $.ajax(this.params.searchUrl, {
                data: data,
                traditional: true,
                success: function (content) {
                    this.showSearchBlock();
                    this.setContent(content);
                }.bind(this)
            });
        } else {
            this.hideSearchBlock();
        }
    };

    this.getTitle = function () {
        return this.params.titleInput.val();
    };

    this.getCheckedDistricts = function () {
        return this.params.districtsInputs.filter(':checked').map(function () {
            return $(this).val();
        }).get();
    };

    this.setContent = function (content) {
        this.params.schoolsContainer.html(content);
    };

    this.showSearchBlock = function () {
        this.params.searchBlockContainer.show();
    };

    this.hideSearchBlock = function () {
        this.params.searchBlockContainer.hide();
    };
};
var SchoolSearcher = {
    params: {
        searchUrl: null,
        schoolsContainer: null,
        titleInput: null,
        districtsInputs: null,
        paginationLinkSelector: null
    },

    init: function (params) {
        $.extend(this.params, params);
        this.params.titleInput.on('input', this.search.bind(this));
        this.params.districtsInputs.on('change', this.search.bind(this));
        this.bindPaginationLinks();
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
            districts: this.getDistricts()
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

    getDistricts: function () {
        return this.params.districtsInputs.filter(':checked').map(function () {
            return $(this).val();
        }).get();
    },

    setContent: function (content) {
        this.params.schoolsContainer.html(content);
    }
};
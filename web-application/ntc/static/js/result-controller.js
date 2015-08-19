var ResultController = function () {
    var $this = this;
    this.searchResultsUrl = null;
    this.getResultUrl = null;
    this.popupContainer = null;
    this.searchResultsContainer = null;

    this.showResultList = function (data) {
        $this.searchResultsContainer.html(data);
    };

    this.showPopUpWithResult = function (data) {
        $this.popupContainer.html(data);
        $this.popupContainer.addClass("active");
    };

    this.searchResult = function (searchString) {
        $.ajax({
            type: 'GET',
            url: $this.searchResultsUrl.replace('0', searchString),
            success: $this.showResultList
        })
    };

    this.getResult = function (resultId) {
        $.ajax({
            type: 'GET',
            url: this.getResultUrl.replace('0', resultId),
            success: $this.showPopUpWithResult
        })
    };

    this.initSearchResultForm = function () {
        $("#search-result-form").on('submit', function (event) {
            event.preventDefault();
            var searchString = $(this).find("input").val();
            $this.searchResult(searchString);
        });
    };

    this.initCloseButton = function() {
        $this.popupContainer.on("click", ".popup-close", function() {
            $this.popupContainer.removeClass('active');
        })
    };

    this.initShowResultPopUpLinks = function () {
        $this.searchResultsContainer.on("click", ".show-result-link", function (event) {
            event.preventDefault();
            var resultId = $(this).data("result-id");
            $this.getResult(resultId)
        })
    };

    this.init = function () {
        if (!$this.searchResultsUrl) {
            throw "searchResultsUrl was not set"
        }
        if (!$this.getResultUrl) {
            throw "getResultUrl was not set"
        }
        if (!$this.popupContainer) {
            throw "popupContainer was not set"
        }
        if (!$this.searchResultsContainer) {
            throw "searchResultsContainer was not set"
        }
        $this.initSearchResultForm();
        $this.initShowResultPopUpLinks();
        $this.initCloseButton();
    };

};


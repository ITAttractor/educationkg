var ResultController = function () {
    var $this = this;
    this.searchResultsUrl = null;
    this.getResultUrl = null;

    this.showResultList = function (data) {
        $("#result-container").html(data);
    };

    this.showPopUpWithResult = function (data) {
        $("#result-container").html(data);
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
        $("#result-form").on('submit', function (event) {
            event.preventDefault();
            var searchString = $(this).find("input").val();
            $this.searchResult(searchString);
        });
    };

    this.initShowResultPopUpLinks = function () {
        $("#result-container").on("click", ".show-result-link", function (event) {
            event.preventDefault();
            var resultId = $(this).data("result-id");
            $this.getResult(resultId)
        })
    };

    this.init = function () {
        if (!$this.searchResultsUrl) {
            throw "searchResultsUrl not set"
        }
        if (!$this.getResultUrl) {
            throw "getResultUrl not set"
        }
        $this.initSearchResultForm();
        $this.initShowResultPopUpLinks()
    };

};


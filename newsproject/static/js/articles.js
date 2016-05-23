// Set Pagination Link Variable
var linkHeader = "";

// Handle a Simple AJAX Get Request
function ajaxGet(url) {
    return new Promise(function(resolve, reject) {
        var request = new XMLHttpRequest();
        request.open("GET", url);
        request.onload = function() {
            if (request.status === 200) {
                resolve(request.response);
				linkHeader = request.getResponseHeader("Link");
            } else {
                reject(new Error(request.statusText));
            }
        };

        request.onerror = function() {
            reject(new Error("Network Error"));
        };

        request.send();
    });
}

// Render Articles List on the Page
function renderArticles(articles) {
	var output = "";

	if (linkHeader != undefined) {
		var links = parseLinkHeader(linkHeader);
		renderPagination(links);
	}

	// TODO: Cleanup this output code.
	for(var article = 0; article < articles.length; article++) {
		output += "<div class='col-masonry'><div class='panel'><div class='panel-body bg-purple'><h3 class='mv-lg'>" +
		articles[article].title +
		"</h3></div><div class='panel-body'><p id='description-wrapper'>" +
		jQuery.truncate(articles[article].description, { length: 1000, words: true }) +
		"</p><p class='clearfix'><span class='pull-left'><small class='mr-sm'>" +
		articles[article].publication_date +
		"</small></span><span class='pull-right'><small><span><a href='" +
		articles[article].url +
		"' target='_blank' title='Read More'>Read More</a></span></small></span></p></div></div></div>";
	}

	document.getElementById("loading-wrapper").style.display = "none";
	document.getElementById("articles-wrapper").innerHTML = output;
	document.getElementById("pagination-wrapper").style.display = "block";
}

window.onload = function () {
	var apiUrl = "/api" + window.location.pathname;
	var loadingMessage = randomLoadingMessage();
	var currentPage = getQueryString('page') || 1;
	var daysFilter = getQueryString('days');

	if (daysFilter != undefined) {
		apiUrl += "?days=" + daysFilter + "&page=" + currentPage
	} else {
		apiUrl += "?page=" + currentPage
	}

	document.getElementById("loading-message").innerHTML = loadingMessage;

	// Perform the AJAX Get Request
	ajaxGet(apiUrl).then(JSON.parse).then(
		function(objects) { return this.renderArticles(objects); }
	).catch(function(error) { throw new ApplicationError(error); });
}

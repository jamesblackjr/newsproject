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

// Parse the Link Header into Seperate Links
function parseLinkHeader(header) {
    if (header.length === 0) {
        throw new Error("Input must not be of zero length");
    }

    // Split parts by comma
    var parts = header.split(',');
    var links = {};
    // Parse each part into a named link
    for(var i=0; i<parts.length; i++) {
        var section = parts[i].split(';');
        if (section.length !== 2) {
            throw new Error("Section could not be split on ';'");
        }
        var url = section[0].replace(/<(.*)>/, '$1').trim();
        var name = section[1].replace(/rel="(.*)"/, '$1').trim();
        links[name] = url;
    }
    return links;
}

// Slpit Array into Equal Chunks for Column Layout
function splitArray(a, n, balanced) {    
    if (n < 2)
        return [a];

    var len = a.length,
            out = [],
            i = 0,
            size;

    if (len % n === 0) {
        size = Math.floor(len / n);
        while (i < len) {
            out.push(a.slice(i, i += size));
        }
    }

    else if (balanced) {
        while (i < len) {
            size = Math.ceil((len - i) / n--);
            out.push(a.slice(i, i += size));
        }
    }

    else {

        n--;
        size = Math.floor(len / n);
        if (len % size === 0)
            size--;
        while (i < size * n) {
            out.push(a.slice(i, i += size));
        }
        out.push(a.slice(size * n));

    }

    return out;
}

// Get the value of a querystring
function getQueryString(field, url) {
    var href = url ? url : window.location.href;
    var reg = new RegExp( '[?&]' + field + '=([^&#]*)', 'i' );
    var string = reg.exec(href);
    return string ? string[1] : null;
};

// Render Articles List on the Page
function renderArticles(objects) {
	var column;
	var output = "";
	var pagination = "";
	
	var columns = splitArray(objects, 3, true);
	var links = parseLinkHeader(linkHeader);
	
	for(column = 0; column < columns.length; column++) {
		var article;
		var articles = columns[column];
		
		output += "<div class='col-lg-4'>";
		
		for(article = 0; article < articles.length; article++) {
			output += "<div class='panel'><div class='panel-body bg-purple'><h3 class='mv-lg'>" +
			articles[article].title +
			"</h3></div><div class='panel-body'><p id='description-wrapper'>" +
			jQuery.truncate(articles[article].description, { length: 1000, words: true }) +
			"</p><p class='clearfix'><span class='pull-left'><small class='mr-sm'>" +
			articles[article].publication_date +
			"</small></span><span class='pull-right'><small><span><a href='" +
			articles[article].url +
			"' target='_blank' title='Read More'>Read More</a></span></small></span></p></div></div>";
		}
		
		output += "</div>";
	}
	
	pagination += "<div class='col-sm-12 text-center'><nav><ul class='pager'>"
	
	if (links["prev"] != undefined) {
		pagination += "<li class='previous'><a href='" + links["prev"].replace('/api/articles', '') + "'><span aria-hidden='true'>←</span> Previous Page</a></li>"
	};
	
	if (links["next"] != undefined) {
		pagination += "<li class='next'><a href='" + links["next"].replace('/api/articles', '') + "'>Next Page <span aria-hidden='true'>→</span></a></li>"
	};
	
	pagination += "</ul></nav></div>"
	
	document.getElementById("loading-wrapper").style.display = "none";
	document.getElementById("articles-wrapper").innerHTML = output;
	document.getElementById("pagination-wrapper").innerHTML = pagination;
}

window.onload = function () {
	var loadingMessage = randomLoadingMessage();
	var currentPage = getQueryString('page') || 1;
	
	document.getElementById("loading-message").innerHTML = loadingMessage;
	
	// Perform the AJAX Get Request
	ajaxGet('/news/api/articles/?page=' + currentPage).then(JSON.parse).then(
		function(objects) { return this.renderArticles(objects); }
	).catch(function(error) { throw new ApplicationError(error); });
}

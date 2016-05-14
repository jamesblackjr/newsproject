// Handle a Simple AJAX Get Request
function ajaxGet(url) {
    return new Promise(function(resolve, reject) {
        let request = new XMLHttpRequest();
        request.open("GET", url);
        request.onload = function() {
            if (request.status === 200) {
                resolve(request.response);
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
var getQueryString = function (field, url) {
    var href = url ? url : window.location.href;
    var reg = new RegExp( '[?&]' + field + '=([^&#]*)', 'i' );
    var string = reg.exec(href);
    return string ? string[1] : null;
};

// Render Articles List on the Page
function renderArticles(objects) {
	var column;
	var output = "";
	
	var columns = splitArray(objects, 3, true)
	
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
	
	document.getElementById("loading-wrapper").style.display = "none";
	document.getElementById("articles-wrapper").innerHTML = output;
	document.getElementsByClassName("pagination-wrapper")[0].style.display = "";
}

onload = function () {
	var loadingMessage = randomLoadingMessage();
	var currentPage = getQueryString('page');
	
	document.getElementById("loading-message").innerHTML = loadingMessage;
	
	// Perform the AJAX Get Request
	ajaxGet('/news/api/articles.json?page=' + currentPage).then(JSON.parse).then(
		(objects) => { this.renderArticles(objects); }
	).catch(function(error) { throw new ApplicationError(error); });
}

// Get the value of a querystring
function getQueryString(field, url) {
    var href = url ? url : window.location.href;
    var reg = new RegExp( '[?&]' + field + '=([^&#]*)', 'i' );
    var string = reg.exec(href);
    return string ? string[1] : null;
};

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

// Render Pagination from Header Links
function renderPagination(links) {
	var pagination = "<div class='col-sm-12 text-center'><nav><ul class='pager'>";
	
	if (links["prev"] != undefined) {
		pagination += "<li class='previous'><a href='" + links["prev"].replace('/api', '') + "'><span aria-hidden='true'>←</span> Previous Page</a></li>"
	};
	
	if (links["next"] != undefined) {
		pagination += "<li class='next'><a href='" + links["next"].replace('/api', '') + "'>Next Page <span aria-hidden='true'>→</span></a></li>"
	};
	
	pagination += "</ul></nav></div>"
	
	document.getElementById("pagination-wrapper").innerHTML = pagination;
}
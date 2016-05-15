// Custom Feeds List JavaScript
$(document).ready(function() {
	// Load DataTables for Feed List Table
    $('#feed-table').dataTable({
        'paging':   true,  // Table pagination
        'ordering': true,  // Column ordering 
        'info':     true,  // Bottom left status text
		'lengthMenu': [[-1, 10, 25, 50, 100], ['All', 10, 25, 50, 100]],
		'pageLength': 25,
        // Text translation options
        // Note the required keywords between underscores (e.g _MENU_)
        oLanguage: {
            sSearch:      'Search all columns:',
            sLengthMenu:  '_MENU_ records per page',
            info:         'Showing page _PAGE_ of _PAGES_',
            zeroRecords:  'Nothing found - sorry',
            infoEmpty:    'No records available',
            infoFiltered: '(filtered from _MAX_ total records)'
        }
    });
});
function w3_open() {
  document.getElementById("main").style.marginLeft = "15%";
  document.getElementById("mySidebar").style.width = "15%";
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("openNav").style.display = 'none';
  table.classList.add("table table-fixed")
}
function w3_close() {
  document.getElementById("main").style.marginLeft = "0%";
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("openNav").style.display = "inline-block";
}

$("table").append(
    $('<tfoot style="font-size: 12px;" />').append($("table thead tr").clone())
);
$("table tfoot tr th").css({
  'font-family':'arial'
});

$("table thead tr th").css({
  'text-align':'center'
});


//For search range

$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min = parseInt( $('#min').val(), 10 );
        var max = parseInt( $('#max').val(), 10 );
        var num = parseInt( data[3] ) || parseInt(data[2]) || parseInt(data[4]); // use data for the age column
	//var college = data[3];
	//var name = $('search').val();
 
        if ( ( isNaN( min ) && isNaN( max ) ) ||
             ( isNaN( min ) && num <= max ) ||
             ( min <= num   && isNaN( max ) ) ||
             ( min <= num   && num <= max ) )
        {
            return true;
        }
        return false;
    }
);

//Converting into data table
$(document).ready(function() {
  var mytable = $('.dataframe').DataTable({
	/*
	responsive: {
            details: {
                type: 'column',
                target: 'tr'
            }
        },
        columnDefs: [ {
            className: 'control',
            orderable: false,
            targets:   0
        } ],
        order: [ 1, 'asc' ],	
	*/
    initComplete: function () {
            this.api().columns().every( function () {
                var column = this;
                var select = $('<select><option value="">All</option></select>')
                    .appendTo( $(column.footer()).empty() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
 
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
 
                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                } );
            } );
        },
    colReorder: true,
    select: true,
    fixedHeader: true,
    searchHighlight: true,
  });
  $('#min, #max, #search').keyup( function() {
        mytable.draw();
  });

  $("table").addClass("table table-striped table-bordered nowrap");
  $("thead").addClass("table-dark");
});

function w3_open() {
  document.getElementById("main").style.marginLeft = "15%";
  document.getElementById("mySidebar").style.width = "15%";
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("openNav").style.display = 'none';
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



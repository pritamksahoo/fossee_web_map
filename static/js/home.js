document.getElementById("uploadBtn").onchange = function () {
  document.getElementById("uploadFile").value = this.value;
  if(form.filename.value != "Choose your .csv file") {
    document.getElementById("see").style.visibility = "visible";
  }
};

function myFunction() {
  document.getElementById("see").style.visibility = "hidden";
  form.filename.value = "Choose your .csv file";
  form.myfile.value = null;
}

function goback() {
  document.getElementById("see").style.visibility = "hidden";
}

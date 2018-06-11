
function init() {

    var url = "/api/wfreq/<sample>";
    Plotly.d3.json(url, function(error, response) {

    console.log(response);

    var data = response.dataset.samples_metadata //don't know what goes here
  
    var layout = {
      height: 600,
      width: 800
    };
  
    Plotly.plot("pie", data, layout);
  }
  
  function updatePlotly(newdata) {
    // YOUR CODE HERE
    // Use `Plotly.restyle` to update the pie chart with the newdata array
    var PIE = document.getElementById("pie");
  
    // Note the extra brackets around 'newx' and 'newy'
    Plotly.restyle(PIE, "values", [newdata]);
  }

  //something else happens here for the dropdown options...

  buildPlot();

var data = [];
var dates = [];
var maxDate;
var minDate;

$.ajax({
  type: "GET",
  url: "http://localhost:8000/api/sources?sort_date=true",
  contentType: "application/json; charset=utf-8",
  dataType: "json",
  success: function(data, status, jqXHR) {
    data = data;
    for (var i = 0; i < data.length; i++) {
      dates.push(new Date(data[i].date_created));
    }
    dates.sort(function(a, b) {
      return a.date - b.date;
    });
    var maxDate = dates[0];
    var minDate = dates[data.length - 1];
    console.log(minDate);
    initD3(minDate, maxDate);
  }.bind(this),
  error: function(xhr, status, err) {}.bind(this)
});

function initD3(min, max) {
  var margin = {
      top: 20,
      right: 20,
      bottom: 30,
      left: 50
    },
    width = 640 - margin.left - margin.right,
    height = 250 - margin.top - margin.bottom;

  var parseDate = d3.time.format("%d-%b-%y").parse;

  var x = d3.time.scale()
    .domain([min, max])
    .range([0, width]);

  var y = d3.scale.linear()
    .domain([0, 100])
    .range([height, 0]);

  var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

  var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

  var line = d3.svg.line()
    .x(function(d) {
      return x(d.date);
    })
    .y(function(d) {
      return y(d.close);
    });

  var svg = d3.select(".graph").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  x.domain(d3.extent(dates, function(d) {
    return d.date;
  }));
  // y.domain(d3.extent(data, function(d) { return d.close; }));

  svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

  svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)

  svg.append("path")
    .datum(data)
    .attr("class", "line")
    .attr("d", line);
}

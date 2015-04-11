var Map = React.createClass({
  componentWillMount: function() {
    $.ajax({
      type: "GET",
      url: "http://localhost:8000/api/sources",
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function(data, status, jqXHR) {
        console.log(data)
        var myLatlng = new google.maps.LatLng(-25.363882, 131.044922);
        var mapOptions = {
          center: myLatlng,
          zoom: 1
        };
        var map = new google.maps.Map(document.getElementById("map-canvas"),
          mapOptions);

        for (var i = 0; i < data.length; i++) {
          var coords = new google.maps.LatLng(data[i].latitude, data[i].longitude);
          var marker = new google.maps.Marker({
            position: coords,
            map: map,
          });
        }
      },
    });
  },
  render: function() {
    var mapStyle = {
      width:'100%',
      height:'500px'
    };
    return (
      <div id="map-canvas" style={mapStyle}></div>
    );
  }
});

React.render(<Map/>, document.querySelectorAll('.map')[0]);

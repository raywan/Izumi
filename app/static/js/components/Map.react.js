var Map = React.createClass({
  componentWillMount: function() {
    $.ajax({
      type: "GET",
      url: "http://localhost:8000/api/sources",
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function(data, status, jqXHR) {
        var myLatlng = new google.maps.LatLng(0,0);
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
          marker.setIcon('http://maps.google.com/mapfiles/ms/icons/blue-dot.png')
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

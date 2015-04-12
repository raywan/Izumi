var Map = React.createClass({
  componentWillMount: function() {
    var source_slug = window.location.pathname;
    console.log("http://localhost:8000/api" + source_slug);

    $.ajax({
      type: "GET",
      url: "http://localhost:8000/api" + source_slug,
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function(data, status, jqXHR) {
        var mapOptions = {
          center: new google.maps.LatLng(data.latitude,data.longitude),
          zoom: 10
        };
        var map = new google.maps.Map(document.getElementById("map-canvas"),
          mapOptions);

        var coords = new google.maps.LatLng(data.latitude, data.longitude);
        var marker = new google.maps.Marker({
          position: coords,
          map: map,
        });
        marker.setIcon('http://maps.google.com/mapfiles/ms/icons/blue-dot.png')
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

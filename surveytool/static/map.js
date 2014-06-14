var mapOptions = {
	center: new google.maps.LatLng(-34.397, 150.644),
	zoom: 8
};
var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

/*
var data = loadMarkers();

var markers = [];

for(var i = 0; i < data.length; i++){
	markers[i] = new google.maps.Marker(
										{
											position : data[i].LatLng
										});
}
*/
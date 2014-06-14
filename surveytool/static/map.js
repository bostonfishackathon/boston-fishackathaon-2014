var mapOptions = {
	center: new google.maps.LatLng(-34.397, 150.644),
	zoom: 8
};
var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

var markers = []

$.ajax{
	type: "GET",
	url: "returnFarmerDataJSON/",
	success: populateData(data)
}

function populateData(data){
	for(var i = 0; i < data.length; i++){
		markers[i] = new google.maps.Marker(
											{
												position : new google.maps.LatLng(data[i].latitude, data[i].longitude)
											});
	}
}

var mc = new MarkerClusterer(map, markers);
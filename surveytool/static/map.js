var mapOptions = {
	center: new google.maps.LatLng(-34.397, 150.644),
	zoom: 8
};
var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

var markers = [];
var mc;

$.ajax({
	type: "GET",
	url: "/returnFarmerDataJSON",
	success: function(data) {
		populateData(data)
	}
});

function populateData(data){

	var i = 0;
	$.each(data, function(index){
		var lat = parseFloat(this.fields.latitude.replace(/[^0-9.]+/g, ''));
		var lng = parseFloat(this.fields.longitude.replace(/[^0-9.]+/g, ''));
		markers[i] = new google.maps.Marker({position: new google.maps.LatLng(lat,lng)});

		var contentString = "Disease Presence: " + this.fields.is_diseased;

		var infowindow = new google.maps.InfoWindow({
		    content: contentString
		});

		google.maps.event.addListener(marker, 'click', function() {
		    infowindow.open(map,markers[i]);
		  });
				i++;
	})

	mc = new MarkerClusterer(map, markers);
}



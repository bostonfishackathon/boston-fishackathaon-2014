var mapOptions = {
	center: new google.maps.LatLng(11.1, 72.646),
	zoom: 3
};
var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

var markers = [];
var infowindows = [];
var mc;
var i = 0;

$.ajax({
	type: "GET",
	url: "/returnFarmerDataJSON",
	success: function(data) {
		populateData(data)
	}
});

function populateData(data){

	$.each(data, function(){
		var lat = parseFloat(this.fields.latitude.replace(/[^0-9.]+/g, ''));
		var lng = parseFloat(this.fields.longitude.replace(/[^0-9.]+/g, ''));
		markers[i] = new google.maps.Marker({position: new google.maps.LatLng(lat,lng)});

		var contentString = "Disease Presence: " + this.fields.is_diseased;

		infowindows[i] = new google.maps.InfoWindow({
		    content: contentString
		});

		google.maps.event.addListener(markers[i], 'click', function() {
		    infowindows[i].open(map, markers[i]);
		  });
		i++;
	})

	mc = new MarkerClusterer(map, markers);
}



function initMap() {

      var mapOptions = {
        center: { lat: -18, lng: 156 },
        zoom: 5
      };
      var mapCoral = new google.maps.Map(document.getElementById("map"), mapOptions);

      coralReefPin.forEach(function (coralReef) {

          //console.log(coralReef)

          if(coralReef.observer === currentUserId) {

              var coralMarker = new google.maps.Marker({
                  position: {lat: coralReef.latitudeC, lng: coralReef.longitudeC},
                  map: mapCoral,
                  title: ''
              });


              var infoWindow = new google.maps.InfoWindow({
                  content: '<h1>' + coralReef.name + '</h1><p>' + coralReef.description + '</p>'
              });

              coralMarker.addListener("mouseover", function () {
                  infoWindow.open(mapCoral, coralMarker);
              });

              coralMarker.addListener("mouseout", function () {
                  infoWindow.close();
              });
          }
      })
}


window.onload = function() {
      initMap();
};





var map;
var infoWindow;
var marker;

//地図の初期化
function initialize1() {

    var mapOptions = {
		center: new google.maps.LatLng(35.66, 139.69),//最初の中心座標
		zoom: 15,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		//styles: styles,
		disableDefaultUI: true
    };
    
    map = new google.maps.Map(document.getElementById("map_canvas"),mapOptions);

    //ウインドウの表示
	infoWindow = new google.maps.InfoWindow({
		content: '<strong>Hallo!!</strong>',
	});
		
	//マーカーの表示
	marker = new google.maps.Marker({
		position: map.getCenter(),
		map: map
	});
	        
    google.maps.event.addListener(marker, 'click', function(){
		infoWindow.open(map, marker);
	});	
}


//住所を緯度経度に変換，マップ化
function initialize2(){

		var geocoder = new google.maps.Geocoder();
		geocoder.geocode({
			'address': '兵庫県神戸市'
		}, function(result, status){
			if(status == google.maps.GeocoderStatus.OK){
				var latlng = result[0].geometry.location;
				var mapOptions = {
					zoom: 15,
					center: latlng,
					mapTypeId: google.maps.MapTypeId.ROADMAP
				};
				map = new google.maps.Map(document.getElementById("map_canvas2"), mapOptions);
				
				google.maps.event.addListener(map, 'click', function(event){
					marker = new google.maps.Marker({
						position: event.latLng,
						map: map
					});
				
					geocoder.geocode({
						'latLng': event.latLng
					},function(result, status){
						if(status == google.maps.GeocoderStatus.OK){
							infoWindow = new google.maps.InfoWindow({
								content: result[0].formatted_address
							});
							infoWindow.open(map, marker);
						}else{
							alert("Error!!");
						}
					});
				});
			}else{
				alert("Error!!");
			}
		});
	
}


//住所を入力し，地図を移動
function initialize3(){	
		var latlng = new google.maps.LatLng(35.66, 139.69);
		var mapOptions = {
			zoom: 15,
			center: latlng,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		};
		map = new google.maps.Map(document.getElementById("map_canvas3"), mapOptions);
}
function moveMap(){
			var geocoder = new google.maps.Geocoder();
			geocoder.geocode({
				'address': document.getElementById('address').value
			},function(result,status){
				if(status == google.maps.GeocoderStatus.OK){
					map.panTo(result[0].geometry.location);
				}else{
					alert("Error!!");
				}
			});
}


//現在地の地図を表示
function initialize4(){

	var latlng = new google.maps.LatLng(35.66, 139.69);
	var mapOptions = {
			zoom: 15,
			center: latlng,
			mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById("map_canvas4"), mapOptions);
	
	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(function(position){
			map.setCenter(new google.maps.LatLng(position.coords.latitude, position.coords.longitude));
		}, function(){
			alert("Error!!");
		});
	}else{
		alert("Error!!");
	}

}





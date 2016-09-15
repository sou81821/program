var user_logs = {
	
	"Onmyoji" : 3,
	"GTO" : 3,
	"Led Zeppelin" : 3,
	"Dragon Ball" : 3,
	"Sex and the City" : 3,
	"Chaplin" : 3,
	"KILL BILL" : 3,
	"THE MATRIX" : 3,
	"Alice in Wonderland" : 3,
	"Yu-Yu hakusho" : 3,
	"Hamlet" : 3,
	"Spider-Man2" : 3,
	"Lupin the Third" : 3,
	"GHOST SHIP" : 3
};

display_movie = ['135', '210', '238', '263', '270', '370', '457', '468', '596', '724', '903', '1551', '1691', '2617'];

function submitData(clicked){
	if (clicked == 0 || clicked == 1){
		//console.log(clicked);
		a = ($("#movie" + clicked.toString()).find('.movie_title').html());
		//console.log(a);
		user_logs[a] += 1;
		if (clicked == 0){
			b = ($("#movie" + (clicked + 1).toString()).find('.movie_title').html());
                	user_logs[b] -= 1;
		}else{
                        b = ($("#movie" + (clicked - 1).toString()).find('.movie_title').html());
                        user_logs[b] -= 1;
                }
	}

	console.log(user_logs);
	var json_str = JSON.stringify(user_logs);

	$.ajax({
		type: "GET",
		url: "api/getItem/index.php",
		data: user_logs,
		contentType: 'application/json',
		dataType: "json",
		success: function(response){
			console.log("success.");
			console.log(response);
			//console.log(clicked)
			
			showSelectMovies(response);
			showRecommendMovies(response);
		},
		error: function(a,b,c){
			console.log("error.");
			
			//console.log(a);console.log(b);console.log(c);
		}
	});

}


function createRecommendMovie(img_src,movie_title){
	
	return '<div id = "recommend_movie1" class="col-sm-3"><div class="thumbnail"><img src = "'+img_src+'" alt = "..."><div class = "caption"><h3 class = "movie_title" style="text-align:center;">'+movie_title+'</h3></div></div></div>';

}

function showSelectMovies(data){
	console.log(data);
	for (i = 0; i < data.length; i++){
		$("#movie" + i.toString()).find('.movie_title').html(data[i]["title"]);
		$("#movie" + i.toString()).find('img').attr('src', data[i]["img"]);
	}
}

function showRecommendMovies(data){
        //console.log(data);
	$('#recommend_zone').empty();
	for(i = 0; i < data[0]["total"]; i++){
		a = createRecommendMovie(data[i+2]["img"], data[i+2]["title"]);
		$('#recommend_zone').append(a);
	}
}


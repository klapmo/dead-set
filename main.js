$.ajax({
    url:"https://api.setlist.fm/rest/1.0/artist/94f8947c-2d9c-4519-bcf9-6d11a24ad006/setlists?p=1",
    type:"GET",
    dataType:"json",
    headers:{
        "x-api-key": "X5zdk_R9xhoRkSxvDUDSV1n_1hlGGSRPwaDq"
    },
    contentType:"application/json; charset=UTF-8",

    success:function(result){
        // Call Back function for result
        console.log(result.setlist[1])
        for(let i=0; i < result.setlist.length;i++){
            let artist = result.setlist[i].artist[3]
            let eventDate = result.setlist[i].eventDate
            let eventID = result.setlist[i].id
            let setNum = result.setlist[i].sets.set[i].name
            let song = result.setlist[i].sets.set[i].song[i].name
            
            // Code below to add to HTML divs
            // $("#posters").append(`<div><img src="${poster}" alt="Poster"><h3>${movieTitle} (${year})</h3><p><ul><li>"It's a good Movie" -RottenTomatoes</li><li>Runtime: 120min</li></ul></p></div>`)
            // $("#table").append(`<div><table><tr><td>${type}</td><td>${imdbID}</td></tr></table></div>`)
        }
    },
    error:function(error){
        console.log(error)
    }
});
let selectedImages = [];

$("#submit").click(function(){
	$.ajax({
		  url:"http://localhost:52520/img_history",
		  type:"POST",
		  data: JSON.stringify({selectedImages}),
		  contentType:"application/json",
		  dataType:"json",
		  success: function(data){
        console.log(data);
        selectedImages = [];
        $( "img.img" ).remove();
        for (let img of data.img_recommended) {
          $( "#images" ).append( `
          <img class="img" src="https://010703da.ngrok.io/${img}" alt="Smiley face" data-img=${img} width="200" height="200">
          `);
        }
        $( ".img" ).click(function() {
          let imageName = $(this).data().img;
          selectedImages.push(imageName);
        });
			}
	})
});

$( ".img" ).click(function() {
  let imageName = $(this).data().img;
  selectedImages.push(imageName);
});

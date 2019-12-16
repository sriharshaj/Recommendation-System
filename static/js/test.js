let selectedImages = [];

$("#submit").click(function(){
	$.ajax({
		  url:"http://e3540793.ngrok.io/img_history",
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
          <img class="img" src="https://da91000b.ngrok.io/${img}" alt="Smiley face" data-img=${img} width="200" height="200">
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

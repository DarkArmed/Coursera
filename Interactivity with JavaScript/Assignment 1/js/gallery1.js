/*Name this external file gallery.js*/

function upDate(previewPic){

 document.getElementById('image').innerHTML = previewPic.alt;
document.getElementById("image").style.backgroundImage = 'url(' + previewPic.src + ')';
document.getElementById("image").style.backgroundColor = "green";
	}


	function unDo(){
    document.getElementById('image').innerHTML = ' Hover over an image below to display here.';
    document.getElementById("image").style.backgroundColor = "#8e68ff";
	document.getElementById("image").style.backgroundImage = "url('')";
     
		
	}
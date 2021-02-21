window.onload = function() {
	var myCanvas = document.getElementById("noticecanvas");
	var ctx = myCanvas.getContext("2d");

    function bufferHandler(buffer, options) {
        console.log(buffer.length, options);
    }

    whiteboard_options = {
        strokeStyle: "#3477eb",
        lineWidth: 5,
    }

    const whiteboard = new Whiteboard('noticecanvas', bufferHandler, whiteboard_options);


    prevDrawing = document.getElementById("prevdrawing")
    ctx.drawImage(prevDrawing, 0, 0)
    $('#clearwhiteboard').click(function() {
        var canvas = document.getElementById("noticecanvas");
        ctx = canvas.getContext('2d')
        ctx.clearRect(0, 0, canvas.width, canvas.height);

    });
    $('#submitwhiteboard').click(function() {
        var canvas   = document.getElementById("noticecanvas");
        var img      = canvas.toDataURL("image/png");
        var filename = 'whiteboard.png';
        var formdata = new FormData();
        formdata.append(filename, img);
        var dataURL  = canvas.toDataURL(); 
        $.ajax({ 
            type: "POST", 
            url: "/upload_whiteboard", 
            data: { 
                imgBase64: dataURL 
            } 
        }).done(function(o) { 
            console.log('saved'); 
        }); 
    });
};

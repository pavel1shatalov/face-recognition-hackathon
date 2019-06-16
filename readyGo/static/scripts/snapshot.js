  Webcam.set({
        width: 320,
        height: 240,
        image_format: 'jpeg',
        jpeg_quality: 90
      });
      Webcam.attach( '#my_camera' );

      <!-- Code to handle taking the snapshot and displaying it locally -->
      function take_snapshot() {
        // take snapshot and get image data
        Webcam.snap(function (data_uri) {
          console.log(data_uri)
          // display results in page
          document.getElementById('results').innerHTML =
                  '<img src="' + data_uri + '"/>';
          console.log("before ajax")
          $.ajax({
            type: "POST",
            contentType: "application/json; charset=utf-8",
            url: "http://0.0.0.0:5000/registration",
            data: JSON.stringify({image: data_uri, name: document.getElementById("name").value}),
            success: function (data) {
              console.log("success")
            },
            dataType: "json"
          });
        });
      }
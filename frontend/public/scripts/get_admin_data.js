$.ajax({
            type: 'GET',
            url: "http://0.0.0.0:5000/admin",
            success:function(data){
             console.log(data);
            }
        });
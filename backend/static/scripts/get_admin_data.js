$.ajax({
            type: 'GET',
            url: "http://0.0.0.0:5000/admin",
            success:(backend_data) => {
             // console.log(backend_data);
                let divs = document.getElementsByClassName("rty");
                console.log(divs);
             backend_data.forEach( (element, index) => {
                 console.log(divs[index]);
                    divs[index].style.display = "block";
                 // console.log(el);
                 console.log(element["name"])
             })
            }
        });
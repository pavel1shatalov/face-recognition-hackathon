$.ajax({
            type: 'GET',
            url: "http://0.0.0.0:5000/admin",
            success:(backend_data) => {
                console.log(backend_data);
                backend_data = JSON.parse(backend_data);
                console.log("did get to fetch data");
                let divs = document.getElementsByClassName("rty");
             backend_data.forEach( (element, index) => {
                 console.log(divs[index]);
                 divs[index].style.visibility = "visible";
                 divs[index].getElementsByClassName("name")[0].innerHTML = element["name"]
                 if (element["available"] === '1') {
                      divs[index].classList.remove("table-danger");
                     divs[index].classList.add("table-primary");
                     divs[index].getElementsByClassName("position")[0].innerHTML = "available"
                 }
             })
            }
        });
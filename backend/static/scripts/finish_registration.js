stop_reg_btn = document.getElementById("stop_reg");

stop_reg_btn.addEventListener("click", () => {
    console.log("Im here");
    $.ajax({
        type: "POST",
        contentType: "application/json; charset=utf-8",
        url: "http://0.0.0.0:5000/admin",
        data: ('0'),
        success: function (data) {
          console.log("success")
        },
        dataType: "json"
    });
});

// function finish_registration() {
//     $.ajax({
// type: "POST",
// contentType: "application/json; charset=utf-8",
// url: "http://0.0.0.0:5000/admin",
// data: JSON.stringify({registration: '0'}),
// success: function (data) {
//   console.log("success")
// },
// dataType: "json"
// });
// }

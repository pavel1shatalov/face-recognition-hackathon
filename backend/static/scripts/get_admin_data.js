$.ajax({
            type: 'GET',
            url: "http://0.0.0.0:5000/admin",
            success:(backend_data) => {
             console.log(backend_data);

            var markup = "<li><b>${name}</b> (${available})</li>";

            /* Compile the markup as a named template */
            $.template( "userTemplate", markup );

            /* Render the template with the movies data and insert
               the rendered HTML under the "movieList" element */
            $.tmpl( "userTemplate", backend_data)
              .appendTo( "#userTable" );

            }
        });
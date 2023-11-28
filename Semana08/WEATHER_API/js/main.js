$(document).ready(function(){
    $('#btnSearch').click(function(){
        busqueda();
    })
});

function busqueda() { 
    console.log("busqueda");
    var ubicacion = $('#floatingInput').val();
    const API_KEY = 'a5ba34a8e2e7338521c27ebb96a65300'
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${ubicacion}&appid=${API_KEY}&units=metric`
    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",
        success: function (data) {
            console.log(data);
            agregarFila(data);
        },

        error : function(error) {
            alert('Disculpe, existió un problema,Verifique el nombre de la cuidad');
        },

         // código a ejecutar sin importar si la petición falló o no
        // complete : function(jqXHR, status) {
        //     alert('Petición realizada');
        // }
    });

};

function agregarFila(data){
    const tableBody =  $('#contenedor-clima')
    const fila = `
    <tr>
        <td>${data.name}</td>
        <td>${data.main.temp}°C</td>
        <td>${data.weather[0].description}</td>
    </tr>
    `
    tableBody.append(fila);
}



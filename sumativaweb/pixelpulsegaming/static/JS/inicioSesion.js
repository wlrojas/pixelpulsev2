// Propósito: Validar los campos del formulario de inicio de sesión
// Hasta el momento solo capturar los valores de los campos y validar que no estén vacíos

$(document).ready(function() { 
    $('#InicioSesion').submit(function(e) { 
        e.preventDefault(); 

        // Capturar valores de los campos
        var email = $('#email').val(); 
        var password = $('#password').val(); 

        // Validar campos
        if ( email === '' || password === '') {
            
            alert('Por favor, complete todos los campos.'); 
            return false; 
        } 

        $('#InicioSesion')[0].reset();
        alert('Iniciaste sesión correctamente.'); 
        return true; 
    });
});

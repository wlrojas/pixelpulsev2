// Funciones para validar los campos del formulario de creación de cuenta

function validarNombre(nombre) {
    var regex = /^[a-zA-Z\s]*$/;
    return regex.test(nombre);
}

function validarApellido(apellido) {
    var regex = /^[a-zA-Z\s\-]*$/;
    return regex.test(apellido);
}

function validarRun(run) {
    var regex = /^[0-9]+$/;
    if (run.length < 7 || run.length > 8 || !regex.test(run)) {
        console.log("El run debe tener 7 u 8 caracteres numéricos");
        return false;
    }
    return true;
}

function validarDvRun(dvRun) {
    var regex = /^[0-9kK]{1}$/;
    return regex.test(dvRun);

}

function validarEdad(edad) {
    if (edad < 13 || edad > 110) {
        alert("Para poder crear una cuenta en PixelPulse Gaming, debes ser mayor de 13 años y menor de 110 años.");
        return false;
    } 
    return true;
}

function validarTelefono(numeroContacto) {
    var regex = /^[0-9]+$/;
    if (regex.test(numeroContacto)) {
        return true;
    } 
    if (numeroContacto.length != 9) {
        return false;
    } 

    return false;     
}

function validarEmail(email) {
    var regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    return regex.test(email);
}

function validarPassword(password, rPassword) {
    let ERROR_LONGITUD = "La contraseña debe tener al menos 8 caracteres y máximo 20 caracteres.";
    let ERROR_NUMERO = "La contraseña debe tener al menos un número.";
    let ERROR_LETRAS = "La contraseña debe tener al menos una minúscula y una mayúscula.";
    let ERROR_ESPECIAL = "La contraseña debe tener al menos un carácter especial.";

    let longitudValida = /^.{8,25}$/.test(password);
    let tieneNumero = /\d/.test(password);
    let tieneLetraMinuscula = /[a-z]/.test(password);
    let tieneLetraMayuscula = /[A-Z]/.test(password);
    let tieneCaracterEspecial = /[\W_]/.test(password);

    if (!longitudValida) {
        alert(ERROR_LONGITUD);
        return false;
    }

    if (!tieneNumero) {
        alert(ERROR_NUMERO);
        return false;
    }

    if (!tieneLetraMinuscula || !tieneLetraMayuscula) {
        alert(ERROR_LETRAS);
        return false;
    }

    if (!tieneCaracterEspecial) {
        alert(ERROR_ESPECIAL);
        return false;
    }

    if (password !== rPassword) {
        alert("Las contraseñas no coinciden.");
        return false;
    }
    return true;

}





$(document).ready(function() { 
    $('#formularioCrearCuenta').submit(function(e) { 
        e.preventDefault(); 
        console.log("Evento submit capturado.");
        // Capturar valores de los campos
        var pNombre = $('#pNombre').val(); 
        var apellidoPaterno = $('#apellidoPaterno').val();
        var apellidoMaterno = $('#apellidoMaterno').val();
        var run = $('#run').val();
        var dvRun = $('#dvRun').val();
        var edad = $('#edad').val();
        var numeroContacto = $('#numeroContacto').val();
        var email = $('#email').val(); 
        var password = $('#password').val(); 
        var rPassword = $('#rPassword').val(); 

        // Validar campos
        if (pNombre === '' ||  apellidoPaterno === '' || apellidoMaterno === '' || 
            run === '' || dvRun === '' || edad === '' || numeroContacto === '' ||  
            email === '' || password === '' || rPassword === '') {
            
            alert('Por favor, complete todos los campos.'); 
            return false; 
        } 

        if (!validarNombre(pNombre)) {
            return false;
        }

        if (!validarApellido(apellidoPaterno)) {
            return false;
        }

        if (!validarApellido(apellidoMaterno)) {
            return false;
        } 
        
        if (!validarRun(run)) {
            return false;
        }

        if (!validarDvRun(dvRun)) {
            return false;
        }
        
        if (!validarEdad(edad)) {
            return false;
        }
        
        if (!validarTelefono(numeroContacto)) {
            return false;
        }
        
        if (!validarEmail(email)) {
            return false;
        }

        if (!validarPassword(password, rPassword)) {
            return false;
        }

        // Si todo está validado, enviar el formulario y restablecerlo
        $('#formularioCrearCuenta')[0].reset();
        alert('Cuenta creada con éxito.'); 
        return true; 
    });
});

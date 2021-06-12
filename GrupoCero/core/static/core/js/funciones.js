/*5 FUNCIONES*/


var validaNombre = function() {
        var nom = document.getElementById("Nombre").value;
        if (nom.length > 0) {
            return true;
        } else {
            return false;
        }
    }
    // var validaApellido = function(){
    //     var ape = document.getElementById("apellidoP").value;
    //     if(ape.length>0){
    //         return true;
    //     }else{
    //         return false;
    //     }
    // }
var validarTelefono = function() {
    var tel = document.getElementById("Telefono").value;
    if (tel.length == 9) {
        return true;
    } else {
        return false;
    }
}

var validarCorreo = function() {
    var corr = document.getElementById("E-mail").value;
    if (corr.length > 0) {
        return true;
    } else {
        return false;
    }
}

var validarMensaje = function() {
    var men = document.getElementById("mensaje").value;
    if (men.length > 10) {
        return true;
    } else {
        return false;
    }
}

// validacion de funciones 

var validarFunciones = function() {
    if (validaNombre() == true) {} else {
        envio = "El campo nombre y apellido debe ser ingresado";
        return envio;

    }
    if (validarTelefono() == true) {} else {
        envio = "El campo telefono debe contener 9 dígitos";
        return envio;
    }
    if (validarCorreo() == true) {} else {
        envio = "Debe indicar un correo"
        return envio;
    }
    if (validarMensaje() == true) {} else {
        envio = "El campo Mensaje debe contener como mínimo 10 caracteres";
        return envio;
    }
    if (validaNombre() == true && validarTelefono() == true && validarCorreo() == true && validarMensaje() == true) {
        envio = "Ingreso exitoso, Bienvenido!";
        return envio;
    }
}
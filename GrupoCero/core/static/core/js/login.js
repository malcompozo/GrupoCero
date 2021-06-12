var validarCorreo = function() {
    var correo = document.getElementById("idcorreo").value;
    re = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
    if (!re.exec(correo)) {
        return false;
    } else
        return true;
}

var validarContraseña = function() {
    var contra = document.getElementById("idcontrasena").value;
    if (contra.length >= 6) {
        return true;
    } else {
        return false;
    }
}


var validarFunciones = function() {

    if (validarCorreo() == true) {} else {
        envio = "Debe ingresar un correo (Ejemplo: Correo123@gmail.com)"
        return envio;
    }
    if (validarContraseña() == true) {} else {
        envio = "El campo contraseña debe contener como mínimo 6 caracteres";
        return envio;
    }
    if (validarCorreo() == true && validarContraseña() == true) {
        envio = "Bienvenido";
        location.href = "/publicacion";
        return envio;
    }
}
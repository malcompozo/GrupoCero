
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input, textarea');

const expresiones = {
	texto: /^.{1,50}$/,
    fecha: /^\d{4}$/,
	numero: /^\d{1,8}$/
}

const campos = {
    nombre: false,
    fecha: false,
    precio: false,
    tipo: false,
    dim: false,
    soporte: false,
    desc: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "nombreObra":
            validarCampo(expresiones.texto, e.target, 'nombre');
            break;
        case "fecha":
            validarCampo(expresiones.fecha, e.target, 'fecha');
            break;
        case "precio":
            validarCampo(expresiones.numero, e.target, 'precio');
            break;
        case "tipoObra":
            validarCampo(expresiones.texto, e.target, 'tipo');
            break;
        case "alto":
            validarCampo(expresiones.numero, e.target, 'dim');
            break;
        case "ancho":
            validarCampo(expresiones.numero, e.target, 'dim');
            break;
        case "largo":
            validarCampo(expresiones.numero, e.target, 'dim');
            break;
        case "soporte":
            validarCampo(expresiones.texto, e.target, 'soporte');
            break;
        case "desc":
            validarCampo(expresiones.texto, e.target, 'desc');
            break;
    
        default:
            break;
    }
}

const validarCampo = (expresion, input, campo) => {
	if (expresion.test(input.value)) {
        document.querySelector('#formulario_'+campo+' .input-error')
        .classList.remove('input-error-activo');
        campos[campo] = true;
    } else {
        document.querySelector('#formulario_'+campo+' .input-error')
        .classList.add('input-error-activo');
        campos[campo] = false;
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup',validarFormulario);
    input.addEventListener('blur',validarFormulario);
});

formulario.addEventListener('submit',(e) => {
    e.preventDefault()

    //faltaria hacer la validacion para la imagen que se adjunta
    if (campos.nombre && campos.fecha && campos.precio && campos.tipo && campos.dim && campos.soporte && campos.desc) {
        formulario.reset();  
    } else {
        //arreglar el query para mostrar el aviso de error
        document.querySelector('#formulario_aviso .error-envio')
        .classList.add('error-envio-activo');
    }
});
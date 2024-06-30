


var container = document.querySelector("#catalogo");
window.onload = getCatalog();
function getCatalog() {
    fetch('https://api.sampleapis.com/wines/reds')
        .then(res => res.json())
        .then(res => {
            getAll = casteo(res);
            for (let i = 0; i < getAll.length; i++) {

                let agregar = document.createElement("div");
                agregar.innerHTML = `
                <div class=catalogo-info>
                <h3>
                ${getAll[i].nombre}
                </h3>
                <p>Cosecha: ${getAll[i].cosecha}</p>
                <img src="${getAll[i].image}" alt="">

                </div>
                `
                container.appendChild(agregar);
            }
            console.log(getAll);
        })
}

/* ingreso el json recibido y lo casteo con la clase winnery atravez de un IF donde pregunto si 
// dentro del atributo location contiene la palabra argentina, 
// si contiene la palabra me devolvera el numero de la posicion en
  donde empieza sino devolvera -1 */
function casteo(item) {
    const obj = [];
    const ver = item;
    for (let i = 0; i < ver.length; i++) {

        if (ver[i].location.indexOf("Argentina") != -1) {
            let valor = new winnery(ver[i].id, ver[i].winery, ver[i].wine, ver[i].image, ver[i].location);
            obj.push(valor)
        }
    }
    return obj;

}


class winnery {
    constructor(Id, nomb, cosec, imag, loca) {
        this.id = Id;
        this.nombre = nomb;
        this.cosecha = cosec;
        this.image = imag;
        this.location = loca;
    }
}

//// VALIDACIÓN///////////////////////////////



    document.getElementById('formulario').addEventListener('submit', function(event) {

    const nombre = document.getElementById('Nombre').value.trim();
    const apellido = document.getElementById('Apellido').value.trim();
    const empresa = document.getElementById('empresa').value.trim();
    const dni = document.getElementById('DNI').value.trim();
    const area = document.getElementById('Area').value.trim();
    const telefono = document.getElementById('telefono').value.trim();
    const email = document.getElementById('email').value.trim();
    const condiciones = document.getElementById('condiciones').checked;
    const mensaje = document.getElementById('mensaje').value.trim();



    if (nombre === '' || apellido === '' || empresa === '' || dni === '' || area === '' || telefono === '' || email === ''|| mensaje === '') {
        event.preventDefault();
        alert('Todos los campos marcados con asterisco son obligatorios.');
        return;
    }


    if (!condiciones) {
        event.preventDefault();
        alert('Debe aceptar las condiciones.');
        return;
    }

    const valEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!valEmail.test(email)) {
        event.preventDefault();
        alert('Por favor, ingrese un correo electrónico válido.');
        return;
    }


    const valTelefono = /^\d+$/;
    if (!valTelefono.test(telefono)) {
        event.preventDefault();
        alert('Por favor, ingrese un número de teléfono válido.');
        return;
    }
    else{
        alert(nombre +' '+ apellido +','+' el formulario fué enviado exitosamente, pronto nos pondremos en contacto con usted')
    }
});






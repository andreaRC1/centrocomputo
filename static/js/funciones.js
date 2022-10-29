function muestraModal(url, titulo, tipo){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modalCuerpo').innerHTML = `¿Deseas eliminar el ${tipo} ${titulo} ? `;
}

function muestraModalMaterial(url, nombre){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modalCuerpo').innerHTML = `¿Deseas eliminar el material ${nombre} ? `;
}

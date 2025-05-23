function eliminarPelicula(id){
    Swal.fire({
        title: '¿Estás seguro?',
        showDenyButton: true,
        confirmButtonText: 'Sí',
        denyButtonText: `No`,
    }).then((result) => {
        if (result.isConfirmed){
            location.href = '/eliminarPelicula/' + id;
        }
    });
}
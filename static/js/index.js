copyaction = () => {
    document.getElementById("imagelink").select();
    document.execCommand("Copy");
}

var home = window.location.origin;
$("#ImageModal").on('shown.bs.modal', function (event) {
    var modal = $(this)
    modal.find('.modal-footer input').val(home)

})
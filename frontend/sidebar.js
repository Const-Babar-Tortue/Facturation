/*Script permettant d'ouvrir et de fermer le sidebar (Menu principal de gauche.*/

$(document).ready(function () {
  var scactif = location.pathname.substring(location.pathname.lastIndexOf('/') + 1)
  scactif = scactif.split(".")
  $('#' + scactif[0]).addClass('active');

  $('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
  });





});

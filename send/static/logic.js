$(document).ready(function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    updateStatus(socket.connected);

    socket.on('status', function (data) {
        updateStatus(data.message);
    });

    function updateStatus(status) {
        var statusMessage = status ? 'Connected' : 'Not Connected';
        $('#status-message').text(statusMessage);
    }
});
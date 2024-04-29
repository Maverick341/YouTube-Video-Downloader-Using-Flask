$(document).ready(function() {
    $('#download-btn').click(function() {
        var videoUrl = $('#video-url').val();
        $.ajax({
            url: '/download',
            type: 'POST',
            data: { video_url: videoUrl },
            success: function(response) {
                $('#message').text(response.message);
            },
            error: function(xhr, status, error) {
                console.error(error);
                $('#message').text('An error occurred. Please try again later.');
            }
        });
    });
});

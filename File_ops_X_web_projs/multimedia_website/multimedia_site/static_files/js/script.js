// script.js

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all video players on the page
    var videos = document.querySelectorAll('.video-js');
    
    videos.forEach(function(video) {
        // Initialize the video player
        videojs(video, {}, function() {
            // Player is ready
            console.log('Video player is ready');
        });
    });
});
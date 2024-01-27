document.addEventListener('DOMContentLoaded', function () {
    adjustContentHeight();
});

// Function to adjust the height of the content div
function adjustContentHeight() {
    var navbarHeight = document.querySelector('nav').offsetHeight;
    var footerHeight = document.querySelector('footer').offsetHeight;
    
    var screenHeight = window.innerHeight;
    var contentHeight = screenHeight - navbarHeight - footerHeight;

    document.getElementById('content').style.height = contentHeight + 'px';
}

// Adjust the content height if the window is resized
window.addEventListener('resize', adjustContentHeight);

// Open the contact us popup when the user clicks the contact us link
document.querySelector('a[href="#contact-us"]').addEventListener('click', function() {
    document.querySelector('.contact-us-popup').style.display = 'block';
    });

    // Close the contact us popup when the user clicks the close button
    document.querySelector('.contact-us-popup-close').addEventListener('click', function() {
    document.querySelector('.contact-us-popup').style.display = 'none';
    });
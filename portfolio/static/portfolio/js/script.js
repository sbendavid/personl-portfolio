//material contact form animation
$(".contact-form")
.find(".form-control")
.each(function () {
    var targetItem = $(this).parent();
    if ($(this).val()) {
        $(targetItem)
            .find("label")
            .css({
                top: "-6px"
                , fontSize: "16px"
                , color: "#ff512f"
            });
    }
});
$(".contact-form")
.find(".form-control")
.focus(function () {
    $(this)
        .parent(".input-block")
        .addClass("focus");
    $(this)
        .parent()
        .find("label")
        .animate({
                top: "-6px"
                , fontSize: "16px"
                , color: "#ff512f"
            }
            , 300
        );
});
$(".contact-form")
.find(".form-control")
.blur(function () {
    if ($(this).val().length == 0) {
        $(this)
            .parent(".input-block")
            .removeClass("focus");
        $(this)
            .parent()
            .find("label")
            .animate({
                    top: "20px"
                    , fontSize: "18px"
                }
                , 300
            );
    }
});


$(document).ready(function() {
  // Hide the header content initially
  $("#headerContent").hide();

  // Add a click event listener to the "CONTACT" link
  $("a[href$='portfolio:contact']").click(function(e) {
    e.preventDefault(); // Prevent the default behavior of the link

    // Toggle the visibility of the header content
    $("#headerContent").toggle();

    // Optionally, you can also close the navbar if it's open
    $(".navbar-collapse").collapse('hide');
  });
});
$(document).ready(function() {
    $("#slideToggle").click(function() {
        $("body").toggleClass("dark-mode");
        $(".navbar").toggleClass("dark-mode");
        $(".card").toggleClass("dark-mode");

    });
});

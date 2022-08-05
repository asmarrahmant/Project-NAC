// Left Menu
$(document).ready(function() {
    $('.menu-button').click(function() {
        $('.left-menu').addClass('show');
        $('.modal-bg').addClass('show');
    });
    $('.menu-back').click(function() {
        $('.left-menu').removeClass('show');
        $('.modal-bg').removeClass('show');
    });
});


// Back Button
function goBack() {
    window.history.back();
}

// Toast Message
function showToast(text) {
    var x = document.getElementById("toast");
    x.classList.add("show");
    x.innerHTML = text;
    setTimeout(function() {
        x.classList.remove("show");
    }, 3000);
}

// Header Fixed Scroll down
var didScroll, lastScrollTop = 0,
    delta = 5,
    navbarHeight = $(".header-top").outerHeight();

function hasScrolled() {
    var l = $(this).scrollTop();
    Math.abs(lastScrollTop - l) <= delta || (l > lastScrollTop && l > navbarHeight ? $(".header-top").removeClass("header-down").addClass("header-up") : l + $(window).height() < $(document).height() && $(".header-top").removeClass("header-up").addClass("header-down"), lastScrollTop = l)
}
$(window).scroll(function(l) { didScroll = !0 }), setInterval(function() { didScroll && (hasScrolled(), didScroll = !1) }, 250);


// Image Modal
function onClick(element) {
    document.getElementById("img01").src = element.src;
    document.getElementById("imageModal").style.display = "block";
}

//Comment Modal
var modal = document.getElementById("commentModal"),
    btn = document.getElementById("commentButton"),
    span = document.getElementsByClassName("comment-close")[0];
btn.onclick = function() {
    modal.style.display = "block"
}, span.onclick = function() {
    modal.style.display = "none"
}, window.onclick = function(n) {
    n.target == modal && (modal.style.display = "none")
};
document.addEventListener("DOMContentLoaded", () => {
    const elementos = document.querySelectorAll("h1, h2, p, img, form");
    elementos.forEach((el, i) => {
        el.style.opacity = 0;
        setTimeout(() => {
            el.style.transition = "opacity 1s ease";
            el.style.opacity = 1;
        }, i * 300);
    });
});

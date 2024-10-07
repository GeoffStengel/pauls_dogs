document.addEventListener("DOMContentLoaded", (event) => {
    gsap.registerPlugin(ScrollTrigger, Draggable);

    gsap.from('.nav-buttons', {
        duration: 1,
        y: '-300%',
        opacity: 0,
        stagger: 0.08,
        ease: 'bounce'
    });

    gsap.from('.adoption_discount', {duration: 2, ease: 'power2.in', opacity: 0});

    gsap.from('.header_banner_image', {
        duration: 1.5,
        y: '-100%',
        opacity: 0,
        ease: 'bounce'
    });

    gsap.to(".box", {
        rotation: 360,
        duration: 2,
        scrollTrigger: {
            trigger: ".box",
            toggleActions: "restart pause reverse pause"
        }
    });

    
    const puppy_grid_6_img = document.getElementsByClassName('puppy_grid_6_img');

    Draggable.create('.puppy_item', {
        bounds: puppy_grid_6_img
    });

});
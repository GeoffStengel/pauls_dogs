//Scroll Trigger For Divs To Move when Scrolling Down, Also Draggable index puppy pics code 
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

    
    const puppy_grid_6_img = document.getElementsByClassName('puppy_grid_6_img');

    Draggable.create('.puppy_item', {
        bounds: puppy_grid_6_img
    });

});
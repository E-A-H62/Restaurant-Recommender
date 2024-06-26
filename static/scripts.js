// script.js
const images = [
    'https://images.pexels.com/photos/2478248/pexels-photo-2478248.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'https://images.pexels.com/photos/16222200/pexels-photo-16222200/free-photo-of-restaurants-by-street-on-shore-in-town.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'https://images.pexels.com/photos/316093/pexels-photo-316093.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
];

let currentIndex = 0;

function changeBackground() {
    document.body.style.backgroundImage = `url(${images[currentIndex]})`;
    currentIndex = (currentIndex + 1) % images.length;
}

document.addEventListener('DOMContentLoaded', () => {
    changeBackground(); // Set the initial background image
    setInterval(changeBackground, 10000); // Change background every 10 seconds
});
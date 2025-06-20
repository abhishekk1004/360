const img = document.getElementById('image');

let rotation = 0;
img.addEventListener('click', () => {
    rotation += 45;
    img.style.transform = `rotateY(${rotation}deg)`;
});

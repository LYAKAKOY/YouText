const navSlide = () => {
    const burger = document.querySelector('.burger');
    const header = document.querySelector('.items-list');
    const itemLinks =  document.querySelectorAll('.items-list li');

    burger.addEventListener('click', ()=>{
        //Toggle Nav
        header.classList.toggle('item-active');

        //Animate Links
        itemLinks.forEach((link, index)=>{
            if(link.style.animation) {
                link.style.animation = ''
            } else {
                link.style.animation = `headerLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        });
        //Burger animation
        burger.classList.toggle('toggle');
    });

}

navSlide();

let loginBtn = document.querySelector('.item__link-login');
let closeBtn = document.querySelector('.modal-window-close');
let modalWindow = document.querySelector('.modal-window')
let fillerBlock = document.querySelector('.filler');

loginBtn.onclick = function() {
    modalWindow.style.display = 'block';
    fillerBlock.style.display = 'block';
}

closeBtn.onclick = function(event) {
    modalWindow.style.display = 'none';
    fillerBlock.style.display = 'none';
}

document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        modalWindow.style.display = 'none';
        fillerBlock.style.display = 'none';
    }
})


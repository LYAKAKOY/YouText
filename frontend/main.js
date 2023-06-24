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

function onEntry(entry) {
    entry.forEach(change => {
        if (change.isIntersecting) {
            change.target.classList.add('element-show');
        }
    });
}

window.onload = () => {
    let options = {
        threshold: 0.5
    };
    let observer = new IntersectionObserver(onEntry, options);
    let elementsTitle = document.querySelectorAll('.main__title');
    let elementsSubtitle = document.querySelectorAll('.main__subtitle');

    
    for (let elm of elementsTitle) {
        observer.observe(elm);
    }
    
    for (let elm of elementsSubtitle) {
        observer.observe(elm);
    }
}

const dom = {
    loginBtn: document.querySelector('.item__link-login'),
    closeBtn: document.querySelector('.modal-window-close'),
    modalWindow: document.querySelector('.modal-window'),
    fillerBlock: document.querySelector('.filler'),
    mainContainer: document.querySelector('.main__container'),
    paramsButton: document.querySelector('.main__params-title-button'),
    mainParams: document.querySelector('.main__params'),
    paramsInner: document.querySelector('.main__params-inner')
}

dom.loginBtn.onclick = function() {
    dom.modalWindow.style.display = 'flex';
    dom.fillerBlock.style.display = 'block';
}

dom.closeBtn.onclick = function() {
    dom.modalWindow.style.display = 'none';
    dom.fillerBlock.style.display = 'none';
}

function changeHeight() {
    if (dom.mainContainer.classList.contains('opened') && dom.mainParams.classList.contains('opened')) {
        dom.mainContainer.classList.remove('opened');
        dom.mainParams.classList.remove('opened');
    }
    else {
        dom.mainContainer.classList.add('opened');
        dom.mainParams.classList.add('opened');
    }
}

function changeVisibility() {
    dom.paramsInner.style.display === "flex" 
    ? dom.paramsInner.style.display = "none" 
    : dom.paramsInner.style.display = "flex";
}

function changeButton() {
    dom.mainContainer.classList.contains('opened')
    ? dom.paramsButton.style.backgroundImage = "url(media/system-icons/Arrow_up.svg"
    : dom.paramsButton.style.backgroundImage = "url(media/system-icons/Arrow_down.svg)"
}

document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        dom.modalWindow.style.display = 'none';
        dom.fillerBlock.style.display = 'none';
    }
})

dom.paramsButton.onclick = function() {
    changeHeight();
    changeVisibility();
    changeButton();
}
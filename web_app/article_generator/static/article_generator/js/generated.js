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

const dom = {
    loginBtn: document.querySelector('.item__link-login'),
    closeBtn: document.querySelector('.modal-window-close'),
    modalWindow: document.querySelector('.modal-window'),
    fillerBlock: document.querySelector('.filler'),
    textarea: document.querySelector('.item__text'),
    successBtn: document.querySelector('.success-notification'),
    copyBtn: document.querySelector('.copy-button')
}

dom.loginBtn.onclick = function() {
    dom.modalWindow.style.display = 'flex';
    dom.fillerBlock.style.display = 'block';
}

dom.closeBtn.onclick = function() {
    dom.modalWindow.style.display = 'none';
    dom.fillerBlock.style.display = 'none';
}

document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        dom.modalWindow.style.display = 'none';
        dom.fillerBlock.style.display = 'none';
    }
})


function setSelection() {
    let target = dom.textarea;
    rng = document.createRange();
    rng.selectNode(target)
    sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(rng);
    try {
        document.execCommand('copy');
        successNotification();
        dom.successBtn.style.display = 'flex';
    } catch(err) {
        console.log('Oops, unable to copy');
    }
     sel.removeAllRanges();
}

function successNotification() {
    setTimeout(function() {
        dom.successBtn.classList.add('closed');
    }, 2000)
    dom.copyBtn.disabled = true;

    setTimeout(function() {
        dom.successBtn.classList.remove('closed');
        dom.successBtn.style.display = 'none';
        dom.copyBtn.disabled = false;
    }, 2200)
}

function autoAdjust() {
    dom.textarea.style.height = 'auto';
    dom.textarea.style.height = dom.textarea.scrollHeight + 'px';
}

autoAdjust();







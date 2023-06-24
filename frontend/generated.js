const startTime = [...document.querySelectorAll(".start-time")];
let separator = document.querySelector('.separator');
const finishTime = [...document.querySelectorAll(".finish-time")];
let text = document.querySelectorAll('.item__text').innerHTML;
let textItems = document.querySelectorAll('.main__inner-right-info-item');

// console.log((startTime.forEach(x => JSON.stringify(x.innerHTML))));

// function copyContent() {
//     // navigator.clipboard.writeText(`${startTime} ${separator} ${finishTime} ${text}`);
//     // console.log('Content copied to clipboard');
//     navigator.clipboard.writeText(JSON.stringify(startTime.innerHTML))
// }

function copyContent() {
    for(item of startTime) {
        for (item1 of finishTime)
            navigator.clipboard.writeText(`${item.innerHTML} ${separator.innerHTML} ${item1.innerHTML}`);
    }
}




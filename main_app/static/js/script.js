// let cardContent = document.getElementsByClassName('card-content');
 
// for (let i=0; i<cardContent.length; i++) {
//     cardContent[i].addEventListener('click', handleClick);
// }

// let closeModalEls = document.getElementsByClassName('closeModal');

// function handleClick(evt) {
//     // let key = JSON.stringify('key');
//     // key = JSON.parse(key);
//     // console.log(key);
//     let modals = document.getElementsByClassName('modal');
//     console.log(modals);
//     console.log(evt);
//     evt.target.firstElementChild.style.display = "block";
//     for (let i=0; i<closeModalEls.length; i++) {
//         closeModalEls[i].innerHTML = `<button>Close</button>`
//     }
// }

// for (let i=0; i<closeModalEls.length; i++) {
//     closeModalEls[i].addEventListener('click', function(evt) {
//         evt.target.offsetParent.style.display = "none";
//     })
// }





// const dataLocEl = document.getElementById('data-locations');
// console.log(dataLocEl);

// pollEl = ''
// siteEl = ''
// dropEl = ''

// const plBtnEl = document.getElementById('pl-btn')
// plBtnEl.addEventListener("click", function() {
//     siteEl.innerHTML = '';
//     dropEl.innerHTML = '';
//     pollEl = document.createElement('pollingLocations');
//     pollEl.innerHTML = 'Here are some polling locations!';
//     dataLocEl.appendChild(pollEl);
// });

// const evsBtnEl = document.getElementById('evs-btn')
// console.log(evsBtnEl);
// evsBtnEl.addEventListener("click", function() {
//     pollEl.innerHTML = '';
//     dropEl.innerHTML = '';
//     siteEl = document.createElement('earlyVotingSites');
//     siteEl.innerHTML = "These are some early voting sites!";
//     dataLocEl.appendChild(siteEl);
// });

// const dolBtnEl = document.getElementById('dol-btn')
// console.log(dolBtnEl);
// dolBtnEl.addEventListener("click", function() {
//     pollEl.innerHTML = '';
//     siteEl.innerHTML = '';
//     dropEl = document.createElement('dropOffLocations');
//     dropEl.innerHTML = "You can drop off your ballots here!";
//     dataLocEl.appendChild(dropEl);
// })

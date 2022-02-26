const swiper = new Swiper('.swiper', {
  slidesPerView: 3,
  spaceBetween: 30,
  slidesPerGroup: 1,
  loop: true,
  loopFillGroupWithBlank: true,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
<<<<<<< HEAD
});
function nextClick(){
  document.getElementById("next").click();
}

setInterval(nextClick, 1500);
=======
  });

  
>>>>>>> 143fcfa6753c637ce9d14c9c144d123bce8b13f0

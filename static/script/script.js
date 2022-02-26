const swiper = new Swiper('.swiper', {
    slidesPerView: 3,
    spaceBetween: 30,
    // If you want to use pagination then uncomment below
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  });
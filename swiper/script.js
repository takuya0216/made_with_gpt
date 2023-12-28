document.addEventListener('DOMContentLoaded', function () {
  var swiper = new Swiper('.swiper-container', {
    loop: true,
    slidesPerView: 1.8, // 一度に表示されるスライドの数
    centeredSlides: true, // 現在のスライドを中央に配置
    spaceBetween: 20, // スライドとスライドの隙間の設定
    autoplay: {
      delay: 5000, // 自動再生の遅延時間（ミリ秒）
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });
});

window.addEventListener("DOMContentLoaded", () => {

    
  let mobile_toggle_btn = document.getElementById('mobile-menu_toggle');
  let mobile_close_btn = document.getElementById('mobile-menu_close');
  let offcanvas = document.getElementById('offcanvas-nav');

  mobile_close_btn.classList.add('uk-hidden');

  // When the offcanvas is shown, add the "open" class
  UIkit.util.on(offcanvas, 'show', function() {
    mobile_close_btn.classList.remove('uk-hidden');
    mobile_toggle_btn.classList.add('uk-hidden');
    
  });

  // When the offcanvas is hidden, remove the "open" class
  UIkit.util.on(offcanvas, 'hide', function() {
    mobile_close_btn.classList.add('uk-hidden');
    mobile_toggle_btn.classList.remove('uk-hidden');
    
  });

  mobile_close_btn.addEventListener('click', () => {
    UIkit.offcanvas(offcanvas).hide();
    mobile_close_btn.classList.add('uk-hidden');
    mobile_toggle_btn.classList.remove('uk-hidden');
  });
});
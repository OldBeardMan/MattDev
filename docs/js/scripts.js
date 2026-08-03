/*!
* Start Bootstrap - Freelancer v7.0.7 (https://startbootstrap.com/theme/freelancer)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-freelancer/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

// Numer telefonu - ochrona przed scraperami.
// W źródle HTML nie ma ani jednej cyfry numeru ani linku tel: - numer jest
// zapisany w atrybucie data-tel jako base64 z odwróconą kolejnością znaków
// i składany dopiero tutaj, po stronie przeglądarki. Boty zbierające numery
// regexem po surowym HTML-u nie mają czego złapać.
// Kod jest poza DOMContentLoaded, bo scripts.js ładuje się na końcu <body>
// - elementy już istnieją, więc numer pojawia się bez migotania.
(function () {
    var slots = document.querySelectorAll('[data-tel]');

    for (var i = 0; i < slots.length; i++) {
        var slot = slots[i];
        var number;

        try {
            number = atob(slot.getAttribute('data-tel')).split('').reverse().join('');
        } catch (e) {
            continue;
        }

        // +48502836411 -> "502 836 411"
        var label = number.replace(/^\+48/, '').replace(/(\d{3})(?=\d)/g, '$1 ');

        var link = document.createElement('a');
        link.href = 'tel:' + number;
        link.textContent = label;

        var extraClass = slot.getAttribute('data-tel-class');
        if (extraClass) {
            link.className = extraClass;
        }

        slot.textContent = '';
        slot.appendChild(link);
    }
})();


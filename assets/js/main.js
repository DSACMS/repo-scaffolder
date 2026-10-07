document.addEventListener('DOMContentLoaded', function () {

    // // Federal banner opening functionality
    // const bannerButton = document.querySelector('.usa-banner__button');
    // const bannerContent = document.getElementById('gov-banner');
    // const cmsHeader = document.querySelector('.cms-header');
    // let bannerExpanded = false;

    // if (bannerButton && bannerContent) {
    //     bannerContent.style.display = 'none';

    //     bannerButton.addEventListener('click', function () {
    //         bannerExpanded = !bannerExpanded;
    //         this.setAttribute('aria-expanded', bannerExpanded);

    //         // hacky but only way i got this to expand and close with the custom banner
    //         if (bannerExpanded) {
    //             bannerContent.style.display = 'block';
    //             if (cmsHeader) {
    //                 cmsHeader.style.top = bannerContent.offsetHeight + 24 + 'px';
    //             }
    //         } else {
    //             bannerContent.style.display = 'none';
    //             if (cmsHeader) {
    //                 cmsHeader.style.top = '24px';
    //             }
    //         }
    //     });
    // }

    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const mainMenu = document.getElementById('main-menu');

    if (menuToggle && mainMenu) {
        menuToggle.addEventListener('click', function () {
            const expanded = this.getAttribute('aria-expanded') === 'true' || false;
            this.setAttribute('aria-expanded', !expanded);
            mainMenu.classList.toggle('show');
        });

        document.addEventListener('click', function (e) {
            if (!menuToggle.contains(e.target) && !mainMenu.contains(e.target) && mainMenu.classList.contains('show')) {
                mainMenu.classList.remove('show');
                menuToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const target = document.querySelector(this.getAttribute('href'));

            if (target) {
                // Adjust the scroll position to account for the fixed header
                const headerHeight = document.querySelector('.cms-header').offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.scrollY;
                const offsetPosition = targetPosition - headerHeight;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Keyboard navigation for cards
    const cards = document.querySelectorAll('.feature-card, .doc-card');
    cards.forEach(card => {
        card.setAttribute('tabindex', '0');

        card.addEventListener('keydown', function (e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                const link = this.querySelector('a');
                if (link) {
                    link.click();
                }
            }
        });
    });

    // // dynamic nav bar based on scroll position
    // const sections = document.querySelectorAll('section[id]');
    // const navItems = document.querySelectorAll('nav ul li a');

    // function setActiveNavItem() {
    //     const scrollPosition = window.scrollY;
    //     const headerHeight = document.querySelector('header').offsetHeight;
    //     const bannerHeight = document.querySelector('.usa-banner').offsetHeight;
    //     const totalOffset = headerHeight + bannerHeight;

    //     navItems.forEach(item => {
    //         item.removeAttribute('aria-current');
    //     });

    //     const documentationSection = document.getElementById('documentation');

    //     if (scrollPosition < (documentationSection.offsetTop - totalOffset - 100)) {
    //         navItems.forEach(item => {
    //             if (item.getAttribute('href') === '#hero') {
    //                 item.setAttribute('aria-current', 'page');
    //             }
    //         });
    //         return;
    //     }
    //     let currentSection = null;

    //     sections.forEach(section => {
    //         if (section.id === 'hero') return;

    //         const sectionTop = section.offsetTop - totalOffset - 100;
    //         const sectionBottom = sectionTop + section.offsetHeight;

    //         if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
    //             currentSection = section.id;
    //         }
    //     });

    //     if (currentSection) {
    //         navItems.forEach(item => {
    //             if (item.getAttribute('href') === '#' + currentSection) {
    //                 item.setAttribute('aria-current', 'page');
    //             }
    //         });
    //     }
    // }

    // window.addEventListener('scroll', setActiveNavItem);
    // setActiveNavItem();
});
const toggle = document.querySelector('.toggle');
const navigation = document.querySelector('.navigation');

toggle.addEventListener('click', () => {
    toggle.classList.toggle('active');
    navigation.classList.toggle('active');

    // Randomly change menu colour to be dark red or dark blue:

    let color_dark_red = 'rgb(128, 0, 32)';
    let color_dark_blue = 'navy';
    var random_boolean = Math.random() < 0.5;
    if (random_boolean) {
        navigation.style.setProperty('background', color_dark_red);
    } else {
        navigation.style.setProperty('background', color_dark_blue);
    }
});

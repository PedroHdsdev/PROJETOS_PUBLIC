
    let currentIndex = 0;

    function showImage(index) {
        const carousel = document.querySelector('.carousel');
        const images = document.querySelectorAll('.carousel-img');
        const totalImages = images.length;

        // Certifique-se de que o índice está no intervalo correto
        if (index >= totalImages) {
            currentIndex = 0;
        } else if (index < 0) {
            currentIndex = totalImages - 1;
        } else {
            currentIndex = index;
        }

        // Mova o carrossel para mostrar a imagem correta
        carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    function nextImage() {
        showImage(currentIndex + 1);
    }

    function prevImage() {
        showImage(currentIndex - 1);
    }

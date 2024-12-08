document.addEventListener('DOMContentLoaded', function () {
    // Додаємо анімацію для заголовків
    const headers = document.querySelectorAll('h1, h2');
    headers.forEach(header => {
        header.style.opacity = '0';
        header.style.transition = 'opacity 0.5s ease-in-out';
        setTimeout(() => {
            header.style.opacity = '1';
        }, 300);
    });

    // Додаємо обробник подій для форми
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function (event) {
            const title = form.querySelector('input[name="title"]');
            const content = form.querySelector('textarea[name="content"]');
            if (title.value.trim() === '' || content.value.trim() === '') {
                event.preventDefault();
                alert('Будь ласка, заповніть всі поля форми.');
            }
        });
    }
});



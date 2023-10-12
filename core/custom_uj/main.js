// Пример кастомного JavaScript для Jazzmin

// Изменение текста при загрузке страницы
document.addEventListener("DOMContentLoaded", function () {
    const welcomeText = document.querySelector(".welcome-text");
    if (welcomeText) {
        welcomeText.textContent = "Добро пожаловать на Jazzmin!";
    }
});

// Добавление дополнительного функционала
const customButton = document.querySelector("#custom-button");
if (customButton) {
    customButton.addEventListener("click", function () {
        alert("Вы нажали на кастомную кнопку!");
    });
}

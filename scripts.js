function loadHeader() {
    fetch('header.html')
        .then(response => response.text())
        .then(data => {
            document.body.insertAdjacentHTML('afterbegin', data);
            checkAuthStatus();
            setCurrentYear();
        });
}

function setCurrentYear() {
    const currentYear = new Date().getFullYear();
    document.getElementById('currentYear').textContent = currentYear;
}

document.addEventListener('DOMContentLoaded', loadHeader);

function toggleMenu() {
    const navLinks = document.getElementById("nav-links");
    navLinks.classList.toggle("show");
}

function checkAuth(page) {
    if (localStorage.getItem('isLoggedIn') === 'true' || sessionStorage.getItem('isLoggedIn') === 'true') {
        window.location.href = page;
    } else {
        sessionStorage.setItem("intendedPage", page);
        showLoginMessage();
    }
}

function showLoginMessage() {
    document.getElementById("login-message").style.display = "block";
}

function checkAuthStatus() {
    const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true' || sessionStorage.getItem('isLoggedIn') === 'true';
    document.getElementById("logout-nav").style.display = isLoggedIn ? "block" : "none";
}

function logout() {
    localStorage.removeItem("rememberMe");
    localStorage.removeItem("email");
    localStorage.removeItem("password");
    localStorage.removeItem("isLoggedIn");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("password");
    sessionStorage.removeItem("isLoggedIn");
    sessionStorage.removeItem("intendedPage");
    window.location.href = 'index.html';
}

document.addEventListener('DOMContentLoaded', loadHeader);
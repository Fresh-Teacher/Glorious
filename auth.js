function checkAuth() {
    const isRemembered = localStorage.getItem("rememberMe") === "true";
    const sessionEmail = sessionStorage.getItem("email");
    const localEmail = localStorage.getItem("email");
    const email = isRemembered ? localEmail : sessionEmail;

    if (!((isRemembered && localEmail === "user@glorious.com" && localStorage.getItem("password") === "User") ||
        (sessionEmail === "user@glorious.com" && sessionStorage.getItem("password") === "User"))) {
        // Store the page they were trying to access
        localStorage.setItem("intendedPage", window.location.href);
        window.location.href = "index.html?needLogin=true";
    }
}
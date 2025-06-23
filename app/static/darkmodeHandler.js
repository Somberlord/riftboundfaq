/* Dark mode toggle script */
function toggleDarkMode() {
    const isDark = document.body.classList.toggle('dark-mode');
    document.body.classList.toggle('light-mode', !isDark);
    localStorage.setItem('darkMode', isDark);
    updateDarkModeButton();
    updateMightIcons();
}

function updateDarkModeButton() {
    const btn = document.getElementById('darkModeBtn');
    if (!btn) return;
    if (document.body.classList.contains('dark-mode')) {
        btn.innerText = '🌙 Dark Mode';
    } else {
        btn.innerText = '☀️ Light Mode';
    }
}

function updateMightIcons() {
    const isDark = document.body.classList.contains('dark-mode');
    document.querySelectorAll('.might-icon').forEach(img => {
        img.src = isDark ? img.dataset.dark : img.dataset.light;
    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Restore dark mode if previously set
    const darkPref = localStorage.getItem('darkMode') === 'true';
    document.body.classList.toggle('dark-mode', darkPref);
    document.body.classList.toggle('light-mode', !darkPref);
    // Add toggle button if not present
    if (!document.getElementById('darkModeBtn')) {
        const btn = document.createElement('button');
        btn.id = 'darkModeBtn';
        btn.className = 'btn btn-secondary position-fixed m-3';
        btn.style.top = '0';
        btn.style.right = '0';
        btn.onclick = toggleDarkMode;
        document.body.appendChild(btn);
    }
    updateDarkModeButton();
    updateMightIcons();
});

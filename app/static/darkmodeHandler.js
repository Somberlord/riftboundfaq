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

document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('darkmode-toggle');
    const icon = document.getElementById('darkmode-toggle-icon');
    if (!toggleBtn) return;

    function setIcon(isDark) {
        icon.textContent = isDark ? '☀️' : '🌙';
    }

    function setDarkMode(isDark) {
        document.body.classList.toggle('dark-mode', isDark);
        document.body.classList.toggle('light-mode', !isDark);
        setIcon(isDark);
    }

    // Load preference
    let dark = localStorage.getItem('darkmode') === 'true';
    setDarkMode(dark);

    toggleBtn.addEventListener('click', function () {
        dark = !dark;
        setDarkMode(dark);
        localStorage.setItem('darkmode', dark);
        // Swap might icon if present
        document.querySelectorAll('.might-icon').forEach(function(img) {
            if (img.dataset.light && img.dataset.dark) {
                img.src = dark ? img.dataset.dark : img.dataset.light;
            }
        });
    });

    // Sidebar collapse logic
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebarToggleIcon = document.getElementById('sidebar-toggle-icon');
    if (sidebar && sidebarToggle && sidebarToggleIcon) {
        let collapsed = localStorage.getItem('sidebar-collapsed') === 'true';
        function setSidebar(collapsed) {
            sidebar.classList.toggle('collapsed', collapsed);
            sidebarToggleIcon.textContent = collapsed ? '⮞' : '⮜';
        }
        setSidebar(collapsed);
        sidebarToggle.addEventListener('click', function () {
            collapsed = !collapsed;
            setSidebar(collapsed);
            localStorage.setItem('sidebar-collapsed', collapsed);
        });
    }
});

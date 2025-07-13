// Handles the arrow toggle for the Guides expandable menu in both desktop and mobile navs
document.addEventListener('DOMContentLoaded', function () {
  // Arrow toggle for desktop
  var guidesCollapse = document.getElementById('guidesCollapse');
  var guideArrowDesktop = document.getElementById('guideArrowDesktop');
  if (guidesCollapse && guideArrowDesktop) {
    guidesCollapse.addEventListener('show.bs.collapse', function () {
      guideArrowDesktop.innerHTML = '\u25BC'; // ▼
    });
    guidesCollapse.addEventListener('hide.bs.collapse', function () {
      guideArrowDesktop.innerHTML = '\u25B6'; // ▶
    });
  }
  // Arrow toggle for mobile
  var guidesCollapseMobile = document.getElementById('guidesCollapseMobile');
  var guideArrowMobile = document.getElementById('guideArrowMobile');
  if (guidesCollapseMobile && guideArrowMobile) {
    guidesCollapseMobile.addEventListener('show.bs.collapse', function () {
      guideArrowMobile.innerHTML = '\u25BC'; // ▼
    });
    guidesCollapseMobile.addEventListener('hide.bs.collapse', function () {
      guideArrowMobile.innerHTML = '\u25B6'; // ▶
    });
  }
  // Arrow toggle for Sets menu (desktop)
  var setsCollapse = document.getElementById('setsCollapse');
  var setsArrowDesktop = document.getElementById('setsArrowDesktop');
  if (setsCollapse && setsArrowDesktop) {
    setsCollapse.addEventListener('show.bs.collapse', function () {
      setsArrowDesktop.innerHTML = '\u25BC'; // ▼
    });
    setsCollapse.addEventListener('hide.bs.collapse', function () {
      setsArrowDesktop.innerHTML = '\u25B6'; // ▶
    });
  }
});

const sidebarItems = document.querySelectorAll(".sidebar-item");
const pages = document.querySelectorAll(".page");
const sidebar = document.querySelector('.sidebar');
const sidebarCursor = document.querySelector('.sidebar-cursor');
let startX;
let startWidth;

sidebarCursor.addEventListener('mousedown', (e) => {
  startX = e.clientX;
  startWidth = parseInt(document.defaultView.getComputedStyle(sidebar).width, 10);
  document.documentElement.addEventListener('mousemove', doDrag, false);
  document.documentElement.addEventListener('mouseup', stopDrag, false);
});

function doDrag(e) {
  sidebar.style.width = startWidth + e.clientX - startX + 'px';
}

function stopDrag(e) {
  document.documentElement.removeEventListener('mousemove', doDrag, false);
  document.documentElement.removeEventListener('mouseup', stopDrag, false);
}

sidebarItems.forEach((item) => {
  item.addEventListener("click", (event) => {
    const page = event.currentTarget.getAttribute("data-page");

    sidebarItems.forEach((item) => {
      item.classList.remove("active");
    });
    event.currentTarget.classList.add("active");

    pages.forEach((page) => {
      page.classList.remove("active");
    });
    document.querySelector(`.page[data-page="${page}"]`).classList.add("active");
  });
});

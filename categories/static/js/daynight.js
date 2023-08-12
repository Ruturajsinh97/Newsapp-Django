const toggle = document.getElementById("slideToggle");
toggle.addEventListener("change", () => {
  document.body.classList.toggle("night-mode", toggle.checked);
});

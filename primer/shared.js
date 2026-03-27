/* Industry Primer — shared JS (all showTab primers) */
function showTab(name, idx) {
  document.querySelectorAll(".tab-section").forEach(function(s) { s.classList.remove("active"); });
  document.querySelectorAll(".tab-btn").forEach(function(b) { b.classList.remove("active"); });
  document.getElementById("tab-" + name).classList.add("active");
  document.querySelectorAll(".tab-btn")[idx].classList.add("active");
  document.querySelectorAll(".progress-dot").forEach(function(d, i) { d.classList.toggle("active", i === idx); });
  document.getElementById("progress-label").textContent = "Section " + (idx + 1) + " of 9";
}
function toggleGloss(header) { header.parentElement.classList.toggle("open"); }
(function() {
  var glossSearch = document.getElementById("gloss-search");
  if (glossSearch) {
    glossSearch.addEventListener("input", function() {
      var q = glossSearch.value.trim().toLowerCase();
      document.querySelectorAll(".glossary-item").forEach(function(item) {
        var terms = item.dataset.terms || "";
        item.style.display = (!q || terms.includes(q) || item.textContent.toLowerCase().includes(q)) ? "" : "none";
      });
    });
  }
  document.addEventListener("keydown", function(e) {
    if (e.key === "/" && document.activeElement !== glossSearch) { e.preventDefault(); if (glossSearch) glossSearch.focus(); }
  });
})();

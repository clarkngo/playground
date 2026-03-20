/** Shared utilities for static lab pages */

function showFeedback(correct, html) {
  const fb = document.getElementById('feedback');
  if (!fb) return;
  fb.className = 'feedback-box show ' + (correct ? 'feedback-correct' : 'feedback-incorrect');
  fb.innerHTML = (correct ? '✅ ' : '❌ ') + html;
  if (correct) {
    const why = document.getElementById('why-matters');
    if (why) setTimeout(() => { why.classList.add('show'); why.scrollIntoView({behavior:'smooth',block:'nearest'}); }, 350);
  }
  fb.scrollIntoView({behavior:'smooth', block:'nearest'});
}

function markBtn(btn, correct) {
  const parent = btn.closest('.options-grid, .question-box');
  if (parent) parent.querySelectorAll('.opt-btn').forEach(b => b.classList.remove('correct','incorrect'));
  btn.classList.add(correct ? 'correct' : 'incorrect');
}

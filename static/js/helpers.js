// Shared helpers for AI 101 Academy front-end components.

function getCookie(name) {
  const match = document.cookie.match(new RegExp("(^|;\\s*)" + name + "=([^;]*)"));
  return match ? decodeURIComponent(match[2]) : null;
}

async function postJSON(url, data) {
  const resp = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify(data || {}),
  });
  if (!resp.ok) {
    let detail = "Request failed";
    try { detail = (await resp.json()).error || detail; } catch (e) { /* noop */ }
    throw new Error(detail);
  }
  return resp.json();
}

async function getJSON(url) {
  const resp = await fetch(url);
  if (!resp.ok) throw new Error("Request failed");
  return resp.json();
}

// Minimal, safe markdown renderer (bold, italics, inline code, lists, paragraphs).
function mdToHtml(text) {
  const escapeHtml = (s) =>
    s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  const inline = (s) =>
    escapeHtml(s)
      .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
      .replace(/\*(.+?)\*/g, "<em>$1</em>")
      .replace(/`([^`]+)`/g, "<code style=\"background:#eaedff;padding:0 4px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:0.85em\">$1</code>");

  const lines = String(text).split("\n");
  let html = "";
  let inList = false;
  for (const line of lines) {
    const listMatch = line.match(/^\s*[-*]\s+(.*)/) || line.match(/^\s*\d+\.\s+(.*)/);
    if (listMatch) {
      if (!inList) { html += "<ul>"; inList = true; }
      html += "<li>" + inline(listMatch[1]) + "</li>";
    } else {
      if (inList) { html += "</ul>"; inList = false; }
      if (line.trim()) html += "<p>" + inline(line) + "</p>";
    }
  }
  if (inList) html += "</ul>";
  return html;
}

// "Mark Lesson Complete" button on lessons without a quiz.
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("complete-btn");
  if (!btn) return;
  btn.addEventListener("click", async () => {
    btn.disabled = true;
    btn.textContent = "Saving…";
    try {
      const data = await postJSON(`/api/lessons/${btn.dataset.lessonId}/complete/`, {});
      btn.textContent = data.certificate_issued
        ? "🎓 Course complete! Redirecting to your certificate…"
        : "✓ Lesson completed";
      btn.classList.remove("bg-primary-container");
      btn.classList.add("bg-success");
      setTimeout(() => window.location.reload(), data.certificate_issued ? 1500 : 800);
      if (data.certificate_issued) setTimeout(() => (window.location.href = "/certificates/"), 1500);
    } catch (err) {
      btn.disabled = false;
      btn.textContent = "Mark Lesson Complete";
      alert("Could not save progress: " + err.message);
    }
  });
});

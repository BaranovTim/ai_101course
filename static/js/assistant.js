// Proactive AI assistant widget: shiny floating button (bottom-right) with a
// mini chat panel. Pops up on wrong quiz answers to offer help, and
// occasionally opens on its own with a fun AI fact.
(function () {
  // Skip on the full tutor page — it already IS the chat.
  if (document.getElementById("tutor-root")) return;
  // Only for signed-in app pages (helpers.js is present there).
  if (typeof postJSON !== "function") return;

  const FACTS = [
    "💡 **Fun fact:** ChatGPT reached 100 million users in just 2 months — the fastest-growing consumer app in history.",
    "💡 **Fun fact:** The word 'robot' comes from the Czech word *robota*, meaning 'forced labour' — coined in a 1920 play.",
    "💡 **Fun fact:** Modern language models learned from more text than a human could read in 10,000 lifetimes.",
    "💡 **Fun fact:** The Transformer — the 'T' in ChatGPT — was invented in 2017 in a paper called *Attention Is All You Need*.",
    "💡 **Fun fact:** AI models don't 'look up' answers — they generate them word by word, like super-powered autocomplete.",
    "💡 **Pro tip:** Adding 'think through this step by step' to a prompt measurably improves AI reasoning.",
    "💡 **Pro tip:** Paste an example of the writing style you want — showing beats telling, every time.",
    "💡 **Fun fact:** In 1997, IBM's Deep Blue beat world chess champion Garry Kasparov — a landmark moment for AI.",
  ];

  // ---------- Build DOM ----------
  const root = document.createElement("div");
  root.innerHTML = `
    <button id="ai101-fab" class="ai101-fab fixed bottom-6 right-6 z-50 flex h-14 w-14 items-center justify-center rounded-full bg-gradient-to-br from-primary to-secondary text-white transition hover:scale-105" title="AI Tutor — ask me anything">
      <span class="material-symbols-outlined">smart_toy</span>
    </button>
    <div id="ai101-panel" class="ai101-panel fixed bottom-24 right-6 z-50 hidden w-[22rem] max-w-[calc(100vw-2.5rem)] flex-col overflow-hidden rounded-2xl border border-outline-variant/50 bg-white shadow-glow" style="max-height: 70vh">
      <div class="flex items-center justify-between bg-gradient-to-r from-primary to-secondary px-4 py-3 text-white">
        <div class="flex items-center gap-2">
          <span class="material-symbols-outlined text-xl">smart_toy</span>
          <p class="text-sm font-semibold">AI Tutor</p>
        </div>
        <div class="flex items-center gap-1">
          <a href="/tutor/" class="rounded-md p-1 hover:bg-white/15" title="Open full chat"><span class="material-symbols-outlined text-lg">open_in_full</span></a>
          <button id="ai101-close" class="rounded-md p-1 hover:bg-white/15" title="Close"><span class="material-symbols-outlined text-lg">close</span></button>
        </div>
      </div>
      <div id="ai101-msgs" class="flex-1 space-y-3 overflow-y-auto p-4" style="min-height: 8rem"></div>
      <div id="ai101-actions" class="hidden flex-wrap gap-2 px-4 pb-2"></div>
      <form id="ai101-form" class="flex items-end gap-2 border-t border-outline-variant/40 p-3">
        <input id="ai101-input" type="text" placeholder="Ask a quick question…"
               class="flex-1 rounded-lg border border-outline-variant bg-white px-3 py-2 text-sm placeholder:text-outline focus:border-primary focus:ring-4 focus:ring-primary/10 focus:outline-none transition"/>
        <button type="submit" class="flex h-9 w-9 items-center justify-center rounded-lg bg-primary-container text-white shadow-card transition hover:-translate-y-px">
          <span class="material-symbols-outlined text-lg">send</span>
        </button>
      </form>
    </div>`;
  document.body.appendChild(root);

  const fab = document.getElementById("ai101-fab");
  const panel = document.getElementById("ai101-panel");
  const msgs = document.getElementById("ai101-msgs");
  const form = document.getElementById("ai101-form");
  const input = document.getElementById("ai101-input");
  const actions = document.getElementById("ai101-actions");
  let greeted = false;
  let busy = false;

  function addBubble(role, content) {
    const wrap = document.createElement("div");
    wrap.className = "flex " + (role === "user" ? "justify-end" : "justify-start");
    const b = document.createElement("div");
    b.className =
      "chat-bubble max-w-[85%] rounded-2xl px-4 py-2.5 text-sm leading-relaxed shadow-card " +
      (role === "user"
        ? "rounded-br-md bg-primary-container text-white"
        : "rounded-bl-md border border-outline-variant/50 bg-surface-container-low");
    b.innerHTML = mdToHtml(content);
    wrap.appendChild(b);
    msgs.appendChild(wrap);
    msgs.scrollTop = msgs.scrollHeight;
    return wrap;
  }

  function setActions(buttons) {
    actions.innerHTML = "";
    if (!buttons || !buttons.length) {
      actions.classList.add("hidden");
      actions.classList.remove("flex");
      return;
    }
    actions.classList.remove("hidden");
    actions.classList.add("flex");
    buttons.forEach(({ label, onClick }) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.textContent = label;
      btn.className =
        "rounded-full border border-outline-variant bg-white px-3 py-1.5 text-xs font-medium transition hover:border-primary hover:text-primary";
      btn.addEventListener("click", () => { setActions([]); onClick(); });
      actions.appendChild(btn);
    });
  }

  function openPanel() {
    panel.classList.remove("hidden");
    panel.classList.add("flex");
    if (!greeted) {
      greeted = true;
      addBubble("assistant", "Hi! I'm your AI tutor. Ask me anything about the lesson — or anything AI-related. 👋");
    }
  }

  function closePanel() {
    panel.classList.add("hidden");
    panel.classList.remove("flex");
  }

  fab.addEventListener("click", () => {
    panel.classList.contains("hidden") ? openPanel() : closePanel();
  });
  document.getElementById("ai101-close").addEventListener("click", closePanel);

  async function send(text) {
    if (busy) return;
    const message = (text || input.value).trim();
    if (!message) return;
    input.value = "";
    addBubble("user", message);
    busy = true;
    const typing = addBubble("assistant", "…");
    try {
      const data = await postJSON("/tutor/api/chat/", { message });
      typing.remove();
      addBubble("assistant", data.reply);
    } catch (e) {
      typing.remove();
      addBubble("assistant", "Sorry — something went wrong. Please try again.");
    } finally {
      busy = false;
    }
  }

  form.addEventListener("submit", (e) => { e.preventDefault(); send(); });

  // ---------- Proactive: wrong quiz answers ----------
  document.addEventListener("ai101:quiz-feedback", (e) => {
    const d = e.detail || {};
    if (!d.wrong || !d.wrong.length) return;
    openPanel();
    const first = d.wrong[0];
    const plural = d.wrong.length > 1 ? `${d.wrong.length} questions` : "one question";
    addBubble(
      "assistant",
      `I noticed the quiz didn't quite go to plan — ${plural} tripped you up. ` +
        (first.explanation
          ? `For example:\n\n**"${first.question}"**\n\n${first.explanation}\n\nWant me to explain it another way?`
          : `Want to talk through **"${first.question}"** together?`)
    );
    setActions([
      {
        label: "Yes, explain it differently",
        onClick: () =>
          send(`I got this quiz question wrong: "${first.question}". Please explain the concept behind it in a simple, different way with an example.`),
      },
      { label: "Give me a practice question", onClick: () => send(`Give me one practice question about: "${first.question}"`) },
      { label: "I'm okay, thanks!", onClick: () => addBubble("assistant", "No problem — you've got this! Retake the quiz whenever you're ready. 💪") },
    ]);
  });

  // ---------- Proactive: random fun fact ----------
  try {
    const shownThisSession = sessionStorage.getItem("ai101FactShown");
    if (!shownThisSession && Math.random() < 0.35) {
      setTimeout(() => {
        if (!panel.classList.contains("hidden")) return; // don't interrupt a live chat
        sessionStorage.setItem("ai101FactShown", "1");
        openPanel();
        addBubble("assistant", FACTS[Math.floor(Math.random() * FACTS.length)]);
        setActions([
          { label: "Tell me another!", onClick: () => { addBubble("assistant", FACTS[Math.floor(Math.random() * FACTS.length)]); } },
          { label: "Close", onClick: closePanel },
        ]);
      }, 12000 + Math.random() * 18000);
    }
  } catch (e) { /* sessionStorage unavailable — skip */ }
})();

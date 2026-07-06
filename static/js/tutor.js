// AI Tutor chat — React component (no build step, uses React.createElement).
(function () {
  const root = document.getElementById("tutor-root");
  if (!root) return;

  const h = React.createElement;
  const { useState, useRef, useEffect } = React;

  let initialHistory = [];
  const historyEl = document.getElementById("tutor-history");
  if (historyEl) {
    try { initialHistory = JSON.parse(historyEl.textContent); } catch (e) { /* noop */ }
  }

  const SUGGESTIONS = [
    "How do I write a good prompt?",
    "Explain how ChatGPT works in simple terms",
    "How can AI help in hospitality?",
    "Give me a practice exercise",
  ];

  function Bubble({ role, content }) {
    const isUser = role === "user";
    return h(
      "div",
      { className: "flex " + (isUser ? "justify-end" : "justify-start") },
      !isUser &&
        h("span", { className: "mr-3 mt-1 flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-primary to-secondary text-white" },
          h("span", { className: "material-symbols-outlined text-base" }, "smart_toy")),
      h("div", {
        className:
          "chat-bubble max-w-[80%] rounded-2xl px-5 py-3.5 text-sm leading-relaxed shadow-card " +
          (isUser ? "rounded-br-md bg-primary-container text-white" : "rounded-bl-md border border-outline-variant/50 bg-white"),
        dangerouslySetInnerHTML: { __html: mdToHtml(content) },
      })
    );
  }

  function Typing() {
    return h(
      "div",
      { className: "flex justify-start" },
      h("span", { className: "mr-3 mt-1 flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-primary to-secondary text-white" },
        h("span", { className: "material-symbols-outlined text-base" }, "smart_toy")),
      h("div", { className: "rounded-2xl rounded-bl-md border border-outline-variant/50 bg-white px-5 py-4 shadow-card" },
        h("span", { className: "flex gap-1.5" },
          [0, 1, 2].map((i) =>
            h("span", {
              key: i,
              className: "h-2 w-2 animate-bounce rounded-full bg-primary/50",
              style: { animationDelay: i * 0.15 + "s" },
            }))))
    );
  }

  function TutorChat() {
    const [messages, setMessages] = useState(initialHistory);
    const [input, setInput] = useState("");
    const [busy, setBusy] = useState(false);
    const scrollRef = useRef(null);

    useEffect(() => {
      if (scrollRef.current) scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }, [messages, busy]);

    const send = async (text) => {
      const message = (text || input).trim();
      if (!message || busy) return;
      setInput("");
      setMessages((m) => [...m, { role: "user", content: message }]);
      setBusy(true);
      try {
        const data = await postJSON("/tutor/api/chat/", { message });
        setMessages((m) => [...m, { role: "assistant", content: data.reply }]);
      } catch (e) {
        setMessages((m) => [...m, { role: "assistant", content: "Sorry — something went wrong (" + e.message + "). Please try again." }]);
      } finally {
        setBusy(false);
      }
    };

    return h(
      "div",
      { className: "flex min-h-0 flex-1 flex-col rounded-3xl border border-outline-variant/50 bg-surface-container-low shadow-card" },
      // Messages
      h("div", { ref: scrollRef, className: "min-h-0 flex-1 space-y-4 overflow-y-auto p-6" },
        messages.length === 0 &&
          h("div", { className: "flex h-full flex-col items-center justify-center text-center" },
            h("span", { className: "material-symbols-outlined text-5xl text-primary/40" }, "waving_hand"),
            h("h2", { className: "mt-3 text-lg font-bold" }, "Hi! I'm your AI Tutor."),
            h("p", { className: "mt-1 max-w-sm text-sm text-on-surface-variant" },
              "Ask me anything about the course — I can explain concepts, review your prompts, and create practice exercises.")),
        messages.map((m, i) => h(Bubble, { key: i, role: m.role, content: m.content })),
        busy && h(Typing)
      ),
      // Suggestions
      messages.length === 0 &&
        h("div", { className: "flex flex-wrap gap-2 px-6 pb-3" },
          SUGGESTIONS.map((s) =>
            h("button", {
              key: s,
              onClick: () => send(s),
              className: "rounded-full border border-outline-variant bg-white px-4 py-2 text-xs font-medium transition hover:border-primary hover:text-primary",
            }, s))),
      // Input
      h("div", { className: "border-t border-outline-variant/40 p-4" },
        h("form", {
          className: "flex items-end gap-3",
          onSubmit: (e) => { e.preventDefault(); send(); },
        },
          h("textarea", {
            value: input,
            rows: 1,
            placeholder: "Ask your AI tutor anything…",
            className: "max-h-32 flex-1 resize-none rounded-xl border border-outline-variant bg-white px-4 py-3 text-sm placeholder:text-outline focus:border-primary focus:ring-4 focus:ring-primary/10 focus:outline-none transition",
            onChange: (e) => setInput(e.target.value),
            onKeyDown: (e) => {
              if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(); }
            },
          }),
          h("button", {
            type: "submit",
            disabled: busy || !input.trim(),
            className: "flex h-11 w-11 items-center justify-center rounded-xl bg-primary-container text-white shadow-card transition hover:-translate-y-px disabled:opacity-40",
          }, h("span", { className: "material-symbols-outlined" }, "send"))))
    );
  }

  ReactDOM.createRoot(root).render(h(TutorChat));
})();

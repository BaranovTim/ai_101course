// Interactive quiz player — React component (no build step, uses React.createElement).
(function () {
  const root = document.getElementById("quiz-root");
  if (!root) return;

  const h = React.createElement;
  const { useState, useEffect } = React;
  const lessonId = root.dataset.lessonId;
  const nextUrl = root.dataset.nextUrl;
  const alreadyCompleted = root.dataset.completed === "1";

  function ProgressDots({ total, current }) {
    return h(
      "div",
      { className: "flex items-center gap-1.5" },
      Array.from({ length: total }, (_, i) =>
        h("span", {
          key: i,
          className:
            "h-1.5 rounded-full transition-all " +
            (i < current ? "w-6 bg-gradient-to-r from-primary to-secondary" : i === current ? "w-6 bg-primary/40" : "w-3 bg-surface-container-high"),
        })
      )
    );
  }

  function Quiz() {
    const [quiz, setQuiz] = useState(null);
    const [error, setError] = useState(null);
    const [idx, setIdx] = useState(0);
    const [answers, setAnswers] = useState({});
    const [result, setResult] = useState(null);
    const [submitting, setSubmitting] = useState(false);
    const [started, setStarted] = useState(false);

    useEffect(() => {
      getJSON(`/api/lessons/${lessonId}/quiz/`).then(setQuiz).catch((e) => setError(e.message));
    }, []);

    if (error)
      return h("div", { className: "rounded-2xl border border-error/30 bg-error/5 p-6 text-sm text-error" }, "Could not load the quiz: " + error);
    if (!quiz)
      return h("div", { className: "rounded-2xl border border-outline-variant/50 bg-white p-8 text-center text-on-surface-variant shadow-card" }, "Loading quiz…");

    const questions = quiz.questions;

    // ---------- Results screen ----------
    if (result) {
      const reviewItems = questions.map((q, i) => {
        const r = result.results.find((x) => x.question_id === q.id) || {};
        const picked = q.choices.find((c) => c.id === r.picked_choice_id);
        const correct = q.choices.find((c) => c.id === r.correct_choice_id);
        return h(
          "div",
          { key: q.id, className: "rounded-xl border p-4 " + (r.is_correct ? "border-success/30 bg-success/5" : "border-error/30 bg-error/5") },
          h("p", { className: "flex items-start gap-2 font-medium" },
            h("span", { className: "material-symbols-outlined text-lg " + (r.is_correct ? "text-success" : "text-error") }, r.is_correct ? "check_circle" : "cancel"),
            `${i + 1}. ${q.text}`
          ),
          !r.is_correct && picked ? h("p", { className: "mt-2 pl-7 text-sm text-error" }, "Your answer: " + picked.text) : null,
          correct ? h("p", { className: "mt-1 pl-7 text-sm font-medium text-success" }, "Correct answer: " + correct.text) : null,
          r.explanation ? h("p", { className: "mt-2 pl-7 text-sm text-on-surface-variant" }, r.explanation) : null
        );
      });

      return h(
        "div",
        { className: "rounded-3xl border border-outline-variant/50 bg-white p-8 shadow-card" },
        h("div", { className: "text-center" },
          h("span", { className: "material-symbols-outlined filled text-6xl " + (result.passed ? "text-success" : "text-warning") }, result.passed ? "celebration" : "replay"),
          h("h2", { className: "mt-3 text-2xl font-extrabold" }, result.passed ? "Quiz passed!" : "Almost there"),
          h("p", { className: "mt-1 text-on-surface-variant" },
            `You scored ${result.score}/${result.total} (${result.percent}%). ` +
            (result.passed ? "This lesson is marked complete." : `You need ${result.pass_percent}% to pass — review and try again.`)
          )
        ),
        h("div", { className: "mt-6 space-y-3" }, reviewItems),
        h("div", { className: "mt-8 flex flex-wrap justify-center gap-3" },
          !result.passed &&
            h("button", {
              className: "rounded-lg bg-primary-container px-6 py-3 font-semibold text-white shadow-card transition hover:-translate-y-px hover:shadow-glow",
              onClick: () => { setResult(null); setAnswers({}); setIdx(0); setStarted(true); },
            }, "Try Again"),
          result.passed && result.certificate_issued &&
            h("a", { href: "/certificates/", className: "rounded-lg bg-secondary-container px-6 py-3 font-semibold text-white shadow-card transition hover:-translate-y-px" }, "🎓 Get Your Certificate"),
          result.passed && !result.certificate_issued &&
            h("a", { href: nextUrl, className: "rounded-lg bg-primary-container px-6 py-3 font-semibold text-white shadow-card transition hover:-translate-y-px hover:shadow-glow" }, "Continue to Next Lesson →")
        )
      );
    }

    // ---------- Intro screen ----------
    if (!started) {
      return h(
        "div",
        { className: "rounded-3xl border border-outline-variant/50 bg-gradient-to-br from-surface-container-low to-surface-container p-8 text-center shadow-card" },
        h("span", { className: "material-symbols-outlined filled text-5xl text-secondary" }, "quiz"),
        h("h2", { className: "mt-3 text-2xl font-extrabold" }, "Knowledge check"),
        h("p", { className: "mt-1 text-on-surface-variant" }, `${questions.length} questions · pass with ${quiz.pass_percent}% to complete this lesson` + (alreadyCompleted ? " (already completed — retake any time)" : "")),
        h("button", {
          className: "mt-6 rounded-lg bg-primary-container px-8 py-3 font-semibold text-white shadow-card transition hover:-translate-y-px hover:shadow-glow",
          onClick: () => setStarted(true),
        }, "Start Quiz")
      );
    }

    // ---------- Question screen ----------
    const q = questions[idx];
    const isLast = idx === questions.length - 1;
    const selected = answers[q.id];

    const submit = async () => {
      setSubmitting(true);
      try {
        const data = await postJSON(`/api/lessons/${lessonId}/quiz/submit/`, { answers });
        setResult(data);
        // Let the proactive AI assistant offer help on wrong answers.
        const wrong = (data.results || [])
          .filter((r) => !r.is_correct)
          .map((r) => {
            const q = questions.find((x) => x.id === r.question_id);
            return { question: (q && q.text) || r.question_text || "", explanation: r.explanation || "" };
          });
        if (wrong.length) {
          setTimeout(() => {
            document.dispatchEvent(new CustomEvent("ai101:quiz-feedback", { detail: { wrong, passed: data.passed } }));
          }, 1200);
        }
      } catch (e) {
        alert("Could not submit the quiz: " + e.message);
      } finally {
        setSubmitting(false);
      }
    };

    return h(
      "div",
      { className: "rounded-3xl border border-outline-variant/50 bg-white p-8 shadow-card" },
      h("div", { className: "flex items-center justify-between" },
        h("p", { className: "font-mono text-xs uppercase tracking-widest text-secondary" }, `Question ${idx + 1} of ${questions.length}`),
        h(ProgressDots, { total: questions.length, current: idx })
      ),
      h("h2", { className: "mt-4 text-xl font-bold leading-snug" }, q.text),
      h("div", { className: "mt-6 space-y-3" },
        q.choices.map((c) =>
          h("button", {
            key: c.id,
            onClick: () => setAnswers({ ...answers, [q.id]: c.id }),
            className:
              "flex w-full items-center gap-3 rounded-xl border px-5 py-4 text-left text-sm font-medium transition " +
              (selected === c.id
                ? "border-primary bg-surface-container-low shadow-card ring-4 ring-primary/10"
                : "border-outline-variant/60 bg-white hover:border-primary/50"),
          },
            h("span", {
              className: "flex h-5 w-5 shrink-0 items-center justify-center rounded-full border-2 " +
                (selected === c.id ? "border-primary" : "border-outline-variant"),
            }, selected === c.id ? h("span", { className: "h-2.5 w-2.5 rounded-full bg-primary" }) : null),
            c.text
          )
        )
      ),
      h("div", { className: "mt-8 flex items-center justify-between" },
        h("button", {
          className: "rounded-lg border border-outline-variant px-5 py-2.5 text-sm font-semibold transition hover:border-primary hover:text-primary disabled:opacity-40",
          disabled: idx === 0,
          onClick: () => setIdx(idx - 1),
        }, "← Back"),
        isLast
          ? h("button", {
              className: "rounded-lg bg-secondary-container px-6 py-2.5 text-sm font-semibold text-white shadow-card transition hover:-translate-y-px disabled:opacity-40",
              disabled: selected == null || submitting,
              onClick: submit,
            }, submitting ? "Checking…" : "Submit Quiz")
          : h("button", {
              className: "rounded-lg bg-primary-container px-6 py-2.5 text-sm font-semibold text-white shadow-card transition hover:-translate-y-px disabled:opacity-40",
              disabled: selected == null,
              onClick: () => setIdx(idx + 1),
            }, "Next →")
      )
    );
  }

  ReactDOM.createRoot(root).render(h(Quiz));
})();

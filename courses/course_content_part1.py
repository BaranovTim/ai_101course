"""AI 101 course content — Modules 1–3.

Each module: {title, subtitle, icon, lessons: [...]}
Each lesson: {title, slug, type, duration, content, exercise (optional),
              quiz (optional): {pass_percent, questions: [(text, [(choice, is_correct), ...], explanation)]}}
"""

MODULES_PART1 = [
    # ------------------------------------------------------------------
    # MODULE 1 — Introduction to Artificial Intelligence
    # ------------------------------------------------------------------
    {
        "title": "Introduction to Artificial Intelligence",
        "subtitle": "What AI actually is, where it came from, and what it can (and can't) do.",
        "icon": "psychology",
        "lessons": [
            {
                "title": "What is Artificial Intelligence?",
                "slug": "what-is-ai",
                "type": "reading",
                "duration": 12,
                "content": """
<p>Artificial Intelligence sounds intimidating, but the core idea is simple: <strong>AI is software that can perform tasks that normally require human intelligence</strong> — understanding language, recognizing patterns, making decisions, and creating content.</p>
<h2>You already use AI every day</h2>
<ul>
<li><strong>Your phone's keyboard</strong> predicting your next word.</li>
<li><strong>Netflix and Spotify</strong> recommending what to watch or listen to next.</li>
<li><strong>Your bank</strong> flagging a suspicious card transaction within seconds.</li>
<li><strong>Google Maps</strong> predicting traffic on the way to George Town.</li>
</ul>
<p>What changed in the last few years is the arrival of <strong>generative AI</strong> — tools like ChatGPT and Claude that don't just sort or recommend things, but <em>create</em>: emails, reports, images, plans, and ideas.</p>
<h2>The key terms, in plain English</h2>
<table>
<tr><th>Term</th><th>What it means</th></tr>
<tr><td>AI</td><td>The broad field: machines doing "smart" tasks.</td></tr>
<tr><td>Machine Learning</td><td>Software that learns patterns from examples instead of following fixed rules.</td></tr>
<tr><td>Large Language Model (LLM)</td><td>An AI trained on enormous amounts of text so it can read and write like a person. ChatGPT and Claude are LLMs.</td></tr>
<tr><td>Generative AI</td><td>AI that produces new content — text, images, audio, video.</td></tr>
<tr><td>Prompt</td><td>The instruction you type to an AI. Writing good prompts is the #1 skill in this course.</td></tr>
</table>
<div class="callout"><p><strong>The big idea:</strong> you don't need to understand the math inside AI to use it brilliantly — just like you don't need to understand engines to drive. This course teaches you to drive.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "What best describes a Large Language Model (LLM) like ChatGPT or Claude?",
                            [
                                ("An AI trained on huge amounts of text so it can understand and produce language", True),
                                ("A robot with a physical body", False),
                                ("A database that stores every fact on the internet", False),
                                ("A spreadsheet program with extra formulas", False),
                            ],
                            "LLMs learn patterns from enormous amounts of text, which lets them read, summarize, and write language — they are not databases or robots.",
                        ),
                        (
                            "What is a 'prompt'?",
                            [
                                ("The instruction or question you give to an AI tool", True),
                                ("The AI's answer to your question", False),
                                ("A paid subscription plan", False),
                                ("An error message", False),
                            ],
                            "The prompt is what YOU type. The quality of your prompt largely determines the quality of the AI's answer.",
                        ),
                        (
                            "Which of these is an example of generative AI?",
                            [
                                ("ChatGPT drafting a welcome email for hotel guests", True),
                                ("A calculator adding two numbers", False),
                                ("A light switch turning on a lamp", False),
                                ("A USB drive storing files", False),
                            ],
                            "Generative AI creates new content — like drafting an email. Calculators and storage devices don't create anything new.",
                        ),
                    ],
                },
            },
            {
                "title": "A Brief History of AI: From Turing to ChatGPT",
                "slug": "history-of-ai",
                "type": "reading",
                "duration": 10,
                "content": """
<p>Knowing a little history helps you understand why AI suddenly seems to be everywhere — and why this moment is different.</p>
<h2>The short version</h2>
<ul>
<li><strong>1950</strong> — Alan Turing asks "Can machines think?" and proposes the famous Turing Test.</li>
<li><strong>1956</strong> — The term "Artificial Intelligence" is coined at the Dartmouth Conference.</li>
<li><strong>1960s–1990s</strong> — Cycles of excitement and disappointment ("AI winters"). Computers could follow rules but couldn't handle the messiness of real language.</li>
<li><strong>1997</strong> — IBM's Deep Blue beats world chess champion Garry Kasparov.</li>
<li><strong>2012</strong> — The deep learning breakthrough: neural networks get dramatically better at recognizing images and speech.</li>
<li><strong>2017</strong> — Google researchers publish the "Transformer" architecture — the T in ChatGPT. It lets AI understand context in language far better than before.</li>
<li><strong>2022</strong> — ChatGPT launches and reaches 100 million users in two months, the fastest-growing consumer product in history.</li>
<li><strong>Today</strong> — ChatGPT, Claude, Gemini, and Copilot are used daily by hundreds of millions of people at work.</li>
</ul>
<h2>Why now?</h2>
<p>Three ingredients finally came together:</p>
<ol>
<li><strong>Data</strong> — the internet provided oceans of text to learn from.</li>
<li><strong>Computing power</strong> — modern chips can train models with billions of parameters.</li>
<li><strong>Better methods</strong> — the Transformer architecture made language finally "click" for machines.</li>
</ol>
<div class="callout"><p><strong>Why it matters to you:</strong> this isn't a passing fad. Like the arrival of email or the smartphone, AI is a permanent shift in how work gets done — and early skills compound.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "What breakthrough architecture (the 'T' in ChatGPT) made modern language AI possible?",
                            [
                                ("The Transformer", True),
                                ("The Terminator", False),
                                ("The Telegraph", False),
                                ("The Turing Machine", False),
                            ],
                            "The Transformer architecture (2017) allowed AI models to understand context in language far better than earlier approaches.",
                        ),
                        (
                            "Which three ingredients came together to make modern AI possible?",
                            [
                                ("Massive data, powerful computers, and better methods", True),
                                ("Robots, lasers, and satellites", False),
                                ("Faster internet, bigger screens, and cheaper phones", False),
                                ("Social media, video games, and streaming", False),
                            ],
                            "Modern AI needed huge amounts of training data, enough computing power to process it, and the Transformer method to tie it together.",
                        ),
                        (
                            "What happened when ChatGPT launched in late 2022?",
                            [
                                ("It became the fastest-growing consumer product in history", True),
                                ("It was shut down within a week", False),
                                ("Only programmers were allowed to use it", False),
                                ("It could only answer math questions", False),
                            ],
                            "ChatGPT reached 100 million users in about two months — faster than any consumer app before it.",
                        ),
                    ],
                },
            },
            {
                "title": "How Language Models Actually Work",
                "slug": "how-llms-work",
                "type": "reading",
                "duration": 15,
                "content": """
<p>You don't need the math — but a good mental model of <em>how</em> ChatGPT and Claude work will instantly make you better at using them.</p>
<h2>The world's most well-read autocomplete</h2>
<p>A language model is trained on a huge portion of the internet — books, articles, websites. From all that text it learns one skill extremely well: <strong>predicting the next word</strong>.</p>
<p>When you ask, "Write a welcome message for guests arriving at a Seven Mile Beach villa," the model isn't looking anything up. It's generating, word by word, the most fitting continuation based on everything it learned.</p>
<h2>What this explains</h2>
<ul>
<li><strong>Why it's so fluent</strong> — it has "read" more text than any human ever could.</li>
<li><strong>Why it sometimes makes things up</strong> — it predicts what <em>sounds</em> right, which is usually (but not always) what <em>is</em> right. These confident errors are called <strong>hallucinations</strong>.</li>
<li><strong>Why context matters</strong> — the more relevant detail you give it, the better its predictions get. Vague prompt in, generic answer out.</li>
<li><strong>Why it can't read your mind</strong> — it only knows what's in the conversation. Details you leave out don't exist for it.</li>
</ul>
<h2>Training in three steps (simplified)</h2>
<ol>
<li><strong>Pre-training</strong> — the model reads vast amounts of text and learns language patterns.</li>
<li><strong>Fine-tuning</strong> — humans rate its answers so it learns to be helpful, honest, and safe.</li>
<li><strong>Your conversation</strong> — the model uses its training plus your prompt to generate a response.</li>
</ol>
<div class="callout"><p><strong>Golden rule:</strong> treat AI like a brilliant, fast, well-read assistant who is occasionally confidently wrong. Always verify names, numbers, dates, and legal or medical claims.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "At its core, what does a language model do?",
                            [
                                ("Predicts the most fitting next word, over and over", True),
                                ("Searches a database of stored answers", False),
                                ("Phones a human expert for each question", False),
                                ("Copies text directly from websites in real time", False),
                            ],
                            "LLMs generate answers word by word based on learned patterns — they are not looking up answers in a database.",
                        ),
                        (
                            "What is an AI 'hallucination'?",
                            [
                                ("When the AI confidently states something that isn't true", True),
                                ("When the AI refuses to answer", False),
                                ("When the AI answers in a different language", False),
                                ("When the AI takes a long time to respond", False),
                            ],
                            "Because models predict what sounds right, they sometimes produce confident but false information — always verify facts.",
                        ),
                        (
                            "Why does giving the AI more context improve its answers?",
                            [
                                ("The model only knows what's in your conversation, so details sharpen its predictions", True),
                                ("It makes the AI work harder out of respect", False),
                                ("Longer prompts unlock a secret premium mode", False),
                                ("It doesn't — short prompts are always better", False),
                            ],
                            "The model can't read your mind. Relevant details in your prompt directly improve the relevance of the response.",
                        ),
                    ],
                },
            },
            {
                "title": "Capabilities and Limitations: What AI Can and Can't Do",
                "slug": "capabilities-limitations",
                "type": "reading",
                "duration": 12,
                "content": """
<p>The fastest way to get value from AI is knowing which jobs to hand it — and which to keep for yourself.</p>
<h2>Where AI shines ✅</h2>
<ul>
<li><strong>Drafting</strong> — emails, reports, proposals, social posts, job descriptions.</li>
<li><strong>Summarizing</strong> — turning a 40-page document into one page of key points.</li>
<li><strong>Transforming</strong> — rewriting a text formally, simply, shorter, or in another language.</li>
<li><strong>Brainstorming</strong> — 20 ideas in 20 seconds, ready for you to pick the best three.</li>
<li><strong>Explaining</strong> — breaking down jargon, contracts, or spreadsheet formulas in plain English.</li>
<li><strong>Structuring</strong> — turning messy notes into agendas, tables, checklists, or plans.</li>
</ul>
<h2>Where to be careful ⚠️</h2>
<ul>
<li><strong>Facts and figures</strong> — it can hallucinate statistics, citations, and names.</li>
<li><strong>Recent events</strong> — models have a training cutoff; without web access they may not know last month's news.</li>
<li><strong>Math on large numbers</strong> — language models predict text; use a calculator or spreadsheet for precise arithmetic.</li>
<li><strong>Confidential data</strong> — never paste client secrets or personal data into tools that aren't approved by your employer.</li>
<li><strong>Final judgment</strong> — AI drafts, you decide. Responsibility for the result stays with the human.</li>
</ul>
<h2>A simple decision rule</h2>
<div class="callout"><p><strong>Use AI when a good draft in 30 seconds beats a perfect blank page in an hour.</strong> Then apply your own expertise to check and polish it. The winning combination is always: AI speed + human judgment.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "Which task is AI best suited for today?",
                            [
                                ("Drafting a first version of an email or report for you to review", True),
                                ("Making final legal decisions without human review", False),
                                ("Guaranteeing perfectly accurate statistics every time", False),
                                ("Reading your mind to know what you want", False),
                            ],
                            "AI is a phenomenal drafter and summarizer, but final judgment and fact-checking stay with you.",
                        ),
                        (
                            "Why should you avoid pasting confidential client information into public AI tools?",
                            [
                                ("The data leaves your control and may violate privacy rules or company policy", True),
                                ("It makes the AI respond more slowly", False),
                                ("The AI will refuse to answer", False),
                                ("Confidential data confuses the model", False),
                            ],
                            "Treat public AI tools like a public place: never share information you wouldn't be comfortable leaving your organization.",
                        ),
                        (
                            "What is the 'winning combination' this lesson recommends?",
                            [
                                ("AI speed plus human judgment", True),
                                ("AI speed plus zero review", False),
                                ("Human speed plus AI judgment", False),
                                ("Avoiding AI entirely", False),
                            ],
                            "Let AI produce fast drafts, then apply your expertise to verify and polish. Neither works as well alone.",
                        ),
                    ],
                },
            },
        ],
    },
    # ------------------------------------------------------------------
    # MODULE 2 — Working with ChatGPT
    # ------------------------------------------------------------------
    {
        "title": "Working with ChatGPT",
        "subtitle": "Master the art of the prompt — the single highest-leverage AI skill.",
        "icon": "forum",
        "lessons": [
            {
                "title": "Your First Real Conversation with ChatGPT",
                "slug": "first-conversation",
                "type": "exercise",
                "duration": 15,
                "content": """
<p>Time to get hands-on. If you haven't already, open <strong>chatgpt.com</strong> (or <strong>claude.ai</strong>) in another tab and create a free account.</p>
<h2>The conversation mindset</h2>
<p>The biggest beginner mistake is treating AI like a search engine: typing two keywords and accepting whatever comes back. Instead, treat it like a <strong>capable new colleague</strong>:</p>
<ul>
<li>Give it a proper briefing, not keywords.</li>
<li>If the first draft isn't right, <strong>reply and redirect</strong> — "shorter", "warmer", "make it a bulleted list".</li>
<li>Ask follow-up questions. The chat remembers the whole conversation.</li>
</ul>
<h2>Compare these two prompts</h2>
<div class="prompt-box">❌ "email about meeting"</div>
<div class="prompt-box">✅ "Write a short, friendly email to my team letting them know Thursday's staff meeting moves to 3pm because of the visiting auditors. Ask everyone to confirm. Sign it 'Maria'."</div>
<p>Same tool, wildly different results. The second prompt gives the AI a <strong>role to play, facts to use, and a clear output</strong>.</p>
<h2>Keep the conversation going</h2>
<p>After the first draft, try refinements like:</p>
<ul>
<li>"Make it 50% shorter."</li>
<li>"More formal — this is going to the board."</li>
<li>"Give me three different subject lines."</li>
<li>"Now translate it into Spanish."</li>
</ul>
""",
                "exercise": """
<p><strong>Your assignment:</strong> open ChatGPT or Claude and have a real working conversation:</p>
<ol>
<li>Ask it to draft a short email you actually need to send this week.</li>
<li>Reply with at least two refinements ("shorter", "friendlier", "add a deadline").</li>
<li>Ask it for three alternative subject lines.</li>
</ol>
<p>Notice how each refinement improves the result — that back-and-forth <em>is</em> the skill.</p>
""",
            },
            {
                "title": "The Anatomy of a Great Prompt",
                "slug": "anatomy-great-prompt",
                "type": "reading",
                "duration": 15,
                "content": """
<p>Great prompts aren't magic — they follow a pattern. Use the <strong>R-T-C-F formula</strong>: Role, Task, Context, Format.</p>
<h2>The four building blocks</h2>
<table>
<tr><th>Block</th><th>What it does</th><th>Example</th></tr>
<tr><td><strong>R — Role</strong></td><td>Tells the AI who to be</td><td>"You are an experienced Caribbean hotel concierge…"</td></tr>
<tr><td><strong>T — Task</strong></td><td>Says exactly what you want</td><td>"…write a reply to this 3-star guest review…"</td></tr>
<tr><td><strong>C — Context</strong></td><td>Gives the facts it needs</td><td>"…the guest loved the beach but complained about slow check-in. We've since added express check-in."</td></tr>
<tr><td><strong>F — Format</strong></td><td>Shapes the output</td><td>"…under 120 words, warm but professional, no emojis."</td></tr>
</table>
<h2>Put together</h2>
<div class="prompt-box">You are an experienced Caribbean hotel concierge with a warm, professional tone.

Write a public reply to this 3-star review: "Beautiful beach and friendly staff, but check-in took 45 minutes."

Context: we recently introduced express online check-in, and we want the guest to come back.

Format: under 120 words, no emojis, end by inviting them to return.</div>
<div class="callout"><p><strong>You don't need all four every time.</strong> For quick tasks, Task + Context is enough. But when output quality matters, run through R-T-C-F — it takes 30 extra seconds and transforms the result.</p></div>
<h2>One more power move: examples</h2>
<p>If you want a specific style, <strong>show, don't tell</strong>. Paste an example: "Here's an email I wrote that has the tone I like: … Now write a new one about X in the same style."</p>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "What does the R-T-C-F formula stand for?",
                            [
                                ("Role, Task, Context, Format", True),
                                ("Read, Think, Copy, Finish", False),
                                ("Request, Time, Cost, Feedback", False),
                                ("Role, Topic, Creativity, Fun", False),
                            ],
                            "Role, Task, Context, Format — the four building blocks of a strong prompt.",
                        ),
                        (
                            "Which prompt is likely to produce the best result?",
                            [
                                ("\"You are a hotel manager. Write a 100-word apology reply to this review: [review]. Warm tone, invite them back.\"", True),
                                ("\"review reply\"", False),
                                ("\"Write something about hotels\"", False),
                                ("\"Help\"", False),
                            ],
                            "It includes a role, a clear task, context, and format constraints — the R-T-C-F pattern in action.",
                        ),
                        (
                            "If you want the AI to match a specific writing style, what's the best technique?",
                            [
                                ("Paste an example of the style and ask it to match", True),
                                ("Type in all capital letters", False),
                                ("Ask the same question repeatedly", False),
                                ("Use as few words as possible", False),
                            ],
                            "Showing an example ('few-shot prompting') is far more effective than describing a style in the abstract.",
                        ),
                    ],
                },
            },
            {
                "title": "Prompt Engineering Fundamentals",
                "slug": "prompt-engineering-fundamentals",
                "type": "reading",
                "duration": 18,
                "content": """
<p>"Prompt engineering" is just a fancy name for <strong>communicating clearly with AI</strong>. Here are the six techniques professionals use daily.</p>
<h2>1. Be specific about the output</h2>
<p>Numbers work wonders: "5 bullet points", "under 150 words", "a table with 3 columns".</p>
<h2>2. Give it a role</h2>
<div class="prompt-box">Act as a skeptical CFO reviewing this proposal. What questions would you ask?</div>
<p>Roles unlock different knowledge and tone — teacher, lawyer, customer, editor, coach.</p>
<h2>3. Think step by step</h2>
<p>For anything with logic or numbers, add: <strong>"Think through this step by step before giving your final answer."</strong> Reasoning improves noticeably.</p>
<h2>4. Constrain and structure</h2>
<div class="prompt-box">Summarize this contract in exactly this structure:
1. Parties involved
2. Key obligations (bullets)
3. Payment terms
4. Red flags I should ask a lawyer about</div>
<h2>5. Iterate — don't restart</h2>
<p>The first answer is a first draft. Reply with corrections: "Good, but point 2 is wrong — we don't offer refunds. Rewrite." The conversation is the tool.</p>
<h2>6. Ask the AI to ask YOU questions</h2>
<div class="prompt-box">I need a marketing plan for my dive shop. Before you write anything, ask me the 5 most important questions you need answered to do this well.</div>
<p>This flips the script and fixes the "I don't know what to tell it" problem.</p>
<div class="callout"><p><strong>Remember:</strong> vague in, vague out. Every technique above is a way of being less vague.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "What phrase noticeably improves AI answers on logic-heavy questions?",
                            [
                                ("\"Think through this step by step\"", True),
                                ("\"Answer as fast as possible\"", False),
                                ("\"Guess if you're not sure\"", False),
                                ("\"Skip the details\"", False),
                            ],
                            "Asking the model to reason step by step before answering measurably improves accuracy on multi-step problems.",
                        ),
                        (
                            "The AI's first answer isn't quite right. What should you do?",
                            [
                                ("Reply with specific corrections and ask it to revise", True),
                                ("Close the chat and give up", False),
                                ("Send the exact same prompt again unchanged", False),
                                ("Accept it — first answers can't be changed", False),
                            ],
                            "Iterating in the same conversation is the core workflow: correct, refine, and improve the draft.",
                        ),
                        (
                            "You're not sure what information the AI needs for a complex task. What's a smart technique?",
                            [
                                ("Ask the AI to ask you the key questions first", True),
                                ("Provide no context and hope for the best", False),
                                ("Type the request in another language", False),
                                ("Break your keyboard", False),
                            ],
                            "Asking the AI to interview you first ensures it gets the context it needs — a favorite technique of power users.",
                        ),
                    ],
                },
            },
            {
                "title": "Improving AI Responses: The Iteration Playbook",
                "slug": "iteration-playbook",
                "type": "exercise",
                "duration": 15,
                "content": """
<p>Even with a great prompt, the first response is rarely the final one. Professionals treat AI output as <strong>clay to shape</strong>, not stone to accept.</p>
<h2>The five most useful follow-ups</h2>
<table>
<tr><th>When the answer is…</th><th>Say…</th></tr>
<tr><td>Too long / rambling</td><td>"Cut this by half. Keep the key points only."</td></tr>
<tr><td>Too generic</td><td>"Make this specific to a small dive shop in Grand Cayman with 6 staff."</td></tr>
<tr><td>Wrong tone</td><td>"Rewrite warmer / more formal / more confident."</td></tr>
<tr><td>Wrong on facts</td><td>"Point 3 is incorrect — actually [correct fact]. Revise."</td></tr>
<tr><td>Almost right</td><td>"Keep everything, but change the opening line and add a deadline of Friday."</td></tr>
</table>
<h2>Quality-check questions</h2>
<p>Before using any AI output, run this 20-second checklist:</p>
<ol>
<li><strong>Facts</strong> — are the names, numbers, and claims correct?</li>
<li><strong>Voice</strong> — does it sound like you (or your business)?</li>
<li><strong>Audience</strong> — is it right for who's receiving it?</li>
<li><strong>Completeness</strong> — did it miss anything you asked for?</li>
</ol>
<h2>Ask for self-critique</h2>
<div class="prompt-box">Review your own answer above. What are its 3 biggest weaknesses? Now rewrite it fixing them.</div>
<p>It sounds odd, but models are genuinely good at improving their own work when asked.</p>
""",
                "exercise": """
<p><strong>Your assignment:</strong> take any AI draft (an email, a product description, a plan) and improve it through exactly three rounds of iteration:</p>
<ol>
<li>Round 1 — fix the length ("half as long").</li>
<li>Round 2 — fix the tone ("warmer" or "more formal").</li>
<li>Round 3 — ask for self-critique and a final rewrite.</li>
</ol>
<p>Compare the final version with the first. This before/after is the value of iteration.</p>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "The AI's draft is factually wrong about your business. What's the best response?",
                            [
                                ("Tell it the correct fact and ask it to revise", True),
                                ("Publish it anyway", False),
                                ("Start a brand-new chat and never mention it", False),
                                ("Report the AI to the police", False),
                            ],
                            "Corrections work: state the right fact and ask for a revision. The model will incorporate it immediately.",
                        ),
                        (
                            "What is the 'self-critique' technique?",
                            [
                                ("Asking the AI to find weaknesses in its own answer and rewrite it", True),
                                ("Criticizing yourself for using AI", False),
                                ("Deleting the conversation", False),
                                ("Asking a colleague to grade your prompt", False),
                            ],
                            "Models are surprisingly good at improving their own output when explicitly asked to critique and rewrite it.",
                        ),
                        (
                            "Which is part of the 20-second quality checklist before using AI output?",
                            [
                                ("Verify names, numbers, and claims are correct", True),
                                ("Count the number of vowels", False),
                                ("Check that it was generated quickly", False),
                                ("Make sure it's at least 5 pages long", False),
                            ],
                            "Facts, voice, audience, completeness — the four quick checks before any AI draft goes out the door.",
                        ),
                    ],
                },
            },
        ],
    },
    # ------------------------------------------------------------------
    # MODULE 3 — Practical AI Applications
    # ------------------------------------------------------------------
    {
        "title": "Practical AI Applications",
        "subtitle": "Emails, documents, ideas, analysis — your daily productivity toolkit.",
        "icon": "work",
        "lessons": [
            {
                "title": "Writing Emails and Documents with AI",
                "slug": "emails-documents",
                "type": "exercise",
                "duration": 15,
                "content": """
<p>Writing is where AI pays for itself first. Most professionals save <strong>3–5 hours a week</strong> on drafting alone.</p>
<h2>The universal email prompt</h2>
<div class="prompt-box">Write a [tone] email to [who] about [what].
Key points to include:
- [point 1]
- [point 2]
Keep it under [N] words. Sign it [name].</div>
<p>Fill in the brackets and you'll get a solid draft in seconds — for scheduling, follow-ups, apologies, introductions, reminders, thank-yous.</p>
<h2>Harder email situations</h2>
<ul>
<li><strong>Saying no nicely:</strong> "Write a polite decline to this vendor proposal. Keep the relationship warm — we may work together next year."</li>
<li><strong>Chasing payment:</strong> "Firm but courteous third reminder for invoice #204, now 30 days overdue. Mention late fees apply after 45 days."</li>
<li><strong>De-escalating:</strong> "The customer below is angry. Draft a calm, non-defensive reply that acknowledges the problem and offers two solutions."</li>
</ul>
<h2>Longer documents</h2>
<p>For reports and proposals, work in two steps:</p>
<ol>
<li><strong>Outline first:</strong> "Create an outline for a 2-page proposal to add Sunday brunch service, aimed at the restaurant owner."</li>
<li><strong>Then expand:</strong> "Write section 2 in full. Budget: CI$8,000. Expected extra revenue: CI$3,500/month."</li>
</ol>
<div class="callout"><p><strong>Pro tip:</strong> always give AI the raw material — the email you're replying to, the numbers, the previous version. The more real substance it has, the less it invents.</p></div>
""",
                "exercise": """
<p><strong>Your assignment:</strong> use the universal email prompt to draft three real emails from your work or life:</p>
<ol>
<li>A scheduling or reminder email.</li>
<li>A polite "no" to a request.</li>
<li>A follow-up chasing something overdue.</li>
</ol>
<p>Then pick the best one, iterate twice, and actually send it. Real usage beats theory.</p>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "What's the recommended two-step approach for longer documents?",
                            [
                                ("Ask for an outline first, then expand sections with real facts", True),
                                ("Ask for the whole document with no context", False),
                                ("Write it yourself, then delete it", False),
                                ("Generate 50 versions and pick one at random", False),
                            ],
                            "Outline first, then expand — you steer the structure and feed in real numbers before full drafting.",
                        ),
                        (
                            "Why should you paste the email you're replying to into your prompt?",
                            [
                                ("Real substance lets the AI respond accurately instead of inventing details", True),
                                ("It makes the AI feel appreciated", False),
                                ("Longer prompts are always better", False),
                                ("You shouldn't — AI must never see other emails", False),
                            ],
                            "AI works dramatically better with the actual raw material in front of it — context prevents invention.",
                        ),
                        (
                            "Which is a realistic time saving from using AI for drafting?",
                            [
                                ("Several hours per week on routine writing", True),
                                ("It eliminates all work forever", False),
                                ("No time saving at all is possible", False),
                                ("Exactly 45 seconds per year", False),
                            ],
                            "Most professionals report saving 3–5 hours a week on drafting emails and documents alone.",
                        ),
                    ],
                },
            },
            {
                "title": "Generating and Organizing Ideas",
                "slug": "generating-ideas",
                "type": "reading",
                "duration": 12,
                "content": """
<p>AI is a tireless brainstorming partner: it never runs dry, never judges, and never gets tired of "give me ten more."</p>
<h2>Volume first, quality second</h2>
<div class="prompt-box">Give me 20 promotion ideas for a beachfront café during the slow season (September–November). Mix cheap/easy ideas with bigger bets. Format: numbered list, one line each.</div>
<p>You're not looking for 20 winners — you're looking for <strong>3 sparks</strong> among 20 options. Then go deeper:</p>
<div class="prompt-box">Expand ideas #4, #11, and #17. For each: who it targets, rough cost, first step to launch this week.</div>
<h2>Useful brainstorming angles</h2>
<ul>
<li><strong>Inversion:</strong> "What would make customers LEAVE us? Now reverse each into an improvement."</li>
<li><strong>Personas:</strong> "How would a luxury brand approach this? A budget brand? A tech startup?"</li>
<li><strong>Constraints:</strong> "Ideas that cost under $100 and can start tomorrow."</li>
<li><strong>Combination:</strong> "Combine the best parts of ideas 2 and 7 into one plan."</li>
</ul>
<h2>From ideas to organization</h2>
<p>AI is equally good at <em>structuring</em> what you already have. Paste messy notes and ask:</p>
<div class="prompt-box">Organize these meeting notes into: 1) Decisions made, 2) Action items with owners, 3) Open questions. Flag anything with a deadline.</div>
<div class="callout"><p><strong>Mindset shift:</strong> stop asking "what's the answer?" and start asking "give me options." Options are where AI is superhuman; choosing is where you are.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "What's the recommended brainstorming approach with AI?",
                            [
                                ("Ask for many options, then pick a few and go deeper", True),
                                ("Ask for one perfect idea and accept it", False),
                                ("Never ask for more than two ideas", False),
                                ("Only brainstorm on Mondays", False),
                            ],
                            "Volume first: 20 quick options usually contain 3 sparks worth expanding. Choosing is your job.",
                        ),
                        (
                            "What is the 'inversion' technique?",
                            [
                                ("Ask what would make things worse, then reverse each into an improvement", True),
                                ("Typing your prompt backwards", False),
                                ("Asking the AI to disagree with everything", False),
                                ("Turning your monitor upside down", False),
                            ],
                            "Inversion ('what would drive customers away?') surfaces risks and weaknesses you can flip into improvements.",
                        ),
                        (
                            "Besides generating ideas, what organizing task is AI great at?",
                            [
                                ("Turning messy notes into decisions, action items, and open questions", True),
                                ("Physically filing paper documents", False),
                                ("Cleaning your desk", False),
                                ("Scheduling staff without being asked", False),
                            ],
                            "Paste messy notes and ask for structure — decisions, actions with owners, deadlines. Instant clarity.",
                        ),
                    ],
                },
            },
            {
                "title": "Summarizing and Analyzing Information",
                "slug": "summarizing-analyzing",
                "type": "exercise",
                "duration": 15,
                "content": """
<p>Reading is the hidden time sink of office work. AI can compress a 40-page report into one page — and then answer questions about it.</p>
<h2>The layered summary</h2>
<div class="prompt-box">Summarize the document below in three layers:
1. One sentence — the core message
2. One paragraph — the key points
3. One page — full summary with all important details and numbers

[paste document]</div>
<p>You read layer 1, decide if you need layer 2, and only dive into layer 3 when it matters.</p>
<h2>Summaries with a purpose</h2>
<p>Generic summaries waste the tool. Tell it <strong>why</strong> you're reading:</p>
<ul>
<li>"Summarize this focusing on <strong>anything that affects our costs</strong>."</li>
<li>"Summarize this contract from the perspective of <strong>the tenant's risks</strong>."</li>
<li>"What in this report would a <strong>board member</strong> ask about?"</li>
</ul>
<h2>Interrogate the document</h2>
<p>After pasting a document, keep asking:</p>
<ul>
<li>"What's missing or unclear here?"</li>
<li>"List every date and deadline mentioned."</li>
<li>"Does anything contradict itself?"</li>
<li>"Explain section 4 like I'm not a lawyer."</li>
</ul>
<h2>Comparing options</h2>
<div class="prompt-box">Here are two supplier quotes. Build a comparison table: price, delivery time, warranty, hidden costs, risks. Then recommend one and justify it.</div>
<div class="callout"><p><strong>Caution:</strong> summaries can occasionally drop something important. For high-stakes documents (contracts, regulations), use AI summaries to <em>orient</em> yourself — then verify the critical sections yourself.</p></div>
""",
                "exercise": """
<p><strong>Your assignment:</strong> find a long article, policy, or report from your work or interests. Then:</p>
<ol>
<li>Get a three-layer summary.</li>
<li>Ask two purposeful follow-ups (e.g. "list every deadline", "what's missing?").</li>
<li>Ask it to explain the hardest paragraph "like I'm 12".</li>
</ol>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "What is the 'layered summary' technique?",
                            [
                                ("Asking for one sentence, one paragraph, and one page versions together", True),
                                ("Summarizing the same text 100 times", False),
                                ("Only ever reading titles", False),
                                ("Printing documents in layers", False),
                            ],
                            "Three layers let you read only as deep as you actually need — sentence, paragraph, page.",
                        ),
                        (
                            "How do you make a summary more useful than a generic one?",
                            [
                                ("Tell the AI why you're reading — the perspective or focus that matters to you", True),
                                ("Ask it to use bigger words", False),
                                ("Request it in all caps", False),
                                ("Keep your purpose secret", False),
                            ],
                            "Purpose-driven summaries ('focus on costs', 'from the tenant's perspective') surface what actually matters to you.",
                        ),
                        (
                            "For a high-stakes contract, what's the right way to use AI?",
                            [
                                ("Use its summary to orient yourself, then personally verify the critical sections", True),
                                ("Sign whatever the AI says is fine", False),
                                ("Never let AI see any document ever", False),
                                ("Ask it to sign on your behalf", False),
                            ],
                            "AI summaries orient you quickly, but for contracts and regulations the critical sections deserve human verification.",
                        ),
                    ],
                },
            },
            {
                "title": "Your Daily AI Productivity Workflow",
                "slug": "daily-workflow",
                "type": "reading",
                "duration": 12,
                "content": """
<p>Individual tricks are nice; a <strong>system</strong> is transformative. Here's how to weave AI into an ordinary workday.</p>
<h2>A day with AI</h2>
<table>
<tr><th>Moment</th><th>AI move</th></tr>
<tr><td><strong>Morning planning</strong></td><td>"Here's my task list and calendar. Suggest a realistic priority order; flag conflicts and anything that can be delegated or dropped."</td></tr>
<tr><td><strong>Email triage</strong></td><td>Paste the long ones: "Summarize and draft a reply in my usual tone."</td></tr>
<tr><td><strong>Before meetings</strong></td><td>"Create a 30-minute agenda for a check-in about [topic] with these attendees. Include two questions to ask each person."</td></tr>
<tr><td><strong>After meetings</strong></td><td>Paste notes: "Extract decisions, action items with owners, and open questions."</td></tr>
<tr><td><strong>Writing blocks</strong></td><td>Outline → expand → iterate (Module 3, Lesson 1).</td></tr>
<tr><td><strong>End of day</strong></td><td>"Here's what I did today. Draft a brief status update for my manager and tomorrow's top-3 list."</td></tr>
</table>
<h2>Build your prompt library</h2>
<p>The real accelerator: whenever a prompt works well, <strong>save it</strong> in a notes app. After a month you'll have a personal toolkit of 15–20 proven prompts you reuse with tiny edits.</p>
<h2>Start small, stay consistent</h2>
<ol>
<li>Pick <strong>two</strong> moments from the table above.</li>
<li>Do them with AI every workday for two weeks.</li>
<li>Add a third only when the first two are habits.</li>
</ol>
<div class="callout"><p><strong>The compounding effect:</strong> 30 minutes saved daily is over three working weeks per year — from just the basics.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "What's the recommended way to build lasting AI habits?",
                            [
                                ("Start with two daily use-cases and add more once they stick", True),
                                ("Change your entire workflow overnight", False),
                                ("Use AI for everything on day one, then quit", False),
                                ("Wait until everyone else uses it first", False),
                            ],
                            "Small and consistent wins: two habitual use-cases beat ten abandoned ones.",
                        ),
                        (
                            "What is a 'prompt library'?",
                            [
                                ("Your saved collection of prompts that worked well, ready to reuse", True),
                                ("A physical building full of prompts", False),
                                ("A paid feature you must subscribe to", False),
                                ("The AI's internal training data", False),
                            ],
                            "Saving winning prompts in a notes app builds a personal toolkit that compounds over time.",
                        ),
                        (
                            "Roughly how much working time does 30 minutes saved per day add up to in a year?",
                            [
                                ("More than three working weeks", True),
                                ("About one hour", False),
                                ("Two days", False),
                                ("It doesn't add up to anything", False),
                            ],
                            "30 minutes × ~250 working days ≈ 125 hours — over three working weeks per year.",
                        ),
                    ],
                },
            },
        ],
    },
]

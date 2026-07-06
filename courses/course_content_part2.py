"""AI 101 course content — Modules 4–5."""

MODULES_PART2 = [
    # ------------------------------------------------------------------
    # MODULE 4 — AI in Different Industries
    # ------------------------------------------------------------------
    {
        "title": "AI in Different Industries",
        "subtitle": "Real workflows for hospitality, banking, accounting, marketing, and more.",
        "icon": "domain",
        "lessons": [
            {
                "title": "AI in Hospitality & Tourism",
                "slug": "ai-hospitality",
                "type": "reading",
                "duration": 15,
                "content": """
<p>Tourism is Cayman's heartbeat — and hospitality is packed with communication tasks AI handles brilliantly.</p>
<h2>Five high-impact workflows</h2>
<h3>1. Review responses</h3>
<div class="prompt-box">You are the guest relations manager of a beachfront resort. Reply publicly to this review: [paste review]. Acknowledge specifics, stay warm and professional, invite them back. Under 100 words.</div>
<p>Respond to every review, in minutes, in a consistent voice.</p>
<h3>2. Multilingual guest communication</h3>
<p>"Translate this welcome letter into Spanish, German, and Portuguese — keep the warm tone." Instant international service.</p>
<h3>3. Menus, promos, and social posts</h3>
<div class="prompt-box">Write 5 Instagram captions for our new sunset happy hour on Seven Mile Beach. Fun, beachy tone, each under 25 words, include a call to action.</div>
<h3>4. Guest FAQs and SOPs</h3>
<p>Paste your existing info sheets: "Turn this into a clear FAQ page" or "Write a step-by-step checklist for housekeeping turnover of a 2-bedroom condo."</p>
<h3>5. Demand and staffing notes</h3>
<p>"Here are our covers per night for the last 4 weeks. Summarize the pattern and suggest a staffing plan for next week, including the cruise-ship day spike."</p>
<div class="callout"><p><strong>Guest privacy:</strong> never paste passport numbers, card details, or personal guest data into public AI tools. Use placeholders like [GUEST NAME].</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "What's a smart way to handle online review responses with AI?",
                            [
                                ("Give it a role and the review, ask for a warm reply that acknowledges specifics", True),
                                ("Post the same generic reply to every review", False),
                                ("Only reply to 5-star reviews", False),
                                ("Argue with negative reviewers", False),
                            ],
                            "A role + the actual review + tone and length constraints produces personal, consistent replies in minutes.",
                        ),
                        (
                            "What should you NEVER paste into a public AI tool?",
                            [
                                ("Guest passport numbers and card details", True),
                                ("Your dinner menu", False),
                                ("A public review from TripAdvisor", False),
                                ("Your happy hour schedule", False),
                            ],
                            "Personal and payment data stays out of public tools — use placeholders like [GUEST NAME] instead.",
                        ),
                        (
                            "How can AI help with international guests?",
                            [
                                ("Natural-sounding translation of letters and messages while keeping tone", True),
                                ("It can't — AI only speaks English", False),
                                ("By booking their flights automatically", False),
                                ("By replacing all human staff", False),
                            ],
                            "Modern AI translates fluently while preserving tone — instant multilingual guest service.",
                        ),
                    ],
                },
            },
            {
                "title": "AI in Banking & Financial Services",
                "slug": "ai-banking",
                "type": "reading",
                "duration": 15,
                "content": """
<p>Cayman is one of the world's great financial centres — and financial work is reading- and writing-heavy, which is exactly where AI excels.</p>
<h2>Where AI helps daily</h2>
<h3>1. Plain-English summaries of dense material</h3>
<div class="prompt-box">Summarize this regulatory circular for a client-facing team: what changed, who is affected, what we must do differently, and by when. One page maximum.</div>
<h3>2. Client communication</h3>
<p>Draft onboarding emails, meeting recaps, and explanations of products or fees: "Explain what a fixed-term deposit is to a first-time saver — friendly, 100 words, no jargon."</p>
<h3>3. Meeting and call notes</h3>
<p>"Turn these call notes into a file memo: client request, advice given, next steps, follow-up date."</p>
<h3>4. Internal drafting</h3>
<p>Policy first drafts, procedure checklists, training materials, job descriptions — outline, expand, iterate.</p>
<h3>5. Spreadsheet help</h3>
<div class="prompt-box">Write an Excel formula: flag any row where column D (transaction amount) is more than 3x the average of column D. Explain the formula in one line.</div>
<h2>The compliance mindset</h2>
<ul>
<li><strong>Client confidentiality is absolute.</strong> No names, account numbers, or identifying details in public tools — ever. Anonymize first.</li>
<li><strong>Check your firm's AI policy</strong> before using any tool for work. Many institutions provide approved, private AI deployments.</li>
<li><strong>AI drafts, compliance approves.</strong> Anything client-facing or regulatory goes through normal review.</li>
</ul>
<div class="callout"><p><strong>Rule of thumb:</strong> use AI for the <em>form</em> of the work (drafting, structuring, summarizing) — keep humans responsible for the <em>substance</em> (advice, decisions, approvals).</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "How should banking staff treat client data with public AI tools?",
                            [
                                ("Never include it — anonymize everything first and follow the firm's AI policy", True),
                                ("Paste it freely, AI tools are always private", False),
                                ("Only paste account numbers, never names", False),
                                ("Share it if the client is friendly", False),
                            ],
                            "Client confidentiality is absolute: anonymize, follow policy, and prefer firm-approved AI deployments.",
                        ),
                        (
                            "What's the recommended division of labour in financial work?",
                            [
                                ("AI handles the form (drafts, summaries); humans own the substance (advice, approvals)", True),
                                ("AI makes the decisions; humans do the typing", False),
                                ("AI signs off on compliance", False),
                                ("Humans stop reviewing anything", False),
                            ],
                            "AI accelerates drafting and structuring; advice, decisions, and approvals remain human responsibilities.",
                        ),
                        (
                            "Which spreadsheet task can AI help with?",
                            [
                                ("Writing and explaining an Excel formula from a plain-English description", True),
                                ("Physically printing the spreadsheet", False),
                                ("Guaranteeing the numbers are audit-proof", False),
                                ("Replacing the finance team entirely", False),
                            ],
                            "Describe what you need in plain English and AI writes the formula — and explains how it works.",
                        ),
                    ],
                },
            },
            {
                "title": "AI in Accounting & Audit",
                "slug": "ai-accounting",
                "type": "reading",
                "duration": 15,
                "content": """
<p>Accountants and auditors live in documents, standards, and spreadsheets — three things AI navigates exceptionally well.</p>
<h2>Practical workflows</h2>
<h3>1. Standards in plain English</h3>
<div class="prompt-box">Explain the key requirements of IFRS 16 (leases) to a junior accountant, with a simple example of a 3-year office lease. Then list the 5 most common implementation mistakes.</div>
<h3>2. Client communication</h3>
<p>"Draft an email requesting the outstanding PBC items below — professional, friendly, with a deadline of next Friday: [list]."</p>
<h3>3. Engagement and proposal drafting</h3>
<p>Outline → expand → partner review. AI produces the skeleton and boilerplate; you insert judgment, scope, and fees.</p>
<h3>4. Excel acceleration</h3>
<ul>
<li>"Write a formula to..." (lookups, conditionals, date math, text cleanup)</li>
<li>"Explain what this formula does: [paste]"</li>
<li>"Why might this VLOOKUP return #N/A?"</li>
</ul>
<h3>5. Documentation and workpapers</h3>
<p>"Rewrite these testing notes into a clear workpaper narrative: purpose, procedure performed, results, conclusion."</p>
<h2>The professional boundaries</h2>
<ul>
<li><strong>Client data:</strong> anonymized or approved tools only.</li>
<li><strong>Technical accuracy:</strong> AI can misstate standards — verify against the actual pronouncement before relying on it.</li>
<li><strong>Professional judgment:</strong> materiality, risk assessment, and opinions are yours, not the machine's.</li>
</ul>
<div class="callout"><p><strong>Think of AI as a very fast junior:</strong> excellent first drafts, needs review, never signs the opinion.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "How should you treat AI explanations of accounting standards?",
                            [
                                ("Useful orientation — but verify against the actual standard before relying on it", True),
                                ("Always 100% accurate, no checking needed", False),
                                ("Completely useless", False),
                                ("Legally binding", False),
                            ],
                            "AI is great for orientation and teaching, but technical positions must be verified against the pronouncement itself.",
                        ),
                        (
                            "Which analogy fits AI in an accounting firm?",
                            [
                                ("A very fast junior: great drafts, needs review, never signs the opinion", True),
                                ("A partner who makes final decisions", False),
                                ("A client who pays the bills", False),
                                ("A regulator who inspects the firm", False),
                            ],
                            "AI accelerates drafting like a talented junior — review and professional judgment stay with qualified humans.",
                        ),
                        (
                            "Which Excel task is a good fit for AI?",
                            [
                                ("Explaining why a VLOOKUP returns #N/A", True),
                                ("Physically installing Excel", False),
                                ("Approving the financial statements", False),
                                ("Negotiating the audit fee", False),
                            ],
                            "Formula writing, explanation, and debugging are everyday AI wins for accountants.",
                        ),
                    ],
                },
            },
            {
                "title": "AI in Marketing, Sales & Small Business",
                "slug": "ai-marketing-sales",
                "type": "reading",
                "duration": 15,
                "content": """
<p>If you run or market a small business, AI is like hiring a copywriter, analyst, and assistant for the price of a lunch.</p>
<h2>Marketing workflows</h2>
<h3>Content calendar in one prompt</h3>
<div class="prompt-box">Create a 2-week social media calendar for a Grand Cayman dive shop. Mix: educational posts, customer spotlights, promos, and fun facts. For each: platform, caption, best time to post, and an image idea.</div>
<h3>Ad copy variations</h3>
<p>"Write 5 versions of a Facebook ad for our summer special — different angles: price, experience, safety, family, adventure." Test them, keep the winner.</p>
<h3>Customer research</h3>
<p>"Here are 30 customer feedback comments. What are the top 5 themes? Quote examples of each. What's the #1 fixable complaint?"</p>
<h2>Sales workflows</h2>
<ul>
<li><strong>Outreach:</strong> "Write a short intro email to hotel concierges about our sunset cruise partnership program."</li>
<li><strong>Follow-up sequences:</strong> "Draft 3 follow-ups: day 3 gentle, day 10 value-add, day 21 last call."</li>
<li><strong>Objection prep:</strong> "List the 10 most likely objections to this offer and a one-line response to each."</li>
<li><strong>Proposals:</strong> outline → expand → personalize.</li>
</ul>
<h2>Small-business admin</h2>
<p>Job ads, staff rotas, policy documents, price-increase letters, supplier negotiations prep — the "I've been putting this off" pile is exactly what AI clears fastest.</p>
<div class="callout"><p><strong>Brand voice tip:</strong> paste two examples of your best past posts and say "match this voice." Instant consistency, even across staff.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "How do you keep AI content consistent with your brand voice?",
                            [
                                ("Paste examples of your best past content and ask it to match the voice", True),
                                ("Hope the AI guesses correctly", False),
                                ("Use a different tool every day", False),
                                ("Write everything in capital letters", False),
                            ],
                            "Showing examples of your voice is the fastest way to consistent, on-brand output.",
                        ),
                        (
                            "What's a smart use of AI for ad copy?",
                            [
                                ("Generate several variations with different angles, test, keep the winner", True),
                                ("Run the first version forever without testing", False),
                                ("Copy a competitor's ad word for word", False),
                                ("Never write ads again", False),
                            ],
                            "AI makes variation cheap — test different angles and let real results pick the winner.",
                        ),
                        (
                            "How can AI help you understand customer feedback?",
                            [
                                ("Paste the comments and ask for the top themes with quoted examples", True),
                                ("It can't analyze text", False),
                                ("By deleting negative comments", False),
                                ("By responding angrily on your behalf", False),
                            ],
                            "Theme extraction from raw feedback is a classic AI win — patterns, examples, and priorities in seconds.",
                        ),
                    ],
                },
            },
            {
                "title": "AI in Education, Healthcare & Construction",
                "slug": "ai-education-health-construction",
                "type": "reading",
                "duration": 15,
                "content": """
<p>Three very different fields — one common thread: AI removes the paperwork so professionals can focus on people.</p>
<h2>Education 🎓</h2>
<ul>
<li><strong>Lesson planning:</strong> "Create a 40-minute lesson plan on coral reef ecosystems for Year 7, including a starter activity, group task, and exit quiz."</li>
<li><strong>Differentiation:</strong> "Rewrite this worksheet at three reading levels."</li>
<li><strong>Feedback:</strong> "Draft constructive comments for a student who writes creatively but struggles with structure."</li>
<li><strong>Classroom policy:</strong> teach students to use AI to <em>learn</em> (explanations, practice questions) rather than to <em>bypass</em> learning.</li>
</ul>
<h2>Healthcare 🩺</h2>
<ul>
<li><strong>Patient-friendly language:</strong> "Explain what an HbA1c test measures to a newly diagnosed patient, gently and simply."</li>
<li><strong>Admin relief:</strong> appointment letters, referral summaries, clinic FAQs, staff training notes.</li>
<li><strong>Research digestion:</strong> "Summarize this paper's method and findings; list its limitations."</li>
<li><strong>Hard boundary:</strong> AI supports communication and admin — <strong>diagnosis and treatment decisions belong to clinicians</strong>, and patient data never enters public tools.</li>
</ul>
<h2>Construction & Real Estate 🏗️</h2>
<ul>
<li><strong>Quotes and scopes:</strong> "Turn these site notes into a structured quote: scope, materials, labour, exclusions, timeline."</li>
<li><strong>Client updates:</strong> "Write a weekly progress email: foundation complete, plumbing rough-in next week, two days lost to rain."</li>
<li><strong>Listings that sell:</strong> "Write a listing for a 3-bed canal-front home in Prospect — highlight the dock and renovated kitchen."</li>
<li><strong>Safety and training:</strong> toolbox-talk outlines, checklist drafts, induction materials.</li>
</ul>
<div class="callout"><p><strong>The pattern across all industries:</strong> AI eats the writing, summarizing, and structuring. You keep the expertise, relationships, and responsibility.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "What is the hard boundary for AI in healthcare?",
                            [
                                ("Diagnosis and treatment decisions belong to clinicians; patient data stays out of public tools", True),
                                ("AI should diagnose patients directly to save time", False),
                                ("AI can't help healthcare at all", False),
                                ("Only surgeons may use AI", False),
                            ],
                            "AI helps with communication and admin; clinical decisions and patient data protection are non-negotiable human domains.",
                        ),
                        (
                            "How can teachers use AI for differentiation?",
                            [
                                ("Rewrite the same material at multiple reading levels", True),
                                ("Give every student identical worksheets", False),
                                ("Let AI grade final exams unsupervised", False),
                                ("Ban reading in class", False),
                            ],
                            "One worksheet, three reading levels, in seconds — differentiation is a classic education win for AI.",
                        ),
                        (
                            "What's the common pattern of AI value across all industries?",
                            [
                                ("AI handles writing, summarizing, and structuring; humans keep expertise and responsibility", True),
                                ("AI replaces all workers in every field", False),
                                ("AI only works in tech companies", False),
                                ("AI is only useful for entertainment", False),
                            ],
                            "Across every field, AI removes the paperwork layer while humans keep judgment, relationships, and accountability.",
                        ),
                    ],
                },
            },
        ],
    },
    # ------------------------------------------------------------------
    # MODULE 5 — Modern AI Tools & Responsible Use
    # ------------------------------------------------------------------
    {
        "title": "Modern AI Tools & Responsible Use",
        "subtitle": "The full toolkit — Claude, Gemini, Copilot, Perplexity, Midjourney — and how to use it safely.",
        "icon": "construction",
        "lessons": [
            {
                "title": "The Big Three: ChatGPT, Claude, and Gemini",
                "slug": "big-three-assistants",
                "type": "reading",
                "duration": 15,
                "content": """
<p>ChatGPT isn't the only game in town. Knowing the strengths of each major assistant makes you tool-flexible — a real advantage.</p>
<h2>Quick comparison</h2>
<table>
<tr><th>Tool</th><th>Made by</th><th>Known for</th></tr>
<tr><td><strong>ChatGPT</strong></td><td>OpenAI</td><td>The all-rounder: huge feature set, image generation, custom GPTs, voice mode.</td></tr>
<tr><td><strong>Claude</strong></td><td>Anthropic</td><td>Long documents, careful nuanced writing, strong reasoning, great for professional drafting and analysis.</td></tr>
<tr><td><strong>Gemini</strong></td><td>Google</td><td>Deep integration with Gmail, Docs, and Google Workspace; strong at search-connected answers.</td></tr>
</table>
<h2>How to choose (without overthinking)</h2>
<ul>
<li><strong>Live in Google Workspace?</strong> Try Gemini inside Gmail/Docs first.</li>
<li><strong>Working with long reports or contracts?</strong> Claude handles very long documents gracefully.</li>
<li><strong>Want maximum features in one place?</strong> ChatGPT's ecosystem is broadest.</li>
</ul>
<p>The skills you learned in Modules 2–3 (R-T-C-F, iteration, layered summaries) transfer to <strong>all of them</strong> — prompting is a portable skill.</p>
<h2>Free vs paid</h2>
<p>All three offer capable free tiers — perfect while learning. Paid plans (~US$20/month) buy you the newest models, more usage, and file/image features. Advice: <strong>stay free until you hit a limit that costs you real time</strong>, then upgrade the one tool you use most.</p>
<div class="callout"><p><strong>Try this:</strong> give the same prompt to two assistants and compare answers. You'll quickly develop a feel for their personalities.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "Which assistant is known for deep integration with Gmail and Google Docs?",
                            [
                                ("Gemini", True),
                                ("Claude", False),
                                ("Midjourney", False),
                                ("Excel", False),
                            ],
                            "Gemini is Google's assistant and lives inside Gmail, Docs, and the rest of Workspace.",
                        ),
                        (
                            "What's notable about prompting skills across different AI assistants?",
                            [
                                ("They transfer — good prompting works on all major tools", True),
                                ("Each tool needs a completely different language", False),
                                ("Prompts only work on ChatGPT", False),
                                ("Skills expire monthly", False),
                            ],
                            "R-T-C-F, iteration, and the rest are portable — the tools differ, the craft doesn't.",
                        ),
                        (
                            "What's the sensible advice on free vs paid plans while learning?",
                            [
                                ("Stay free until a limit costs you real time, then upgrade your main tool", True),
                                ("Buy every paid plan immediately", False),
                                ("Never pay for anything ever", False),
                                ("Paid plans are required to log in", False),
                            ],
                            "Free tiers are great for learning; upgrade only when a real limitation starts costing you time.",
                        ),
                    ],
                },
            },
            {
                "title": "Copilot, Perplexity & NotebookLM: Specialist Tools",
                "slug": "specialist-tools",
                "type": "reading",
                "duration": 12,
                "content": """
<p>Beyond the general assistants, three specialists deserve a place in your toolkit.</p>
<h2>Microsoft Copilot — AI inside Office</h2>
<p>If your organization runs on Word, Excel, Outlook, and Teams, Copilot brings AI directly into those apps:</p>
<ul>
<li><strong>Outlook:</strong> "Summarize this email thread and draft a reply."</li>
<li><strong>Word:</strong> "Rewrite this section more concisely."</li>
<li><strong>Excel:</strong> "Add a column calculating year-over-year growth."</li>
<li><strong>Teams:</strong> automatic meeting recaps with action items.</li>
</ul>
<p>Big advantage for business: it works within your company's Microsoft security boundary (check your IT policy).</p>
<h2>Perplexity — the research engine</h2>
<p>Perplexity is built for <strong>answering questions with sources</strong>. It searches the web, synthesizes an answer, and shows citations you can click and verify.</p>
<div class="prompt-box">What are the current work permit categories in the Cayman Islands and their fees? Cite official sources.</div>
<p>Use it when facts and freshness matter more than creative drafting.</p>
<h2>NotebookLM — chat with YOUR documents</h2>
<p>Google's NotebookLM lets you upload a stack of documents (reports, PDFs, notes) and then ask questions <strong>answered only from those documents</strong>, with citations to the exact passage. It can even generate a podcast-style audio overview of your sources. Perfect for studying regulations, onboarding packs, or research piles.</p>
<div class="callout"><p><strong>Choosing quickly:</strong> Writing/drafting → ChatGPT or Claude. Fresh facts with sources → Perplexity. Questions about your own documents → NotebookLM. AI inside Office → Copilot.</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "When is Perplexity the right tool?",
                            [
                                ("When you need current facts with clickable sources", True),
                                ("When you want to generate images", False),
                                ("When you need to edit a spreadsheet", False),
                                ("When you want to write poetry", False),
                            ],
                            "Perplexity is a research engine: it searches, synthesizes, and cites sources you can verify.",
                        ),
                        (
                            "What makes NotebookLM special?",
                            [
                                ("It answers questions using only the documents you upload, with citations", True),
                                ("It's the only tool that works offline", False),
                                ("It automatically emails your boss", False),
                                ("It replaces your web browser", False),
                            ],
                            "NotebookLM is grounded in YOUR sources — answers come from your uploaded documents with exact citations.",
                        ),
                        (
                            "Where does Microsoft Copilot shine?",
                            [
                                ("Inside Word, Excel, Outlook, and Teams within your company's security boundary", True),
                                ("Generating music", False),
                                ("Flying drones", False),
                                ("Replacing Windows entirely", False),
                            ],
                            "Copilot embeds AI into the Office apps many businesses already live in, under corporate security controls.",
                        ),
                    ],
                },
            },
            {
                "title": "Creative AI: Midjourney and Image Generation",
                "slug": "creative-ai-images",
                "type": "reading",
                "duration": 12,
                "content": """
<p>AI doesn't just write — it designs. Image generators turn text descriptions into professional visuals in seconds.</p>
<h2>The main players</h2>
<ul>
<li><strong>Midjourney</strong> — the artist's favourite; stunning, stylized results.</li>
<li><strong>DALL·E (inside ChatGPT)</strong> — convenient, good quality, easy iteration in chat.</li>
<li><strong>Ideogram / Flux</strong> — strong at images containing readable text (posters, flyers).</li>
<li><strong>Canva AI</strong> — image generation built into a design tool many small businesses already use.</li>
</ul>
<h2>Anatomy of an image prompt</h2>
<div class="prompt-box">[Subject] + [Setting] + [Style] + [Lighting/Mood] + [Format]

"A beachfront café breakfast spread with tropical fruit, Seven Mile Beach in the background, bright airy photography style, soft morning light, wide banner format for a website header"</div>
<h2>Business uses</h2>
<ul>
<li>Social media graphics and seasonal promos</li>
<li>Website hero images and banners</li>
<li>Menu and flyer illustrations</li>
<li>Concept mockups ("show a beach bar redesigned in modern Caribbean style")</li>
</ul>
<h2>The rules of the road</h2>
<ul>
<li><strong>People:</strong> don't generate images of real, identifiable people without consent.</li>
<li><strong>Brands:</strong> avoid logos and trademarked characters.</li>
<li><strong>Honesty:</strong> don't pass off AI images as real photos of your actual venue or products — customers notice, and trust is your currency.</li>
<li><strong>Rights:</strong> check your generator's commercial-use terms (most paid plans allow it).</li>
</ul>
<div class="callout"><p><strong>Iteration works here too:</strong> generate 4 options, pick the best, then refine — "same image but at sunset, more people, vertical format."</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "What are the useful parts of an image prompt?",
                            [
                                ("Subject, setting, style, lighting/mood, and format", True),
                                ("Just the word 'nice picture'", False),
                                ("Your login credentials", False),
                                ("The image file itself", False),
                            ],
                            "Subject + setting + style + mood + format gives the generator everything it needs for a usable result.",
                        ),
                        (
                            "Which is an ethical rule for AI images in business?",
                            [
                                ("Don't pass off AI images as real photos of your actual venue", True),
                                ("Always claim AI images are real photographs", False),
                                ("Use celebrity faces freely in ads", False),
                                ("Copy competitors' logos into your flyers", False),
                            ],
                            "Honesty preserves customer trust: AI visuals are fine for design, but don't misrepresent them as real photos.",
                        ),
                        (
                            "Which tool family is strongest when the image must contain readable text (like a poster)?",
                            [
                                ("Ideogram / Flux", True),
                                ("Excel", False),
                                ("NotebookLM", False),
                                ("A calculator", False),
                            ],
                            "Text rendering inside images is a known specialty of Ideogram and Flux.",
                        ),
                    ],
                },
            },
            {
                "title": "Using AI Safely, Ethically & Your Next Steps",
                "slug": "responsible-ai-next-steps",
                "type": "reading",
                "duration": 15,
                "content": """
<p>You've built real skills. This final lesson locks in the safety habits that protect you, your employer, and your clients — and points you forward.</p>
<h2>The five rules of responsible AI use</h2>
<ol>
<li><strong>Protect private data.</strong> No client names, account numbers, medical details, passwords, or unreleased business figures in public tools. Anonymize or use company-approved AI.</li>
<li><strong>Verify before you rely.</strong> Facts, figures, citations, laws — check them. AI is confident even when wrong.</li>
<li><strong>Stay accountable.</strong> "The AI wrote it" is never an excuse. If your name is on it, you own it.</li>
<li><strong>Be transparent when it matters.</strong> Follow your organization's rules on disclosing AI use; never present AI images/text as human-made where authenticity is expected.</li>
<li><strong>Watch for bias.</strong> AI learned from the internet, biases included. Review outputs about people (hiring, reviews, descriptions) with extra care.</li>
</ol>
<h2>A personal AI policy (60 seconds)</h2>
<div class="prompt-box">My green list (freely use AI): drafting, brainstorming, summarizing public info, formulas, translations…
My yellow list (use with care + review): client-facing text, reports, anything with numbers…
My red list (never): confidential data, final professional judgments, anything I couldn't defend…</div>
<h2>Where to go from here</h2>
<ul>
<li><strong>Keep the habit:</strong> your two daily AI moments from Module 3 — protect them.</li>
<li><strong>Grow your prompt library:</strong> aim for 20 saved, proven prompts.</li>
<li><strong>Teach someone:</strong> explaining prompting to a colleague is the fastest way to master it.</li>
<li><strong>Stay curious:</strong> tools will change; the fundamentals you learned here (clear communication, iteration, verification) will not.</li>
</ul>
<div class="callout"><p><strong>Congratulations!</strong> Pass this final quiz and your AI 101 Academy certificate is ready to download and share. 🎓</p></div>
""",
                "quiz": {
                    "pass_percent": 70,
                    "questions": [
                        (
                            "Who is accountable for work produced with AI assistance?",
                            [
                                ("You — if your name is on it, you own it", True),
                                ("The AI company", False),
                                ("Nobody", False),
                                ("The internet", False),
                            ],
                            "AI is a tool. Responsibility for accuracy and quality always stays with the human who uses and signs the work.",
                        ),
                        (
                            "Which item belongs on your personal 'red list'?",
                            [
                                ("Pasting confidential client data into public AI tools", True),
                                ("Brainstorming promotion ideas", False),
                                ("Summarizing a public news article", False),
                                ("Asking for an Excel formula", False),
                            ],
                            "Confidential data never enters public tools — that's a permanent red-list item for every professional.",
                        ),
                        (
                            "Why review AI outputs about people (like hiring texts) with extra care?",
                            [
                                ("AI learned from the internet and can reproduce its biases", True),
                                ("AI dislikes people", False),
                                ("Such texts are always perfect", False),
                                ("It's illegal for AI to mention people", False),
                            ],
                            "Training data contains human biases; outputs about people deserve deliberate human review.",
                        ),
                        (
                            "What will stay valuable even as AI tools change?",
                            [
                                ("Clear communication, iteration, and verification habits", True),
                                ("Memorizing one tool's menu layout", False),
                                ("Never trying new tools", False),
                                ("Keeping AI a secret from colleagues", False),
                            ],
                            "Tools evolve fast; the fundamentals — communicating clearly, iterating, verifying — are permanent skills.",
                        ),
                    ],
                },
            },
        ],
    },
]

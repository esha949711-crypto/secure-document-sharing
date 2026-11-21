/* =========================================================
   SECUREVAULT — PROFESSIONAL CYBERSECURITY UI
   Dark Navy / Electric Indigo Theme
   Designed for Streamlit
========================================================= */

/* ---------------------------------------------------------
   1. ROOT VARIABLES
--------------------------------------------------------- */

:root {
    --bg: #070b17;
    --bg-soft: #0b1222;

    --surface: #0f182b;
    --surface-2: #121d33;
    --surface-3: #16243d;

    --border: rgba(112, 139, 190, 0.20);
    --border-strong: rgba(124, 145, 255, 0.38);

    --primary: #7c6cff;
    --primary-2: #4f8cff;
    --primary-soft: rgba(124, 108, 255, 0.14);

    --success: #35d6a2;
    --success-soft: rgba(53, 214, 162, 0.12);

    --warning: #f5b84b;
    --danger: #ff667d;

    --text: #f5f7ff;
    --text-soft: #c5cde0;
    --muted: #8e9ab5;

    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 18px;
    --radius-xl: 24px;

    --shadow:
        0 20px 60px rgba(0, 0, 0, 0.28);

    --glow:
        0 0 35px rgba(124, 108, 255, 0.12);
}


/* =========================================================
   2. GLOBAL APPLICATION
========================================================= */

.stApp {
    background:
        radial-gradient(
            circle at 8% 0%,
            rgba(83, 76, 180, 0.16) 0%,
            transparent 30%
        ),
        radial-gradient(
            circle at 92% 8%,
            rgba(52, 112, 205, 0.13) 0%,
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #070b17 0%,
            #0a1020 48%,
            #070c18 100%
        );

    color: var(--text);
    min-height: 100vh;
}


/* ---------------------------------------------------------
   GLOBAL FONT
--------------------------------------------------------- */

html,
body,
[class*="css"] {
    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
}


/* ---------------------------------------------------------
   MAIN CONTAINER
--------------------------------------------------------- */

.block-container {
    max-width: 1480px !important;

    padding-top: 1.4rem !important;
    padding-left: 2.2rem !important;
    padding-right: 2.2rem !important;
    padding-bottom: 4rem !important;
}


/* ---------------------------------------------------------
   HIDE STREAMLIT DEFAULT UI
--------------------------------------------------------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* =========================================================
   3. TOP NAVIGATION / BRAND BAR
========================================================= */

.topbar {
    position: relative;

    display: flex;
    align-items: center;
    justify-content: space-between;

    min-height: 74px;

    padding: 14px 20px;

    margin-bottom: 25px;

    background:
        linear-gradient(
            135deg,
            rgba(17, 28, 50, 0.96),
            rgba(10, 19, 36, 0.96)
        );

    border: 1px solid var(--border);

    border-radius: var(--radius-lg);

    box-shadow:
        0 15px 45px rgba(0, 0, 0, 0.18);

    backdrop-filter: blur(18px);

    overflow: hidden;
}


/* Topbar subtle glow */

.topbar::before {
    content: "";

    position: absolute;

    top: -100px;
    right: 20%;

    width: 280px;
    height: 180px;

    background: rgba(108, 95, 255, 0.08);

    filter: blur(60px);

    pointer-events: none;
}


/* Brand */

.brand {
    display: flex;
    align-items: center;

    gap: 13px;

    position: relative;
    z-index: 2;
}


.brand-icon {
    width: 45px;
    height: 45px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 12px;

    font-size: 21px;

    background:
        linear-gradient(
            135deg,
            #7668ff 0%,
            #4b8ff5 100%
        );

    box-shadow:
        0 8px 25px rgba(91, 104, 255, 0.25);

    border: 1px solid rgba(255, 255, 255, 0.12);
}


.brand-name {
    color: #ffffff;

    font-size: 20px;

    font-weight: 800;

    letter-spacing: -0.4px;

    line-height: 1.1;
}


.brand-subtitle {
    margin-top: 4px;

    color: #7f8da9;

    font-size: 8px;

    font-weight: 700;

    letter-spacing: 2px;

    text-transform: uppercase;
}


.top-status {
    display: flex;
    align-items: center;

    gap: 7px;

    color: #5fe6b5;

    background:
        rgba(35, 139, 106, 0.10);

    border: 1px solid rgba(53, 214, 162, 0.25);

    border-radius: 999px;

    padding: 8px 13px;

    font-size: 9px;

    font-weight: 800;

    letter-spacing: 0.7px;
}


/* =========================================================
   4. HERO SECTION
========================================================= */

.hero {
    position: relative;

    display: flex;
    align-items: center;
    justify-content: space-between;

    min-height: 350px;

    padding: 50px 55px;

    margin-bottom: 32px;

    border-radius: var(--radius-xl);

    border: 1px solid rgba(126, 145, 255, 0.28);

    background:
        radial-gradient(
            circle at 82% 48%,
            rgba(104, 91, 244, 0.25),
            transparent 32%
        ),
        radial-gradient(
            circle at 65% 100%,
            rgba(52, 111, 210, 0.14),
            transparent 32%
        ),
        linear-gradient(
            120deg,
            #111a32 0%,
            #151f40 48%,
            #101b35 100%
        );

    overflow: hidden;

    box-shadow:
        0 30px 80px rgba(0, 0, 0, 0.20);
}


/* Hero top line */

.hero::before {
    content: "";

    position: absolute;

    left: 0;
    top: 0;

    width: 100%;
    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(130, 117, 255, 0.8),
            transparent
        );

    opacity: 0.7;
}


/* Hero decorative glow */

.hero::after {
    content: "";

    position: absolute;

    width: 300px;
    height: 300px;

    right: -100px;
    bottom: -180px;

    border-radius: 50%;

    background:
        rgba(83, 111, 255, 0.10);

    filter: blur(40px);
}


.hero-content {
    max-width: 760px;

    position: relative;
    z-index: 2;
}


.hero-label {
    color: #aaa1ff;

    font-size: 9px;

    font-weight: 800;

    letter-spacing: 2.4px;

    text-transform: uppercase;

    margin-bottom: 17px;
}


.hero h1 {
    color: #ffffff;

    font-size: clamp(34px, 4.5vw, 54px);

    line-height: 1.08;

    font-weight: 850;

    letter-spacing: -1.7px;

    margin: 0 0 19px 0;
}


.hero h1 span {
    color: #a79dff;

    background:
        linear-gradient(
            90deg,
            #a69cff,
            #75a4ff
        );

    -webkit-background-clip: text;
    background-clip: text;

    -webkit-text-fill-color: transparent;
}


.hero-copy {
    max-width: 650px;

    color: #aeb9d0;

    font-size: 13px;

    line-height: 1.9;

    margin-bottom: 22px;
}


/* Security tags */

.hero-tags {
    display: flex;

    flex-wrap: wrap;

    gap: 8px;
}


.hero-tags span {
    display: inline-flex;
    align-items: center;

    min-height: 31px;

    padding: 0 12px;

    border-radius: 7px;

    border: 1px solid rgba(126, 145, 255, 0.25);

    background:
        rgba(255, 255, 255, 0.035);

    color: #cbd4ec;

    font-size: 8px;

    font-weight: 800;

    letter-spacing: 0.7px;
}


/* Hero visual */

.hero-visual {
    position: relative;

    z-index: 2;

    display: flex;
    align-items: center;
    justify-content: center;

    width: 210px;
    height: 210px;

    margin-right: 35px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(122, 107, 255, 0.18) 0%,
            rgba(122, 107, 255, 0.05) 42%,
            transparent 70%
        );

    font-size: 96px;

    filter:
        drop-shadow(0 0 35px rgba(124, 108, 255, 0.42));
}


/* =========================================================
   5. SECTION HEADING
========================================================= */

.section-heading {
    display: flex;
    align-items: center;

    color: #7f8ca8;

    font-size: 9px;

    font-weight: 800;

    letter-spacing: 2px;

    margin: 8px 0 12px 3px;

    text-transform: uppercase;
}


/* =========================================================
   6. TABS / NAVIGATION
========================================================= */

.stTabs {
    margin-top: 0 !important;
}


/* Tab container */

.stTabs [data-baseweb="tab-list"] {
    display: flex;

    gap: 5px;

    padding: 6px;

    background:
        rgba(12, 21, 39, 0.94);

    border: 1px solid var(--border);

    border-radius: 14px;

    box-shadow:
        0 10px 35px rgba(0, 0, 0, 0.15);
}


/* Individual tab */

.stTabs [data-baseweb="tab"] {
    min-height: 42px;

    padding: 10px 19px;

    border-radius: 9px;

    color: #8f9bb5;

    font-size: 11px;

    font-weight: 700;

    border: none;

    transition:
        all 0.2s ease;
}


/* Tab hover */

.stTabs [data-baseweb="tab"]:hover {
    color: #dce4f7;

    background:
        rgba(255, 255, 255, 0.035);
}


/* Active tab */

.stTabs [aria-selected="true"] {
    color: #ffffff !important;

    background:
        linear-gradient(
            110deg,
            #685be0 0%,
            #487edc 100%
        ) !important;

    box-shadow:
        0 7px 24px rgba(88, 91, 221, 0.25);
}


/* Hide default tab underline */

.stTabs [data-baseweb="tab-highlight"] {
    display: none !important;
}


/* =========================================================
   7. WELCOME PANEL
========================================================= */

.welcome {
    position: relative;

    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 22px 25px;

    margin: 26px 0 20px;

    border-radius: 15px;

    background:
        linear-gradient(
            135deg,
            rgba(19, 32, 57, 0.95),
            rgba(14, 25, 44, 0.95)
        );

    border: 1px solid var(--border);

    overflow: hidden;
}


.welcome::before {
    content: "";

    position: absolute;

    width: 170px;
    height: 170px;

    right: -80px;
    top: -90px;

    background:
        rgba(102, 93, 255, 0.09);

    border-radius: 50%;

    filter: blur(25px);
}


.welcome h2 {
    position: relative;

    color: #ffffff;

    font-size: 20px;

    font-weight: 800;

    letter-spacing: -0.4px;

    margin: 0 0 5px;
}


.welcome p {
    position: relative;

    color: #8f9bb5;

    font-size: 11px;

    margin: 0;
}


.welcome-badge {
    position: relative;

    color: #aaa1ff;

    border: 1px solid rgba(123, 108, 255, 0.28);

    background:
        rgba(124, 108, 255, 0.06);

    padding: 8px 13px;

    border-radius: 7px;

    font-size: 8px;

    font-weight: 800;

    letter-spacing: 1.3px;
}


/* =========================================================
   8. FEATURE CARDS
========================================================= */

.feature-card {
    position: relative;

    min-height: 210px;

    padding: 24px 21px;

    border-radius: 15px;

    border: 1px solid var(--border);

    background:
        linear-gradient(
            145deg,
            rgba(19, 31, 54, 0.96),
            rgba(11, 20, 36, 0.96)
        );

    box-shadow:
        0 15px 40px rgba(0, 0, 0, 0.14);

    transition:
        transform 0.25s ease,
        border-color 0.25s ease,
        box-shadow 0.25s ease;

    overflow: hidden;
}


/* Card top accent */

.feature-card::before {
    content: "";

    position: absolute;

    left: 0;
    top: 0;

    width: 100%;
    height: 2px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(123, 108, 255, 0.55),
            transparent
        );

    opacity: 0;

    transition: opacity 0.25s ease;
}


.feature-card:hover {
    transform: translateY(-4px);

    border-color:
        rgba(123, 108, 255, 0.40);

    box-shadow:
        0 20px 50px rgba(0, 0, 0, 0.24),
        0 0 30px rgba(104, 91, 255, 0.07);
}


.feature-card:hover::before {
    opacity: 1;
}


/* Feature icon */

.feature-icon {
    width: 47px;
    height: 47px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 12px;

    font-size: 20px;

    margin-bottom: 17px;

    border: 1px solid rgba(255, 255, 255, 0.04);
}


.purple {
    background:
        rgba(116, 101, 240, 0.16);

    color: #aaa1ff;
}


.blue {
    background:
        rgba(58, 135, 221, 0.14);

    color: #86b8ff;
}


.green {
    background:
        rgba(46, 192, 144, 0.13);

    color: #62e0b5;
}


.feature-card h3 {
    color: #f5f7ff;

    font-size: 16px;

    font-weight: 750;

    margin: 0 0 9px;
}


.feature-card p {
    color: #8e9bb6;

    font-size: 11px;

    line-height: 1.75;

    margin: 0;
}


.feature-footer {
    color: #9f95f9;

    font-size: 8px;

    font-weight: 800;

    letter-spacing: 1.4px;

    margin-top: 18px;
}


/* =========================================================
   9. INFORMATION PANEL
========================================================= */

.info-panel {
    position: relative;

    display: flex;

    gap: 16px;

    margin-top: 22px;

    padding: 20px 22px;

    border-radius: 14px;

    background:
        linear-gradient(
            135deg,
            rgba(17, 40, 67, 0.82),
            rgba(13, 29, 51, 0.82)
        );

    border: 1px solid rgba(72, 126, 190, 0.27);
}


.info-icon {
    width: 36px;
    height: 36px;

    display: flex;
    align-items: center;
    justify-content: center;

    flex-shrink: 0;

    border-radius: 9px;

    background:
        rgba(75, 137, 220, 0.13);

    font-size: 17px;
}


.info-panel h4 {
    color: #eef3ff;

    font-size: 13px;

    margin: 1px 0 6px;
}


.info-panel p {
    color: #8fa3c1;

    font-size: 10px;

    line-height: 1.9;

    margin: 0;
}


/* =========================================================
   10. PAGE INTRO
========================================================= */

.page-intro {
    display: flex;
    align-items: center;

    gap: 15px;

    margin: 28px 0 20px;
}


.page-icon {
    width: 52px;
    height: 52px;

    display: flex;
    align-items: center;
    justify-content: center;

    flex-shrink: 0;

    border-radius: 14px;

    font-size: 23px;

    background:
        linear-gradient(
            135deg,
            rgba(105, 92, 226, 0.25),
            rgba(55, 103, 177, 0.18)
        );

    border: 1px solid rgba(126, 145, 255, 0.25);

    box-shadow:
        0 8px 25px rgba(80, 90, 200, 0.10);
}


.page-intro h2 {
    color: #ffffff;

    font-size: 21px;

    font-weight: 800;

    letter-spacing: -0.4px;

    margin: 0 0 4px;
}


.page-intro p {
    color: #8794ae;

    font-size: 10px;

    margin: 0;
}


/* =========================================================
   11. STREAMLIT CONTAINERS
========================================================= */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background:
        linear-gradient(
            145deg,
            rgba(16, 27, 47, 0.92),
            rgba(10, 19, 35, 0.92)
        ) !important;

    border:
        1px solid var(--border) !important;

    border-radius:
        16px !important;

    padding:
        20px !important;

    box-shadow:
        0 14px 45px rgba(0, 0, 0, 0.12);
}


/* =========================================================
   12. HEADINGS / MARKDOWN
========================================================= */

.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3,
.stMarkdown h4 {
    color: #f5f7ff !important;
}


.stMarkdown h3 {
    font-size: 17px !important;

    font-weight: 750 !important;
}


.stMarkdown h4 {
    font-size: 14px !important;

    font-weight: 700 !important;
}


/* =========================================================
   13. TEXT / CAPTIONS
========================================================= */

.stCaption,
[data-testid="stCaptionContainer"] {
    color: #7f8da8 !important;

    font-size: 10px !important;
}


.stMarkdown p {
    color: #b0bad0;
}


/* =========================================================
   14. TEXT INPUT
========================================================= */

.stTextInput {
    margin-bottom: 8px;
}


.stTextInput label {
    color: #d9e1f2 !important;

    font-size: 10px !important;

    font-weight: 700 !important;
}


.stTextInput input {
    min-height: 44px;

    background:
        #091324 !important;

    color:
        #f7f9ff !important;

    border:
        1px solid #293b5b !important;

    border-radius:
        9px !important;

    padding:
        10px 13px !important;

    font-size:
        11px !important;

    transition:
        all 0.2s ease;
}


.stTextInput input:hover {
    border-color:
        #42567d !important;
}


.stTextInput input:focus {
    border-color:
        #7468ef !important;

    box-shadow:
        0 0 0 1px rgba(116, 104, 239, 0.25),
        0 0 25px rgba(116, 104, 239, 0.07) !important;
}


/* Password input */

.stTextInput input[type="password"] {
    letter-spacing: 2px;
}


/* =========================================================
   15. FILE UPLOADER
========================================================= */

[data-testid="stFileUploader"] {
    background:
        linear-gradient(
            145deg,
            rgba(10, 20, 37, 0.90),
            rgba(13, 25, 44, 0.90)
        );

    border:
        1px dashed rgba(109, 132, 174, 0.40);

    border-radius:
        12px;

    padding:
        13px;

    transition:
        border-color 0.2s ease,
        background 0.2s ease;
}


[data-testid="stFileUploader"]:hover {
    border-color:
        rgba(126, 108, 255, 0.65);

    background:
        rgba(19, 31, 55, 0.92);
}


[data-testid="stFileUploader"] label {
    color:
        #d9e1f2 !important;

    font-size:
        10px !important;

    font-weight:
        700 !important;
}


/* File uploader text */

[data-testid="stFileUploader"] section {
    background:
        transparent !important;

    border:
        none !important;
}


/* Browse button */

[data-testid="stFileUploader"] button {
    color:
        #dce4f7 !important;

    background:
        #16243d !important;

    border:
        1px solid #344866 !important;

    border-radius:
        8px !important;

    font-size:
        10px !important;

    font-weight:
        700 !important;
}


[data-testid="stFileUploader"] button:hover {
    border-color:
        #7166e8 !important;

    color:
        #ffffff !important;
}


/* =========================================================
   16. BUTTONS
========================================================= */

.stButton > button,
.stDownloadButton > button {
    min-height: 43px;

    border-radius:
        9px !important;

    font-size:
        10px !important;

    font-weight:
        800 !important;

    letter-spacing:
        0.2px;

    color:
        #ffffff !important;

    background:
        linear-gradient(
            110deg,
            #6759d9 0%,
            #437fdc 100%
        ) !important;

    border:
        1px solid rgba(147, 139, 255, 0.35) !important;

    box-shadow:
        0 7px 24px rgba(79, 100, 218, 0.15);

    transition:
        transform 0.18s ease,
        box-shadow 0.18s ease,
        border-color 0.18s ease;
}


.stButton > button:hover,
.stDownloadButton > button:hover {
    color:
        #ffffff !important;

    border-color:
        rgba(174, 164, 255, 0.75) !important;

    transform:
        translateY(-2px);

    box-shadow:
        0 12px 30px rgba(83, 91, 218, 0.24);
}


.stButton > button:active,
.stDownloadButton > button:active {
    transform:
        translateY(0);
}


/* Secondary button appearance */

button[kind="secondary"] {
    background:
        #121f36 !important;

    border:
        1px solid #344866 !important;

    box-shadow:
        none !important;
}


/* =========================================================
   17. DIVIDER
========================================================= */

hr {
    border: none !important;

    height: 1px !important;

    background:
        linear-gradient(
            90deg,
            transparent,
            #273752,
            transparent
        ) !important;

    margin:
        24px 0 !important;
}


/* =========================================================
   18. SUCCESS MESSAGE
========================================================= */

[data-testid="stAlert"] {
    border-radius:
        10px !important;

    border:
        1px solid rgba(53, 214, 162, 0.25) !important;

    background:
        rgba(27, 83, 67, 0.18) !important;

    color:
        #a9e8d2 !important;

    font-size:
        10px !important;
}


/* Custom success panel */

.success-panel {
    display: flex;

    align-items: center;

    gap: 15px;

    padding: 18px 20px;

    margin: 17px 0;

    border-radius: 12px;

    background:
        linear-gradient(
            135deg,
            rgba(25, 94, 73, 0.22),
            rgba(13, 50, 43, 0.22)
        );

    border:
        1px solid rgba(53, 214, 162, 0.27);

    box-shadow:
        0 10px 35px rgba(0, 0, 0, 0.10);
}


.success-icon {
    width: 36px;
    height: 36px;

    display: flex;
    align-items: center;
    justify-content: center;

    flex-shrink: 0;

    border-radius: 50%;

    color: #5de5b5;

    background:
        rgba(53, 214, 162, 0.12);

    border:
        1px solid rgba(53, 214, 162, 0.20);

    font-size: 17px;
}


.success-panel h3 {
    color: #71e9c0;

    font-size: 13px;

    font-weight: 800;

    margin: 0 0 4px;
}


.success-panel p {
    color: #91b9ad;

    font-size: 10px;

    margin: 0;
}


/* =========================================================
   19. WARNING / ERROR / INFO
========================================================= */

.stWarning,
.stError,
.stInfo {
    border-radius:
        10px !important;

    font-size:
        10px !important;
}


[data-testid="stAlert"] p {
    font-size:
        10px !important;
}


/* =========================================================
   20. FINGERPRINT PANEL
========================================================= */

.fingerprint {
    position: relative;

    background:
        linear-gradient(
            135deg,
            #0b1528,
            #0e1a30
        );

    border:
        1px solid rgba(114, 104, 226, 0.28);

    border-radius:
        11px;

    padding:
        16px 18px;

    margin:
        18px 0;

    color:
        #9f96ee;

    font-size:
        9px;

    line-height:
        1.9;

    overflow-wrap:
        anywhere;

    box-shadow:
        inset 0 0 30px rgba(100, 90, 240, 0.025);
}


.fingerprint strong {
    display: block;

    color:
        #e8eaff;

    font-size:
        11px;

    font-family:
        "JetBrains Mono",
        "Consolas",
        monospace;

    letter-spacing:
        0.3px;

    margin-top:
        3px;
}


/* =========================================================
   21. CODE BLOCKS
========================================================= */

.stCodeBlock {
    border-radius:
        10px !important;

    border:
        1px solid #273957 !important;

    background:
        #080f1e !important;

    box-shadow:
        inset 0 0 30px rgba(0, 0, 0, 0.16);
}


.stCodeBlock pre {
    font-size:
        9px !important;

    line-height:
        1.65 !important;
}


/* =========================================================
   22. DOWNLOAD BUTTON
========================================================= */

.stDownloadButton {
    margin-top:
        8px;
}


.stDownloadButton > button {
    background:
        linear-gradient(
            110deg,
            #6558d7,
            #3e78d0
        ) !important;
}


/* =========================================================
   23. SPINNER
========================================================= */

.stSpinner > div {
    border-top-color:
        #8376ff !important;
}


/* =========================================================
   24. COLUMNS
========================================================= */

[data-testid="column"] {
    padding-left:
        0.35rem;

    padding-right:
        0.35rem;
}


/* =========================================================
   25. FOOTER
========================================================= */

.footer {
    position: relative;

    text-align: center;

    padding:
        40px 15px 10px;

    margin-top:
        55px;
}


.footer-brand {
    color:
        #a69cff;

    font-size:
        18px;

    font-weight:
        850;

    letter-spacing:
        -0.3px;
}


.footer p {
    color:
        #71809d;

    font-size:
        9px;

    margin:
        5px 0;
}


.footer small {
    color:
        #596984;

    font-size:
        8px;
}


.footer-line {
    width:
        100%;

    max-width:
        560px;

    height:
        1px;

    margin:
        20px auto 15px;

    background:
        linear-gradient(
            90deg,
            transparent,
            #273650,
            transparent
        );
}


/* =========================================================
   26. SCROLLBAR
========================================================= */

::-webkit-scrollbar {
    width:
        7px;

    height:
        7px;
}


::-webkit-scrollbar-track {
    background:
        #070b17;
}


::-webkit-scrollbar-thumb {
    background:
        #263653;

    border-radius:
        20px;
}


::-webkit-scrollbar-thumb:hover {
    background:
        #3c4e73;
}


/* =========================================================
   27. MOBILE RESPONSIVE
========================================================= */

@media (max-width: 900px) {

    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .hero {
        padding:
            35px 28px;

        min-height:
            300px;
    }

    .hero-visual {
        width:
            150px;

        height:
            150px;

        font-size:
            70px;

        margin-right:
            0;
    }
}


@media (max-width: 768px) {

    .block-container {
        padding:
            0.8rem !important;
    }

    .topbar {
        min-height:
            65px;

        padding:
            11px 13px;

        border-radius:
            13px;
    }

    .brand-icon {
        width:
            39px;

        height:
            39px;

        font-size:
            18px;
    }

    .brand-name {
        font-size:
            17px;
    }

    .brand-subtitle {
        font-size:
            7px;
    }

    .top-status {
        padding:
            7px 9px;

        font-size:
            7px;
    }

    .hero {
        padding:
            30px 22px;

        min-height:
            0;

        border-radius:
            18px;
    }

    .hero h1 {
        font-size:
            32px;

        letter-spacing:
            -1px;
    }

    .hero-copy {
        font-size:
            11px;

        line-height:
            1.8;
    }

    .hero-visual {
        display:
            none;
    }

    .hero-tags span {
        font-size:
            7px;

        padding:
            7px 9px;
    }

    .welcome {
        flex-direction:
            column;

        align-items:
            flex-start;

        gap:
            15px;
    }

    .welcome-badge {
        align-self:
            flex-start;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap:
            3px;

        overflow-x:
            auto;
    }

    .stTabs [data-baseweb="tab"] {
        min-width:
            max-content;

        padding:
            10px 11px;

        font-size:
            8px;
    }

    .page-intro h2 {
        font-size:
            18px;
    }

    .page-icon {
        width:
            46px;

        height:
            46px;

        font-size:
            20px;
    }

    .feature-card {
        min-height:
            190px;
    }
}


/* =========================================================
   28. ACCESSIBILITY / REDUCED MOTION
========================================================= */

@media (prefers-reduced-motion: reduce) {

    * {
        transition:
            none !important;

        animation:
            none !important;
    }
}

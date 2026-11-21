from pathlib import Path

import streamlit as st
from sdsp import core

if not st.runtime.exists():
    print(
        "This is a Streamlit app. Start it with: "
        "python -m streamlit run .\\streamlit_app.py"
    )
    raise SystemExit(0)

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="SecureVault | Document Security",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# PROFESSIONAL CSS DESIGN
# ==========================================

st.markdown("""
<style>

:root {
    --bg: #080d1b;
    --surface: #111a2e;
    --border: #263550;
    --primary: #7467f0;
    --text: #f1f5ff;
    --muted: #98a7c1;
    --green: #39d6a0;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #17244a 0%, transparent 35%),
        radial-gradient(ellipse at 95% 20%, #18204a 0%, transparent 30%),
        var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1450px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

#MainMenu, footer, header {
    visibility: hidden;
}

/* TOP BAR */

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 23px;
    margin-bottom: 28px;
    background: rgba(19,29,50,.9);
    border: 1px solid var(--border);
    border-radius: 16px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 13px;
}

.brand-icon {
    background: linear-gradient(135deg,#7163f2,#318eea);
    width: 48px;
    height: 48px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 13px;
    font-size: 24px;
}

.brand-name {
    font-size: 21px;
    font-weight: 800;
    color: white;
}

.brand-subtitle {
    font-size: 9px;
    letter-spacing: 2px;
    color: #98a7c1;
}

.top-status {
    color: #39d6a0;
    background: #12352e;
    border: 1px solid #28604e;
    border-radius: 30px;
    padding: 10px 15px;
    font-size: 10px;
    font-weight: 700;
}

/* HERO */

.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    min-height: 320px;
    padding: 45px 55px;
    border-radius: 23px;
    border: 1px solid #394775;
    background:
        radial-gradient(circle at 80% 50%,#37347c 0%,transparent 32%),
        linear-gradient(115deg,#171d3d,#202958 55%,#17254a);
    margin-bottom: 35px;
}

.hero-content {
    max-width: 720px;
}

.hero-label {
    color: #b9adff;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero h1 {
    color: white;
    font-size: clamp(32px,4vw,49px);
    font-weight: 800;
    line-height: 1.2;
    margin: 20px 0;
}

.hero h1 span {
    color: #a99cff;
}

.hero-copy {
    color: #bac5df;
    font-size: 14px;
    line-height: 1.9;
}

.hero-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 23px;
}

.hero-tags span {
    padding: 9px 13px;
    border-radius: 8px;
    border: 1px solid #50598e;
    background: rgba(255,255,255,.06);
    color: #e0e4ff;
    font-size: 10px;
    font-weight: 600;
}

.hero-visual {
    font-size: 100px;
    padding: 35px;
    filter: drop-shadow(0 0 30px #8176ff);
}

/* SECTION HEADING */

.section-heading {
    color: #a5b2d0;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    margin: 25px 0 17px;
}

/* TABS */

.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    background: #111a2e;
    padding: 8px;
    border: 1px solid #263550;
    border-radius: 13px;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 9px;
    color: rgba(255, 255, 255, 0.8);
    font-size: 13px;
    font-weight: 600;
    padding: 13px 20px;
    border: none;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(110deg,#6658dc,#417edc) !important;
    color: white !important;
}

/* DASHBOARD */

.welcome {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 28px 0;
    padding: 22px 25px;
    border-radius: 14px;
    background: #19253e;
    border: 1px solid #263550;
}

.welcome h2 {
    color: white;
    font-size: 22px;
    margin: 0 0 7px;
}

.welcome p {
    color: #98a7c1;
    font-size: 13px;
}

.welcome-badge {
    color: #a99cff;
    font-size: 10px;
    letter-spacing: 1px;
    border: 1px solid #4a428c;
    padding: 9px 14px;
    border-radius: 8px;
}

.feature-card {
    min-height: 215px;
    padding: 25px 22px;
    border: 1px solid #263550;
    border-radius: 16px;
    background: linear-gradient(145deg,#17233c,#10192c);
    transition: .25s;
}

.feature-card:hover {
    transform: translateY(-5px);
    border-color: #7165d9;
}

.feature-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    border-radius: 12px;
    margin-bottom: 18px;
}

.purple {background: #30295e;}
.blue {background: #163b5d;}
.green {background: #17483e;}

.feature-card h3 {
    color: white;
    font-size: 17px;
}

.feature-card p {
    color: #9caec9;
    font-size: 12px;
    line-height: 1.8;
}

.feature-footer {
    color: #a99cff;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.4px;
    margin-top: 18px;
}

/* INFO PANEL */

.info-panel {
    display: flex;
    gap: 17px;
    margin-top: 25px;
    padding: 23px;
    background: #132743;
    border: 1px solid #31527d;
    border-radius: 14px;
}

.info-icon {
    font-size: 25px;
}

.info-panel h4 {
    color: white;
}

.info-panel p {
    color: #a9bad4;
    font-size: 12px;
    line-height: 1.9;
}

/* PAGE HEADINGS */

.page-intro {
    display: flex;
    align-items: center;
    gap: 17px;
    margin: 30px 0 23px;
}

.page-icon {
    width: 58px;
    height: 58px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 15px;
    font-size: 27px;
    background: linear-gradient(135deg,#39346f,#214d80);
    border: 1px solid #515a9c;
}

.page-intro h2 {
    color: white;
    font-size: 23px;
    margin: 0 0 6px;
}

.page-intro p {
    color: #98a7c1;
    font-size: 12px;
}

/* CONTAINERS */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(17,27,47,.86);
    border: 1px solid #263550 !important;
    border-radius: 16px;
    padding: 20px;
}

.stMarkdown h3,
.stMarkdown h4 {
    color: #f1f5ff;
}

/* INPUTS */

.stTextInput label,
.stFileUploader label {
    color: #dbe4f7 !important;
    font-weight: 600;
    font-size: 13px;
}

.stTextInput input {
    background: #0d1629 !important;
    color: white !important;
    border: 1px solid #334563 !important;
    border-radius: 10px !important;
    padding: 13px !important;
}

[data-testid="stFileUploader"] {
    background: #101b30;
    border: 1px dashed #58658b;
    border-radius: 12px;
    padding: 15px;
}

/* BUTTONS */

.stButton > button,
.stDownloadButton > button {
    min-height: 44px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 12px;
    border: 1px solid #5553a2;
    color: white;
    background: linear-gradient(110deg,#6758d9,#387edb);
    transition: .2s;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    border-color: #a99cff;
    color: white;
    transform: translateY(-2px);
}

/* FINGERPRINT */

.fingerprint {
    background: #101b30;
    border: 1px solid #3e477d;
    border-radius: 12px;
    padding: 17px;
    margin: 20px 0;
    color: #a99cff;
    font-size: 10px;
    line-height: 2.2;
    overflow-wrap: anywhere;
}

.fingerprint strong {
    color: white;
    font-size: 12px;
}

/* SUCCESS */

.success-panel {
    display: flex;
    align-items: center;
    gap: 17px;
    padding: 20px;
    margin: 18px 0;
    background: #12342e;
    border: 1px solid #247b65;
    border-radius: 13px;
}

.success-icon {
    font-size: 27px;
    color: #39d6a0;
}

.success-panel h3 {
    color: #70edbf;
    font-size: 16px;
    margin: 0;
}

.success-panel p {
    color: #a5c9be;
    font-size: 12px;
}

/* FOOTER */

.footer {
    text-align: center;
    padding: 38px 15px 15px;
    margin-top: 55px;
}

.footer-brand {
    color: #b4a9ff;
    font-size: 20px;
    font-weight: 800;
}

.footer p,
.footer small {
    color: #8596b3;
    font-size: 11px;
}

.footer-line {
    height: 1px;
    background: #27344d;
    margin: 20px auto;
    max-width: 600px;
}

/* RESPONSIVE */

@media(max-width:768px) {
    .block-container {padding: 1rem;}
    .hero {padding: 30px 22px;}
    .hero-visual {display: none;}
    .hero h1 {font-size: 33px;}
    .welcome {flex-direction: column;align-items: flex-start;}
    .topbar {padding: 12px;}
    .stTabs [data-baseweb="tab"] {
        padding: 10px 7px;
        font-size: 10px;
    }
}

</style>
""", unsafe_allow_html=True)

theme_css = Path(__file__).with_name("style.css").read_text(encoding="utf-8")
st.markdown(f"<style>{theme_css}</style>", unsafe_allow_html=True)


# ==========================================
# SESSION STATE
# ==========================================

defaults = {
    "generated_keypair": None,
    "show_public_key": False,
    "show_private_key": False
}

for key, value in defaults.items():
    st.session_state.setdefault(key, value)


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="topbar">
    <div class="brand">
        <div class="brand-icon">🔐</div>
        <div>
            <div class="brand-name">SecureVault</div>
            <div class="brand-subtitle">DOCUMENT SECURITY PLATFORM</div>
        </div>
    </div>
    <div class="top-status">● SYSTEM READY</div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# HERO
# ==========================================

st.markdown("""
<div class="hero">
    <div class="hero-content">
        <div class="hero-label">✦ ADVANCED DOCUMENT PROTECTION</div>
        <h1>Secure your files.<br>
        <span>Share with confidence.</span></h1>
        <p class="hero-copy">
            Protect sensitive documents using advanced encryption.
            Generate secure keys, encrypt files and decrypt
            protected documents with confidence.
        </p>
        <div class="hero-tags">
            <span>🛡 AES-256-GCM</span>
            <span>🔑 RSA-OAEP</span>
            <span>✓ AUTHENTICATED ENCRYPTION</span>
        </div>
    </div>
    <div class="hero-visual">🛡️</div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# NAVIGATION
# ==========================================

st.markdown(
    '<div class="section-heading">SECURITY WORKSPACE</div>',
    unsafe_allow_html=True
)

tab_dashboard, tab_keys, tab_encrypt, tab_decrypt = st.tabs([
    "⌂ Dashboard",
    "🔑 Generate Keys",
    "🔒 Encrypt File",
    "🔓 Decrypt File"
])


# ==========================================
# DASHBOARD
# ==========================================

with tab_dashboard:

    st.markdown("""
    <div class="welcome">
        <div>
            <h2>Welcome to SecureVault</h2>
            <p>Choose a security operation to get started.</p>
        </div>
        <div class="welcome-badge">SECURE WORKSPACE</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon purple">🔑</div>
            <h3>Key Generation</h3>
            <p>Generate an RSA-3072 public and private key pair.</p>
            <div class="feature-footer">RSA-3072 ENCRYPTION</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon blue">🔒</div>
            <h3>File Encryption</h3>
            <p>Protect documents using authenticated encryption.</p>
            <div class="feature-footer">AES-256-GCM</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon green">🔓</div>
            <h3>File Decryption</h3>
            <p>Recover protected documents using your private key.</p>
            <div class="feature-footer">AUTHENTICATED DECRYPTION</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-panel">
        <div class="info-icon">💡</div>
        <div>
            <h4>How SecureVault Works</h4>
            <p>
                First, generate your RSA key pair. Share your public key
                with the sender. The sender encrypts a document using
                your public key. Finally, use your private key to decrypt
                and recover the original document.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# GENERATE KEYS
# ==========================================

with tab_keys:

    st.markdown("""
    <div class="page-intro">
        <div class="page-icon">🔑</div>
        <div>
            <h2>Generate Security Keys</h2>
            <p>Create your RSA-3072 public and private key pair.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):

        st.markdown("#### Private Key Protection")

        st.caption(
            "Set a strong passphrase to protect your private key."
        )

        password = st.text_input(
            "Private key passphrase",
            type="password",
            placeholder="Enter a strong passphrase",
            key="key_password"
        )

        if st.button(
            "✦ Generate RSA-3072 Key Pair",
            type="primary",
            use_container_width=True
        ):
            try:
                with st.spinner("Generating secure key pair..."):
                    keypair = core.generate_keypair(
                        password.encode() or None
                    )

                st.session_state.generated_keypair = keypair
                st.session_state.show_public_key = False
                st.session_state.show_private_key = False

                st.success("RSA key pair generated successfully!")

            except core.SDSPError as e:
                st.error(f"[{e.status}] {e}")

            except Exception:
                st.error("Key generation failed. Please try again.")

    if st.session_state.generated_keypair is not None:

        priv, pub = st.session_state.generated_keypair

        st.markdown("### Your Generated Keys")

        st.markdown(
            f'<div class="fingerprint">PUBLIC KEY FINGERPRINT<br>'
            f'<strong>{core.fingerprint(pub)}</strong></div>',
            unsafe_allow_html=True
        )

        public_col, private_col = st.columns(2, gap="large")

        with public_col:
            with st.container(border=True):

                st.markdown("#### 🌐 Public Key")
                st.caption("Share this key with people sending you files.")

                if st.button(
                    "Show / Hide Public Key",
                    key="public_toggle",
                    use_container_width=True
                ):
                    st.session_state.show_public_key = (
                        not st.session_state.show_public_key
                    )

                if st.session_state.show_public_key:
                    st.code(pub.decode("ascii"))
                else:
                    st.info("Public key is hidden.")

                st.download_button(
                    "⬇ Download Public Key",
                    data=pub,
                    file_name="recipient.public.pem",
                    mime="application/x-pem-file",
                    use_container_width=True
                )

        with private_col:
            with st.container(border=True):

                st.markdown("#### 🔐 Private Key")
                st.caption("SECRET — Never share this key.")

                if st.button(
                    "Show / Hide Private Key",
                    key="private_toggle",
                    use_container_width=True
                ):
                    st.session_state.show_private_key = (
                        not st.session_state.show_private_key
                    )

                if st.session_state.show_private_key:
                    st.warning("You are displaying your secret key.")
                    st.code(priv.decode("ascii"))
                else:
                    st.success("Private key is hidden.")

                st.download_button(
                    "⬇ Download Private Key (SECRET)",
                    data=priv,
                    file_name="recipient.private.pem",
                    mime="application/x-pem-file",
                    use_container_width=True
                )


# ==========================================
# ENCRYPT FILE
# ==========================================

with tab_encrypt:

    st.markdown("""
    <div class="page-intro">
        <div class="page-icon">🔒</div>
        <div>
            <h2>Encrypt Your Document</h2>
            <p>Protect your documents using the recipient's public key.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):

        st.markdown("#### Step 1 — Upload Document")

        uploaded_file = st.file_uploader(
            "Choose the document you want to protect",
            key="plain"
        )

        if uploaded_file:
            st.success(f"Selected: {uploaded_file.name}")
            st.caption(
                f"File size: {uploaded_file.size / 1024:.2f} KB"
            )

        st.divider()

        st.markdown("#### Step 2 — Upload Recipient Public Key")

        public_key_file = st.file_uploader(
            "Upload recipient public key (.pem)",
            type=["pem"],
            key="pub"
        )

        if public_key_file:
            st.success("Recipient public key uploaded.")

        st.divider()

        if st.button(
            "🔒 Encrypt Document",
            type="primary",
            use_container_width=True
        ):

            if not uploaded_file or not public_key_file:
                st.warning("Please upload both required files.")

            else:
                try:
                    with st.spinner("Encrypting document..."):

                        package = core.encrypt_bytes(
                            uploaded_file.getvalue(),
                            public_key_file.getvalue(),
                            uploaded_file.name
                        )

                    st.success("Document encrypted successfully!")

                    st.markdown("""
                    <div class="success-panel">
                        <div class="success-icon">✓</div>
                        <div>
                            <h3>Encryption Complete</h3>
                            <p>Your protected document is ready.</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.download_button(
                        "⬇ Download Encrypted Package",
                        data=package,
                        file_name=uploaded_file.name + ".sdsp",
                        mime="application/octet-stream",
                        type="primary",
                        use_container_width=True
                    )

                except core.SDSPError as e:
                    st.error(f"[{e.status}] {e}")

                except Exception:
                    st.error("Encryption failed. Verify your files.")


# ==========================================
# DECRYPT FILE
# ==========================================

with tab_decrypt:

    st.markdown("""
    <div class="page-intro">
        <div class="page-icon">🔓</div>
        <div>
            <h2>Decrypt Your Document</h2>
            <p>Recover your original document using your private key.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):

        st.markdown("#### Step 1 — Upload Encrypted Package")

        encrypted_file = st.file_uploader(
            "Select encrypted package (.sdsp)",
            key="pkg"
        )

        if encrypted_file:
            st.success(f"Package selected: {encrypted_file.name}")

        st.divider()

        st.markdown("#### Step 2 — Upload Your Private Key")

        private_key_file = st.file_uploader(
            "Select your private key (.pem)",
            type=["pem"],
            key="priv"
        )

        if private_key_file:
            st.success("Private key uploaded.")

        password2 = st.text_input(
            "Private key passphrase",
            type="password",
            key="pw2",
            placeholder="Enter your private key passphrase"
        )

        st.divider()

        if st.button(
            "🔓 Decrypt Document",
            type="primary",
            use_container_width=True
        ):

            if not encrypted_file or not private_key_file:
                st.warning("Please upload both required files.")

            else:
                try:
                    with st.spinner("Verifying and decrypting..."):

                        data, original_name = core.decrypt_bytes(
                            encrypted_file.getvalue(),
                            private_key_file.getvalue(),
                            password2.encode() or None
                        )

                    st.success(
                        "Authenticity verified. Decryption successful!"
                    )

                    st.markdown("""
                    <div class="success-panel">
                        <div class="success-icon">✓</div>
                        <div>
                            <h3>Decryption Complete</h3>
                            <p>Your original document is ready to download.</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.download_button(
                        "⬇ Download Original Document",
                        data=data,
                        file_name=original_name or "decrypted_file",
                        mime="application/octet-stream",
                        type="primary",
                        use_container_width=True
                    )

                except core.SDSPError as e:
                    st.error(f"[{e.status}] {e}")

                except Exception:
                    st.error(
                        "Decryption failed. Check your key and passphrase."
                    )


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    <div class="footer-brand">🔐 SecureVault</div>
    <p>Secure Document Sharing System</p>
    <p>Built with Python · Streamlit · Cryptography</p>
    <div class="footer-line"></div>
    <small>Educational Prototype | Protect your digital documents.</small>
</div>
""", unsafe_allow_html=True)

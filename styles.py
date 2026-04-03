"""
UI Styles module for AI Finance Tracker.

This module contains all CSS styling definitions for the Streamlit application.
Centralizing styles improves maintainability and allows for easy theme customization.
"""

from config import (
    COLOR_PRIMARY_BG, COLOR_SECONDARY_BG, COLOR_TERTIARY_BG,
    COLOR_ACCENT_PRIMARY, COLOR_ACCENT_SECONDARY,
    COLOR_SUCCESS, COLOR_DANGER, COLOR_TEXT_PRIMARY, COLOR_TEXT_SECONDARY,
    COLOR_TEXT_MUTED, COLOR_BORDER
)

# ============================================================================
# MAIN APPLICATION STYLES
# ============================================================================
MAIN_APP_STYLE = f"""
<style>
/* Color Palette Variables */
:root {{
    --bg-primary: {COLOR_PRIMARY_BG};
    --bg-secondary: {COLOR_SECONDARY_BG};
    --bg-tertiary: {COLOR_TERTIARY_BG};
    --accent-primary: {COLOR_ACCENT_PRIMARY};
    --accent-secondary: {COLOR_ACCENT_SECONDARY};
    --success: {COLOR_SUCCESS};
    --danger: {COLOR_DANGER};
    --text-primary: {COLOR_TEXT_PRIMARY};
    --text-secondary: {COLOR_TEXT_SECONDARY};
}}

/* General header styles with cyan gradient */
.main-header, h1, .stMarkdown h1 {{
    text-align: center;
    background: linear-gradient(135deg, {COLOR_ACCENT_PRIMARY}, {COLOR_ACCENT_SECONDARY});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 0rem;
    margin-top: 0rem;
    letter-spacing: 1px;
    text-shadow: 1.5px 2px 10px rgba(0, 209, 255, 0.3), 5px 2px 0px rgba(99, 102, 241, 0.2);
}}

.sub-header, h2, .stMarkdown h2 {{
    text-align: center;
    background: linear-gradient(135deg, {COLOR_ACCENT_PRIMARY}, {COLOR_ACCENT_SECONDARY});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 600;
    font-size: 1.7rem;
    margin-bottom: 3rem;
    padding: 0.2em 0 0.1em 0;
    letter-spacing: 0.7px;
    border-bottom: 2px solid {COLOR_ACCENT_PRIMARY};
}}

h3, .stMarkdown h3 {{
    color: {COLOR_ACCENT_PRIMARY};
    font-weight: 500;
    font-size: 1.18rem;
    margin-bottom: 0.7rem;
    letter-spacing: 0.6px;
    text-shadow: 0 0 10px rgba(0, 209, 255, 0.4);
    padding-left: 0.6em;
    border-left: 3px solid {COLOR_ACCENT_SECONDARY};
}}

/* Button styling with cyan gradient */
.stButton > button {{
    background: linear-gradient(135deg, {COLOR_ACCENT_PRIMARY}, {COLOR_ACCENT_SECONDARY});
    color: {COLOR_PRIMARY_BG};
    font-weight: 600;
    border: none;
    border-radius: 8px;
    box-shadow: 0 0 20px rgba(0, 209, 255, 0.5);
    transition: all 0.3s ease;
}}

.stButton > button:hover {{
    box-shadow: 0 0 30px rgba(0, 209, 255, 0.8), 0 0 40px rgba(99, 102, 241, 0.6);
    transform: translateY(-2px);
}}

/* Card/Container styling */
.stContainer, [data-testid="column"] {{
    background-color: {COLOR_TERTIARY_BG} !important;
    border-radius: 12px;
    padding: 1.5rem;
    border: 1px solid rgba(0, 209, 255, 0.2);
}}

/* Sidebar styling - darker background */
[data-testid="stSidebar"] {{
    background-color: {COLOR_SECONDARY_BG} !important;
}}
</style>
"""

# ============================================================================
# LOGIN PAGE STYLES
# ============================================================================
LOGIN_PAGE_STYLE = f"""
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}

html, body, [data-testid="stAppViewContainer"] {{
    background: {COLOR_PRIMARY_BG} !important;
}}

.block-container {{
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px;
}}

section.main > div {{
    padding-top: 0 !important;
}}

.background-glow {{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(0, 209, 255, 0.04) 0%, rgba(99, 102, 241, 0.02) 50%, transparent 100%);
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
}}

.hero-section {{
    width: 100%;
    max-width: 900px;
    margin: 2.5rem auto;
    padding: 0 1rem;
    text-align: center;
    animation: fadeInDown 0.6s ease-out;
    display: flex;
    flex-direction: column;
    align-items: center;
}}

.hero-title {{
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, {COLOR_ACCENT_PRIMARY} 0%, {COLOR_ACCENT_SECONDARY} 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 auto 0.3rem auto;
    letter-spacing: -0.5px;
    width: 100%;
}}

.hero-subtitle {{
    font-size: 0.95rem;
    color: {COLOR_TEXT_SECONDARY};
    max-width: 500px;
    margin: 0 auto;
    padding: 0 1rem;
    font-weight: 400;
    line-height: 1.5;
    text-align: center;
    width: 100%;
}}

.card-title {{
    font-size: 1.4rem;
    font-weight: 700;
    color: {COLOR_TEXT_PRIMARY};
    margin-bottom: 0.25rem;
    text-align: center;
}}

.card-subtitle {{
    font-size: 0.85rem;
    color: {COLOR_TEXT_MUTED};
    text-align: center;
    margin-bottom: 1.5rem;
}}

/* Style Streamlit container for card effect */
[data-testid="stVerticalBlockBorderWrapper"] {{
    background: {COLOR_SECONDARY_BG} !important;
    border: 1px solid rgba(0, 209, 255, 0.15) !important;
    border-radius: 14px !important;
    padding: 2rem !important;
    box-shadow: 0 15px 50px rgba(0, 209, 255, 0.08) !important;
}}

/* Style input fields */
input {{
    background: {COLOR_TERTIARY_BG} !important;
    color: {COLOR_TEXT_PRIMARY} !important;
    border: 1.5px solid {COLOR_BORDER} !important;
    border-radius: 8px !important;
    padding: 0.85rem 1rem !important;
    font-size: 0.95rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}}

input::placeholder {{
    color: {COLOR_TEXT_MUTED} !important;
}}

input:focus {{
    border-color: {COLOR_ACCENT_PRIMARY} !important;
    box-shadow: 0 0 0 3px rgba(0, 209, 255, 0.1) !important;
}}

/* Style buttons */
button {{
    font-weight: 600 !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    border-radius: 8px !important;
}}

.btn-primary {{
    background: linear-gradient(135deg, {COLOR_ACCENT_PRIMARY} 0%, {COLOR_ACCENT_SECONDARY} 100%) !important;
    color: {COLOR_PRIMARY_BG} !important;
    border: none !important;
}}

.btn-primary:hover {{
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(0, 209, 255, 0.3) !important;
}}

.divider-container {{
    margin: 1.3rem 0;
    display: flex;
    align-items: center;
    gap: 1rem;
}}

.divider-line {{
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, {COLOR_BORDER}, transparent);
}}

.divider-text {{
    color: {COLOR_TEXT_MUTED};
    font-size: 0.8rem;
    font-weight: 500;
}}

.google-btn {{
    width: 100%;
    padding: 0.85rem 1rem;
    background: {COLOR_TERTIARY_BG} !important;
    border: 1.5px solid {COLOR_BORDER} !important;
    border-radius: 8px !important;
    color: {COLOR_TEXT_PRIMARY} !important;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}}

.google-btn:hover {{
    background: #2C3A4A !important;
    border-color: {COLOR_ACCENT_SECONDARY} !important;
    transform: translateY(-2px);
}}

.auth-toggle {{
    text-align: center;
    margin-top: 1.2rem;
    font-size: 0.85rem;
    color: {COLOR_TEXT_SECONDARY};
}}

.auth-toggle-link {{
    color: {COLOR_ACCENT_PRIMARY};
    cursor: pointer;
    font-weight: 600;
    transition: color 0.2s;
}}

.auth-toggle-link:hover {{
    color: {COLOR_ACCENT_SECONDARY};
}}

.features-section {{
    margin-top: 2.5rem;
    text-align: center;
}}

.features-heading {{
    font-size: 1.3rem;
    font-weight: 700;
    color: {COLOR_TEXT_PRIMARY};
    margin-bottom: 0.3rem;
}}

.features-subheading {{
    font-size: 0.9rem;
    color: {COLOR_TEXT_SECONDARY};
    margin-bottom: 1.8rem;
}}

.features-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.3rem;
    max-width: 900px;
    margin: 0 auto;
}}

.feature-card {{
    background: {COLOR_SECONDARY_BG};
    border: 1px solid rgba(0, 209, 255, 0.1);
    border-radius: 10px;
    padding: 1.5rem;
    text-align: center;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    animation: fadeInUp 0.6s ease-out backwards;
}}

.feature-card:nth-child(1) {{ animation-delay: 0.2s; }}
.feature-card:nth-child(2) {{ animation-delay: 0.25s; }}
.feature-card:nth-child(3) {{ animation-delay: 0.3s; }}

.feature-card:hover {{
    background: {COLOR_TERTIARY_BG};
    border-color: {COLOR_ACCENT_PRIMARY};
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(0, 209, 255, 0.1);
}}

.feature-icon {{
    font-size: 2.2rem;
    margin-bottom: 0.8rem;
    transition: transform 0.3s;
}}

.feature-card:hover .feature-icon {{
    transform: scale(1.1);
}}

.feature-title {{
    font-size: 1rem;
    font-weight: 700;
    color: {COLOR_TEXT_PRIMARY};
    margin-bottom: 0.4rem;
}}

.feature-desc {{
    color: {COLOR_TEXT_SECONDARY};
    font-size: 0.85rem;
    line-height: 1.5;
}}

@keyframes fadeInDown {{
    from {{
        opacity: 0;
        transform: translateY(-15px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

@keyframes fadeInUp {{
    from {{
        opacity: 0;
        transform: translateY(15px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

@media (max-width: 768px) {{
    .hero-title {{ font-size: 1.8rem; }}
    .hero-subtitle {{ font-size: 0.9rem; }}
    .features-grid {{ grid-template-columns: 1fr; }}
}}
</style>
"""

# ============================================================================
# DASHBOARD STYLES
# ============================================================================
DASHBOARD_STYLE = f"""
<style>
.hero-container {{
    text-align: center;
    padding: 3rem 2rem;
    background: linear-gradient(135deg, {COLOR_PRIMARY_BG} 0%, {COLOR_TERTIARY_BG} 50%, {COLOR_SECONDARY_BG} 100%);
    border-radius: 16px;
    margin-bottom: 2rem;
    border: 1px solid rgba(0, 209, 255, 0.1);
}}
.hero-title {{
    background: linear-gradient(135deg, {COLOR_ACCENT_PRIMARY} 0%, {COLOR_ACCENT_SECONDARY} 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 3rem;
    font-weight: 800;
    margin: 0 0 1rem 0;
    letter-spacing: -1px;
}}
.hero-subtitle {{
    color: {COLOR_TEXT_SECONDARY};
    font-size: 1.1rem;
    margin-bottom: 2rem;
    font-weight: 400;
}}
.card {{
    background: linear-gradient(135deg, {COLOR_TERTIARY_BG} 0%, {COLOR_SECONDARY_BG} 100%);
    border: 1px solid rgba(0, 209, 255, 0.15);
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}}
.card:hover {{
    transform: translateY(-8px);
    border-color: rgba(0, 209, 255, 0.4);
    box-shadow: 0 20px 40px rgba(0, 209, 255, 0.15);
}}
.card-label {{
    color: {COLOR_TEXT_SECONDARY};
    font-size: 0.9rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.5rem;
}}
.card-value {{
    color: {COLOR_TEXT_PRIMARY};
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}}
.card-change {{
    font-size: 0.85rem;
}}
.card-change.positive {{ color: {COLOR_SUCCESS}; }}
.card-change.negative {{ color: {COLOR_DANGER}; }}
.chart-container {{
    background: linear-gradient(135deg, {COLOR_TERTIARY_BG} 0%, {COLOR_SECONDARY_BG} 100%);
    border: 1px solid rgba(0, 209, 255, 0.15);
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s ease;
}}
.chart-title {{
    color: {COLOR_TEXT_PRIMARY};
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 1rem;
}}
</style>
"""

# ============================================================================
# GLOWING DIVIDER STYLES
# ============================================================================
GLOWING_DIVIDER = """
<hr style="
    border: none;
    height: 2px;
    background: linear-gradient(
        90deg,
        transparent,
        #00D1FF,
        #6366F1,
        transparent
    );
    margin: 25px 0;
    opacity: 0.7;
    box-shadow: 0 0 15px rgba(0, 209, 255, 0.4);
">
"""


def get_page_config():
    """Get Streamlit page configuration."""
    return {
        'page_title': 'AI Finance Tracker',
        'layout': 'wide',
        'initial_sidebar_state': 'expanded'
    }

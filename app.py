from pathlib import Path
import re

import streamlit as st
import streamlit.components.v1 as components


ROOT = Path(__file__).parent

STYLE_OPTIONS = {
    "style1": {
        "label": "Style 1 - Original",
        "path": ROOT / "style1",
    },
    "style2": {
        "label": "Style 2 - Premium Blue",
        "path": ROOT / "style2",
    },
    "style3": {
        "label": "Style 3 - SaaS Clean",
        "path": ROOT / "style3",
    },
    "style4": {
        "label": "Style 4 - Immersive Split Grid",
        "path": ROOT / "style4",
    },
}
LABEL_TO_STYLE = {option["label"]: key for key, option in STYLE_OPTIONS.items()}
PAGE_FILES = {
    "index": "index.html",
    "our-services": "our-services.html",
    "event": "event.html",
}

st.set_page_config(page_title="42one95 Style Preview", layout="wide")
st.sidebar.title("42one95 Styles")

query_style = st.query_params.get("style", "style1")
query_page = st.query_params.get("page", "index")
query_anchor = st.query_params.get("anchor", "")

active_style = query_style if query_style in STYLE_OPTIONS else "style1"
active_page = query_page if query_page in PAGE_FILES else "index"

selected_style = st.sidebar.radio(
    "เลือกสไตล์ที่ต้องการตรวจ:",
    [option["label"] for option in STYLE_OPTIONS.values()],
    index=list(STYLE_OPTIONS).index(active_style),
)

selected_style_key = LABEL_TO_STYLE[selected_style]
file_to_open = STYLE_OPTIONS[selected_style_key]["path"] / PAGE_FILES[active_page]

def internal_url(href, style_key):
    if not href or href.startswith(("#", "mailto:", "tel:")) or re.match(r"^https?://", href):
        return None

    path, _, anchor = href.replace("./", "", 1).partition("#")
    filename = Path(path or "index.html").name
    page_key = next((key for key, value in PAGE_FILES.items() if value == filename), None)
    if page_key is None:
        return None

    url = f"?style={style_key}&page={page_key}"
    if anchor:
        url += f"&anchor={anchor}"
    return url

def rewrite_internal_links(html_content, style_key):
    def replace_anchor(match):
        before_href, href, after_href = match.groups()
        url = internal_url(href, style_key)
        if url is None:
            return match.group(0)

        attrs = f'{before_href}href="{url}"{after_href}'
        if "target=" not in attrs:
            attrs += ' target="_parent"'
        return f"<a{attrs}>"

    return re.sub(r'<a\b([^>]*?)href="([^"]+)"([^>]*)>', replace_anchor, html_content)

def build_preview_html(file_path, style_key, anchor):
    html_content = rewrite_internal_links(file_path.read_text(encoding="utf-8"), style_key)
    if not anchor:
        return html_content

    scroll_script = f"""
    <script>
    (() => {{
        const target = {anchor!r};
        requestAnimationFrame(() => {{
            document.getElementById(target)?.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        }});
    }})();
    </script>
    """
    return html_content.replace("</body>", f"{scroll_script}\n</body>", 1)

try:
    html_content = build_preview_html(file_to_open, selected_style_key, query_anchor)
    components.html(html_content, height=3200, scrolling=True)
except FileNotFoundError:
    st.error(f"ไม่พบไฟล์ {file_to_open}")

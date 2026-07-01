from pathlib import Path
import json

import streamlit as st
import streamlit.components.v1 as components


ROOT = Path(__file__).parent

STYLE_FILES = {
    "Style 1 - Original": ROOT / "style1" / "index.html",
    "Style 2 - Premium Blue": ROOT / "style2" / "index.html",
    "Style 3 - SaaS Clean": ROOT / "style3" / "index.html",
    "Style 4 - Immersive Split Grid": ROOT / "style4" / "index.html",
}

st.set_page_config(page_title="42one95 Style Preview", layout="wide")
st.sidebar.title("42one95 Styles")

selected_style = st.sidebar.radio(
    "เลือกสไตล์ที่ต้องการตรวจ:",
    tuple(STYLE_FILES.keys()),
)

file_to_open = STYLE_FILES[selected_style]

def build_preview_html(file_path):
    page_files = [file_path.parent / "index.html", file_path.parent / "our-services.html", file_path.parent / "event.html"]
    pages = {
        page.name: page.read_text(encoding="utf-8")
        for page in page_files
        if page.exists()
    }
    html_content = pages[file_path.name]
    pages_json = json.dumps(pages, ensure_ascii=False).replace("</", "<\\/")
    router_script = f"""
    <script>
    (() => {{
        const pages = {pages_json};

        function routeKey(rawHref) {{
            if (!rawHref || rawHref.startsWith('#') || rawHref.startsWith('mailto:') || rawHref.startsWith('tel:')) return null;
            if (/^https?:\\/\\//i.test(rawHref)) return null;

            const href = rawHref.replace(/^\\.\\//, '');
            const [path, hash = ''] = href.split('#');
            const key = path.split('/').pop() || 'index.html';

            return pages[key] ? {{ key, hash }} : null;
        }}

        function renderPage(key, hash = '') {{
            const parsed = new DOMParser().parseFromString(pages[key], 'text/html');
            document.title = parsed.title || document.title;
            document.head.innerHTML = parsed.head.innerHTML;
            document.body.innerHTML = parsed.body.innerHTML;
            window.scrollTo(0, 0);

            if (hash) {{
                requestAnimationFrame(() => {{
                    document.getElementById(hash)?.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }});
            }}
        }}

        document.addEventListener('click', (event) => {{
            const link = event.target.closest('a[href]');
            if (!link) return;

            const route = routeKey(link.getAttribute('href'));
            if (!route) return;

            event.preventDefault();
            renderPage(route.key, route.hash);
        }});
    }})();
    </script>
    """
    return html_content.replace("</body>", f"{router_script}\n</body>", 1)

try:
    html_content = build_preview_html(file_to_open)
    components.html(html_content, height=3200, scrolling=True)
except FileNotFoundError:
    st.error(f"ไม่พบไฟล์ {file_to_open}")

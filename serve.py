from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
import posixpath
import urllib.parse

ROOT = Path(__file__).resolve().parent
APP_DIR = ROOT / "Let Glory Manifest"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def translate_path(self, path):
        parsed = urllib.parse.urlparse(path)
        path = urllib.parse.unquote(parsed.path)
        path = posixpath.normpath(path)

        # Serve the app entry point from the project root
        if path == "/":
            return str(ROOT / "index.html")

        # Rewrite asset URLs to point to the Let Glory Manifest subdirectory
        if path.startswith("/assets/"):
            path = "/Let Glory Manifest" + path
        elif path.startswith("/__l5e/"):
            path = "/Let Glory Manifest" + path
        elif path.startswith("/Let Glory Manifest/"):
            pass  # Keep as-is
        else:
            # Unknown path — check if it's a static file, else SPA fallback
            if self._is_static_resource(path):
                path = path.lstrip("/")
                return str((ROOT / path).resolve())
            else:
                # SPA fallback: serve index.html for client-side routing
                return str(ROOT / "index.html")

        # Normalize to the actual filesystem path
        path = path.lstrip("/")
        return str((ROOT / path).resolve())

    def _is_static_resource(self, path):
        """Check if the path looks like a request for a static resource."""
        ext = posixpath.splitext(path)[1].lower()
        return ext in (".js", ".css", ".png", ".jpg", ".jpeg", ".gif", ".svg",
                       ".ico", ".woff", ".woff2", ".ttf", ".eot", ".webp",
                       ".json", ".map", ".txt", ".mp4", ".webm", ".pdf",
                       ".doc", ".docx") or "/assets/" in path or "/__l5e/" in path


if __name__ == "__main__":
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"Serving on http://localhost:{port}")
    server.serve_forever()

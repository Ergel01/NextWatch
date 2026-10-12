import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser(description="Run the NextWatch movie app locally.")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    handler = partial(SimpleHTTPRequestHandler, directory=str(PROJECT_ROOT))
    with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print(f"NextWatch is running at http://127.0.0.1:{args.port}")
        print("Press Ctrl+C to stop the server.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
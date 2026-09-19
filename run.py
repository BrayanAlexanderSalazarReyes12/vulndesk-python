from vulndesk.app import create_app

app = create_app()

if __name__ == "__main__":
    print("VulnDesk Python LAB running on http://localhost:5000")
    print("WARNING: intentionally vulnerable training application.")
    app.run(host="127.0.0.1", port=5000, debug=False)

import argparse
import jinja2
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Nikto HTML Wrapper")
    parser.add_argument("-i", "--input", required=True, help="Target list file")
    parser.add_argument("-o", "--output", required=True, help="Output HTML file")
    args = parser.parse_args()

    with open(args.input, "r") as f:
        targets = [line.strip() for line in f if line.strip()]

    results = []
    for target in targets:
        print(f"Scanning: {target}")
        result = subprocess.run(["nikto", "-h", target], capture_output=True, text=True)
        results.append({"target": target, "output": result.stdout})

    template = jinja2.Template(\"\"\"
    <html><body><h1>Nikto Report</h1>
    {% for item in results %}
      <h2>{{ item.target }}</h2>
      <pre>{{ item.output }}</pre>
    {% endfor %}
    </body></html>
    \"\"\")
    
    with open(args.output, "w") as f:
        f.write(template.render(results=results))

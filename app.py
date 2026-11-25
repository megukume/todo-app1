from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = [
    {"text": "Pythonを勉強する", "done": False},
    {"text": "レポートを書く", "done": False},
    {"text": "GitHubを触る", "done": False}
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        todos=todos
    )


@app.route("/add", methods=["POST"])
def add():
    todo = request.form["todo"]

    if todo:
        todos.append({
            "text": todo,
            "done": False
        })

    return redirect("/")

@app.route("/toggle/<int:index>")
def toggle(index):

    if 0 <= index < len(todos):
        todos[index]["done"] = not todos[index]["done"]

    return redirect("/")


@app.route("/delete/<int:index>")
def delete(index):

    if 0 <= index < len(todos):
        todos.pop(index)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
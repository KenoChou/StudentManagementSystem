from guizero import App, Text, TextBox, PushButton, Box
import time

# =========================
# DATA
# =========================
students = []

# =========================
# GRADE
# =========================
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# =========================
# ADD
# =========================
def add_student():
    name = name_input.value.strip()
    score = score_input.value.strip()

    if not name or not score:
        status.value = "❌ Please fill all fields"
        return

    if not score.isdigit():
        status.value = "❌ Score must be number"
        return

    score = int(score)

    students.append({
        "name": name,
        "score": score,
        "grade": get_grade(score)
    })

    status.value = f"✅ Added {name}"
    name_input.value = ""
    score_input.value = ""


# =========================
# SHOW
# =========================
def show_students():
    if not students:
        status.value = "No students"
        return

    text = "📚 Student List\n────────────\n"
    for i, s in enumerate(students):
        text += f"{i+1}. {s['name']} | Score: {s['score']} | Grade: {s['grade']}\n"

    status.value = text


# =========================
# SEARCH
# =========================
def search_student():
    keyword = name_input.value.strip().lower()

    results = [s for s in students if keyword in s["name"].lower()]

    if not results:
        status.value = "🔍 No match found"
        return

    text = "🔍 Search Result\n────────────\n"
    for i, s in enumerate(results):
        text += f"{i+1}. {s['name']} | {s['score']} | {s['grade']}\n"

    status.value = text


# =========================
# DELETE
# =========================
def delete_student():
    keyword = name_input.value.strip().lower()

    for s in students:
        if s["name"].lower() == keyword:
            students.remove(s)
            status.value = f"🗑 Deleted {s['name']}"
            return

    status.value = "❌ Not found"


# =========================
# RANKING
# =========================
def show_ranking():
    if not students:
        status.value = "No students"
        return

    sorted_list = sorted(students, key=lambda x: x["score"], reverse=True)

    text = "🏆 Ranking\n────────────\n"
    for i, s in enumerate(sorted_list):
        text += f"{i+1}. {s['name']} | {s['score']} | {s['grade']}\n"

    status.value = text


# =========================
# STATISTICS
# =========================
def show_statistics():
    if not students:
        status.value = "No data"
        return

    scores = [s["score"] for s in students]

    status.value = (
        "📊 Statistics\n────────────\n"
        f"Average: {sum(scores)/len(scores):.2f}\n"
        f"Highest: {max(scores)}\n"
        f"Lowest: {min(scores)}\n"
        f"Total: {len(scores)}"
    )


# =========================
# GUI
# =========================
app = App("Student System", width=560, height=700, bg="#eef1f6")

Text(app, "Student Management System", size=18, color="#1f2d3d")

main = Box(app, layout="vertical")

# ================= INPUT =================
input_box = Box(main, width="fill")

Text(input_box, "INPUT", color="#555555")

Text(input_box, "Name")
name_input = TextBox(input_box, width=30)
name_input.tk.config(
    bg="white",
    fg="black",
    insertbackground="black"
)

Text(input_box, "Score")
score_input = TextBox(input_box, width=30)
score_input.tk.config(
    bg="white",
    fg="black",
    insertbackground="black"
)

# ================= BUTTONS =================
btn_box = Box(main, width="fill")

Text(btn_box, "ACTIONS", color="#555555")

PushButton(btn_box, text="Add", command=add_student, width=20)
PushButton(btn_box, text="Show", command=show_students, width=20)
PushButton(btn_box, text="Search", command=search_student, width=20)
PushButton(btn_box, text="Delete", command=delete_student, width=20)
PushButton(btn_box, text="Ranking", command=show_ranking, width=20)
PushButton(btn_box, text="Stats", command=show_statistics, width=20)

# ================= OUTPUT =================
output = Box(app, width="fill", height=300, border=1)

Text(output, "OUTPUT", color="#555555")

status = Text(output, text="Ready")

app.display()
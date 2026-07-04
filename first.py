from guizero import App, Text, TextBox, PushButton, Box

# =========================
# DATA STRUCTURE
# =========================
students = []

# =========================
# UTIL: GRADE SYSTEM
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
# ADD STUDENT
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
# SHOW ALL
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
# SEARCH (Linear Search O(n))
# =========================
def search_student():
    keyword = name_input.value.strip().lower()

    if not keyword:
        status.value = "❌ Enter name to search"
        return

    results = []
    for s in students:
        if keyword in s["name"].lower():
            results.append(s)

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

    if not keyword:
        status.value = "❌ Enter name to delete"
        return

    for s in students:
        if s["name"].lower() == keyword:
            students.remove(s)
            status.value = f"🗑 Deleted {s['name']}"
            return

    status.value = "❌ Not found"


# =========================
# SORT / RANKING (O(n log n))
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

    avg = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)

    text = (
        "📊 Statistics\n────────────\n"
        f"Average: {avg:.2f}\n"
        f"Highest: {max_score}\n"
        f"Lowest: {min_score}\n"
        f"Total: {len(students)}"
    )

    status.value = text


# =========================
# GUI
# =========================
app = App("Student Score System", width=560, height=620, bg="#eef1f6")

Text(app, "Student Score Management System", size=18, color="#1f2d3d")

main = Box(app, layout="grid", width="fill", height=220)

# INPUT
input_box = Box(main, grid=[0, 0], width=260, height=200)
Text(input_box, "INPUT", color="#555555")

Text(input_box, "Name")
name_input = TextBox(input_box, width=25)
name_input.tk.config(fg="black", bg="white", insertbackground="black")

Text(input_box, "Score")
score_input = TextBox(input_box, width=25)
score_input.tk.config(fg="black", bg="white", insertbackground="black")

# BUTTONS
btn_box = Box(main, grid=[1, 0], width=260, height=200)
Text(btn_box, "ACTIONS", color="#555555")

PushButton(btn_box, text="➕ Add", command=add_student, width=14)
PushButton(btn_box, text="📋 Show All", command=show_students, width=14)
PushButton(btn_box, text="🔍 Search", command=search_student, width=14)
PushButton(btn_box, text="🗑 Delete", command=delete_student, width=14)
PushButton(btn_box, text="🏆 Ranking", command=show_ranking, width=14)
PushButton(btn_box, text="📊 Statistics", command=show_statistics, width=14)

# OUTPUT
output_box = Box(app, width="fill", height=320, border=1)
Text(output_box, "OUTPUT", color="#555555")

status = Text(output_box, text="Ready", size=10, color="black")

app.display()
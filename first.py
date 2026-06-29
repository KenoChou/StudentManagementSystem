from guizero import App, Text, TextBox, PushButton, Box

students = []

# ===== logic =====
def add_student():
    name = name_input.value.strip()
    age = age_input.value.strip()

    if not name or not age:
        status.value = "❌ Fill all fields"
        return

    if not age.isdigit():
        status.value = "❌ Age must be number"
        return

    students.append({"name": name, "age": int(age)})
    status.value = f"✅ Added {name}"

    name_input.value = ""
    age_input.value = ""


def show_students():
    if not students:
        status.value = "No students"
        return

    text = "📚 Students\n────────────\n"
    for i, s in enumerate(students):
        text += f"{i+1}. {s['name']} ({s['age']})\n"

    status.value = text


def delete_student():
    name = name_input.value.strip()

    for s in students:
        if s["name"] == name:
            students.remove(s)
            status.value = f"🗑 Deleted {name}"
            return

    status.value = "❌ Not found"


# ===== APP =====
app = App("Student Manager", width=540, height=600, bg="#eef1f6")

Text(app, "Student Management System", size=18, color="#1f2d3d")


# =========================
# MAIN LAYOUT
# =========================
main = Box(app, layout="grid", width="fill", height=220)


# ===== INPUT =====
input_box = Box(main, grid=[0, 0], width=260, height=200)

Text(input_box, "INPUT", color="#555555")

Text(input_box, "Name", color="#333333")
name_input = TextBox(input_box, width=25)

# ✅ 强制修复输入框可见性（关键）
name_input.tk.config(
    fg="black",
    bg="white",
    insertbackground="black"
)

Text(input_box, "Age", color="#333333")
age_input = TextBox(input_box, width=25)

# ✅ 同样修复
age_input.tk.config(
    fg="black",
    bg="white",
    insertbackground="black"
)


# ===== BUTTONS =====
btn_box = Box(main, grid=[1, 0], width=220, height=200)

Text(btn_box, "ACTIONS", color="#555555")

PushButton(btn_box, text="➕ Add", command=add_student, width=12)
PushButton(btn_box, text="📋 Show", command=show_students, width=12)
PushButton(btn_box, text="🗑 Delete", command=delete_student, width=12)


# ===== OUTPUT =====
output_box = Box(app, width="fill", height=300, border=1)

Text(output_box, "OUTPUT", color="#555555")

status = Text(output_box, text="Ready", size=10, color="black")


app.display()
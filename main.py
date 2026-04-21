import PyPDF2

# STEP 1: Extract text from PDF
def extract_text(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

# STEP 2: Load resume safely
try:
    resume_text = extract_text("resume.pdf")
except:
    print("❌ Error: Could not read resume.pdf. Make sure it's a valid PDF.")
    exit()

# STEP 3: Keywords (real-world skills)
keywords = [
    "python", "java", "sql", "machine learning", "data analysis",
    "c++", "javascript", "html", "css", "react", "node",
    "mongodb", "api", "git", "github"
]

# STEP 4: Check skills
def check_keywords(text):
    text = text.lower()
    
    found = []
    missing = []
    
    for word in keywords:
        if word in text:
            found.append(word)
        else:
            missing.append(word)
    
    return found, missing

found, missing = check_keywords(resume_text)

# STEP 5: Score calculation
score = (len(found) / len(keywords)) * 100

# STEP 6: Clean output
print("\n===== RESUME ANALYSIS REPORT =====")

print(f"\n✅ Skills Found ({len(found)}):")
for skill in found:
    print(f" - {skill}")

print(f"\n❌ Skills Missing ({len(missing)}):")
for skill in missing:
    print(f" - {skill}")

print(f"\n📊 Resume Score: {score:.2f}%")

if score >= 70:
    print("🔥 Strong Resume!")
elif score >= 40:
    print("👍 Average — Can Improve")
else:
    print("⚠️ Needs Improvement")

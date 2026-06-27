from flask import Flask, render_template

app = Flask(__name__)

PORTFOLIO = {
    "name": "Vikram Singh",
    "initials": "VS",
    "role": "Cybersecurity Analyst · Ethical Hacker · Penetration Tester",
    "tagline": "Results-driven cybersecurity professional skilled in VAPT, OWASP Top 10, and penetration testing — backed by real-world internship experience and top certifications.",

    "about": [
        "I'm a cybersecurity professional with hands-on experience as a Cyber Security Intern at Codec Technologies (AICTE-approved). I completed an 8-week Internshala Cyber Security training as a Top Performer and earned Grade A in Ethical Hacking with AI from Skill India / NSDC.",
        "Currently pursuing B.Tech in Computer Science at Mewar University while deepening my networking expertise through Cisco Networking Academy. Passionate about securing digital systems and staying ahead of evolving threats.",
    ],
    "facts": [
        {"icon": "📍", "text": "Gorakhpur, UP, India"},
        {"icon": "📧", "text": "vs2577233@gmail.com"},
        {"icon": "🎓", "text": "B.Tech CSE — Mewar University (2024–2028)"},
        {"icon": "🏆", "text": "Internshala Top Performer · Grade A — Skill India"},
    ],

    "skills": [
        {
            "icon": "🔍",
            "name": "Penetration Testing",
            "tools": ["Nmap", "Burpsuite", "Nikto", "OWASP ZAP", "SQLMap", "Kali Linux", "DVWA"],
        },
        {
            "icon": "🔐",
            "name": "Security Domains",
            "tools": ["VAPT", "OWASP Top 10", "Web App Security", "Social Engineering", "Wi-Fi Security", "Malware Analysis"],
        },
        {
            "icon": "🌐",
            "name": "Networking",
            "tools": ["TCP/IP", "DNS", "HTTP/HTTPS", "Cisco Packet Tracer", "VLANs", "WPA2/WPA3"],
        },
        {
            "icon": "💻",
            "name": "Programming & Tools",
            "tools": ["Python", "HTML & CSS", "GitHub Copilot", "MS Excel", "Aircrack-ng", "John the Ripper"],
        },
    ],

    "experience": [
        {
            "role": "Cyber Security Intern",
            "company": "Codec Technologies Pvt. Ltd.",
            "period": "Apr 2026 – May 2026",
            "points": [
                "Performed VAPT on simulated corporate environments",
                "Conducted ethical hacking: SQL injection, XSS, CSRF, password cracking, malware simulation",
                "Wi-Fi security assessment using Aircrack-ng and WPA2 penetration testing",
                "Developed social engineering awareness and controlled phishing simulations",
                "Delivered final security report with full remediation roadmap",
                "Received Letter of Recommendation from Program Manager",
            ],
        }
    ],

   "projects": [
    {
        "title": "Integrated Cybersecurity VAPT",
        "tag": "Full-Scope Pentest",
        "description": "Full-scope 9-phase security assessment for SecureCorp (simulated org) using DVWA. Covered reconnaissance, network/web scanning, SQL injection, XSS/CSRF, password cracking, malware analytics, social engineering, and Wi-Fi penetration testing — with a complete remediation report.",
        "tech": ["Nmap", "Burpsuite", "SQLMap", "OWASP ZAP", "Aircrack-ng", "John the Ripper", "Hashcat", "DVWA"],
        "link": "",
    },
    {
        "title": "Password Strength Checker",
        "tag": "Security Tool",
        "description": "Real-time password analyzer with entropy calculation, estimated crack time (GPU brute force), OWASP-based security checks, and smart recommendations. Built with pure HTML/CSS/JS.",
        "tech": ["HTML", "CSS", "JavaScript", "Cryptography", "Entropy Analysis"],
        "link": "https://github.com/vikram-singh-cyber/2nd-project",
    },
    {
        "title": "Wi-Fi Security Assessment",
        "tag": "Network Security",
        "description": "WPA2 penetration testing using Aircrack-ng and Hashcat with network hardening recommendations including segmentation and WPA3 migration roadmap.",
        "tech": ["Aircrack-ng", "Hashcat", "Kali Linux", "WPA2/WPA3"],
        "link": "",
    },
    {
        "title": "Web App Security Audit",
        "tag": "OWASP Top 10",
        "description": "Manual and automated OWASP Top 10 assessment using Burpsuite and Nikto. Identified and documented vulnerabilities with CVE/CWE references and implemented security headers.",
        "tech": ["Burpsuite", "Nikto", "OWASP ZAP", "CVE/CWE"],
        "link": "",
    },
],

    "certifications": [
        {"name": "Cyber Security Training (8 Weeks) — Top Performer 🏆", "issuer": "Internshala × IITM Pravartak", "date": "Mar 2026"},
        {"name": "Ethical Hacking with AI — Grade A", "issuer": "Scholiverse / Skill India / NSDC", "date": "Mar 2026"},
        {"name": "Ethical Hacking — ICAC Recognized", "issuer": "Codec Technologies", "date": "May 2026"},
        {"name": "Cisco Networking with Packet Tracer 🔄", "issuer": "Cisco Networking Academy", "date": "In Progress"},
        {"name": "Python & GitHub Copilot Masterclass", "issuer": "Simplilearn", "date": "Aug 2025"},
    ],

    "contact": [
    {"icon": "✉️", "label": "vs2577233@gmail.com", "href": "mailto:vs2577233@gmail.com"},
    {"icon": "💼", "label": "LinkedIn", "href": "https://linkedin.com/in/vikram-singh-8b432b364"},
    {"icon": "🐙", "label": "GitHub", "href": "https://github.com/vikram-singh-cyber"},
    {"icon": "📞", "label": "+91 93056 00749", "href": "tel:+919305600749"},
    ],
}


@app.route("/")
def index():
    return render_template("index.html", **PORTFOLIO)


if __name__ == "__main__":
    print("\n🚀  Vikram's Portfolio → http://127.0.0.1:5000\n")
    app.run(debug=True)

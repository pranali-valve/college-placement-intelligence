# =========================================================
# STUDENT INTELLIGENCE
# =========================================================


def analyze_student(student):
    """
    Analyze one student's profile and generate:
    - Strong areas
    - Skill gaps
    - Recommended roles
    - Student status
    """

    strengths = []
    skill_gaps = []
    recommended_roles = []


    # =====================================================
    # STRONG AREAS
    # =====================================================

    if student["cgpa"] >= 8:
        strengths.append("Strong academic performance")
    elif student["cgpa"] < 7:
        skill_gaps.append("Improve CGPA")


    if student["technical_skills"] >= 6:
        strengths.append("Strong technical skills")
    else:
        skill_gaps.append("Improve technical skills")


    if student["internships"] >= 2:
        strengths.append("Good internship experience")
    elif student["internships"] == 0:
        skill_gaps.append("Gain internship experience")


    if student["projects"] >= 3:
        strengths.append("Good project experience")
    elif student["projects"] < 2:
        skill_gaps.append("Build more projects")


    if student["aptitude_score"] >= 75:
        strengths.append("Good aptitude score")
    else:
        skill_gaps.append("Improve aptitude score")


    if student["communication_score"] >= 75:
        strengths.append("Good communication skills")
    else:
        skill_gaps.append("Improve communication skills")


    if student["attendance"] >= 85:
        strengths.append("Good attendance")
    elif student["attendance"] < 75:
        skill_gaps.append("Improve attendance")


    if student["backlogs"] == 0:
        strengths.append("No backlogs")
    else:
        skill_gaps.append("Clear backlogs")


    # =====================================================
    # RECOMMENDED ROLES
    # =====================================================

    if student["technical_skills"] >= 6 and student["projects"] >= 2:
        recommended_roles.append("Software Developer")


    if student["technical_skills"] >= 5 and student["aptitude_score"] >= 70:
        recommended_roles.append("Data Analyst")


    if student["communication_score"] >= 70 and student["aptitude_score"] >= 70:
        recommended_roles.append("Business Analyst")


    if student["technical_skills"] >= 7:
        recommended_roles.append("Machine Learning / AI Engineer")


    if not recommended_roles:
        recommended_roles.append("Graduate Trainee")


    # =====================================================
    # STUDENT STATUS
    # =====================================================

    if student["cgpa"] >= 8 and student["technical_skills"] >= 6:

        if student["backlogs"] == 0 and student["internships"] >= 1:
            status = "Placement Ready"
        else:
            status = "Needs Training"

    elif student["cgpa"] < 6.5 or student["backlogs"] >= 3:

        status = "High Risk"

    else:

        status = "Needs Training"


    # =====================================================
    # RETURN RESULT
    # =====================================================

    return {
        "strengths": strengths,
        "skill_gaps": skill_gaps,
        "recommended_roles": recommended_roles,
        "status": status
    }


# =========================================================
# STATUS FUNCTION FOR ADMIN DASHBOARD
# =========================================================

def get_student_status(student):

    if student["cgpa"] >= 8 and student["technical_skills"] >= 6:

        if student["backlogs"] == 0 and student["internships"] >= 1:
            return "Placement Ready"

        else:
            return "Needs Training"

    elif student["cgpa"] < 6.5 or student["backlogs"] >= 3:

        return "High Risk"

    else:

        return "Needs Training"
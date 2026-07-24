import csv
import os


def get_field(row, aliases):
    for key in aliases:
        if key in row:
            return row[key]
    return None


def main():
    filename = 'grades.csv'
    if not os.path.exists(filename):
        print(f"Error: {filename} not found in the current folder!")
        input("Press Enter to exit...")
        return

    assignments = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row_norm = {
                    (k or '').strip().lower(): v
                    for k, v in row.items()
                }
                try:
                    assignment = get_field(row_norm, ['assignment', 'name']).strip()
                    assign_type = get_field(row_norm, ['type', 'group', 'category']).strip()
                    weight = int(get_field(row_norm, ['weight']))
                    score = int(get_field(row_norm, ['score', 'grade']))
                    if not (0 <= score <= 100):
                        print(f"Warning: Invalid score for {assignment}")
                        continue
                    assignments.append({
                        'Assignment': assignment,
                        'Type': assign_type,
                        'Weight': weight,
                        'Score': score
                    })
                except Exception:
                    continue
    except Exception as e:
        print(f"Error reading file: {e}")
        input("Press Enter to exit...")
        return

    if not assignments:
        print("No valid data found.")
        input("Press Enter to exit...")
        return

    formative = [a for a in assignments if a['Type'].lower() == 'formative']
    summative = [a for a in assignments if a['Type'].lower() == 'summative']

    formative_weight = sum(a['Weight'] for a in formative)
    summative_weight = sum(a['Weight'] for a in summative)
    total_weight = formative_weight + summative_weight

    if formative_weight != 60:
        print(f"Error: Formative weight = {formative_weight}% (must be 60%)")
        input("Press Enter to exit...")
        return

    if summative_weight != 40:
        print(f"Error: Summative weight = {summative_weight}% (must be 40%)")
        input("Press Enter to exit...")
        return

    if total_weight != 100:
        print(f"Error: Total weight = {total_weight}% (must be 100%)")
        input("Press Enter to exit...")
        return

    total_grade = sum(a['Weight'] * a['Score'] for a in assignments) / 100
    gpa = (total_grade / 100) * 5.0

    formative_raw = sum(a['Weight'] * a['Score'] for a in formative)
    summative_raw = sum(a['Weight'] * a['Score'] for a in summative)

    formative_pct = (formative_raw / (formative_weight * 100)) * 100 if formative_weight else 0
    summative_pct = (summative_raw / (summative_weight * 100)) * 100 if summative_weight else 0

    print("\n=== FINAL GRADE REPORT ===")
    print(f"Weighted Score : {total_grade:.1f}/100")
    print(f"GPA            : {gpa:.2f}/5.0")
    print(f"Formative      : {formative_pct:.1f}%")
    print(f"Summative      : {summative_pct:.1f}%")

    status = "PASSED" if formative_pct >= 50 and summative_pct >= 50 else "FAILED"
    print(f"FINAL STATUS   : {status}")

    if status == "FAILED":
        failed_formative = [a for a in formative if a['Score'] < 50]
        if failed_formative:
            max_w = max(a['Weight'] for a in failed_formative)
            eligible = [a['Assignment'] for a in failed_formative if a['Weight'] == max_w]
            print(f"Resubmission Eligible: {', '.join(eligible)}")

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()

# סיכום קידוח, עם טיפול בשגיאות
# הקובץ borehole.txt צריך להיות באותה תיקייה של הקובץ הזה

total = 0        # צבירה: סכום החבטות
count = 0        # ספירה: מספר המדידות התקינות
max_blows = 0    # השיא עד עכשיו
max_depth = 0    # העומק של השיא

filename = "borehole.txt"

try:
    with open(filename) as f:
        for line in f:
            line = line.strip()
            parts = line.split(",")

            # ניסיון להמיר למספרים. אם השורה פגומה, מדלגים עליה וממשיכים
            try:
                depth = float(parts[0])
                blows = int(parts[1])
            except ValueError:
                print(f"Skipping bad line: {line}")
                continue

            print(f"Depth {depth} m: {blows} blows")
            count = count + 1
            total = total + blows
            if blows > max_blows:
                max_blows = blows
                max_depth = depth

    # סיכום: רץ פעם אחת, אחרי שכל הקובץ נקרא
    print(f"Measurements: {count}")
    print(f"Average blows: {total / count:.1f}")
    print(f"Max blows: {max_blows} at {max_depth} m")

# אם הקובץ לא נמצא, מודיעים על כך במקום לקרוס
except FileNotFoundError:
    print(f"File not found: {filename}")

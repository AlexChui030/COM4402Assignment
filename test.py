# Printing uppercase (A-Z) and lowercase (a-z) using for loop
import Settings
Settings.initialize()

for i in range(0, len(Settings.global_QnA)):
    print(f"i = {i}")
    print(f"Question{i + 1}:", Settings.global_QnA[i]["question"])
    for j in range(0, len(Settings.global_QnA[i]["options"])):
        print(f"Option{chr(j + 65)}: " + Settings.global_QnA[i]["options"][j])
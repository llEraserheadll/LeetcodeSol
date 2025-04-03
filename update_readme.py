import os
import re

def get_solved_problems():
    problem_dirs = [d for d in os.listdir('.') if os.path.isdir(d) and re.match(r'\d+', d)]
    problem_data = []
    
    for problem in problem_dirs:
        match = re.match(r'(\d+) (.+)', problem)
        if match:
            problem_number = match.group(1)
            problem_title = match.group(2)
            problem_data.append((problem_number, problem_title))
    
    return sorted(problem_data, key=lambda x: int(x[0]))


def update_readme():
    problems = get_solved_problems()
    problem_count = len(problems)
    
    problem_table = '\n'.join([f"| {num} | {title} | TBD | [Solution](./{num} {title}) |" for num, title in problems])
    
    with open("README.md", "r") as f:
        readme_content = f.read()
    
    readme_content = re.sub(r'`{{PROBLEM_COUNT}}`', f'`{problem_count}`', readme_content)
    readme_content = re.sub(r'\|---\|---------\|-----------\|----------\|\n{{PROBLEM_TABLE}}', f'|---|---------|-----------|----------|\n{problem_table}', readme_content)
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    
if __name__ == "__main__":
    update_readme()

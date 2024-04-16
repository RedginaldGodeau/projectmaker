from bs4 import BeautifulSoup
from markdownify import markdownify as md
import sys
import os


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        sys.stderr.write("Usage: ./projectmaker.py hbnb.html\n")
        sys.exit(1)
    
    input_file = args[1]
    if not os.path.exists(input_file):
        sys.stderr.write("Missing " + input_file + "\n")
        sys.exit(1)

    html_file = open(input_file)

    soup = BeautifulSoup(html_file, 'html.parser')
    task_cards = soup.find_all("div", {"class": "task-card"})

    # Create Task files
    for card in task_cards:
        directories = card.find("div", {"class": "list-group-item"}).find_all("code")
        Dirname = directories[len(directories) - 2].get_text()
        if not os.path.exists(Dirname):
            os.makedirs(Dirname)
        FileName = directories[len(directories) - 1].get_text()
        if not os.path.exists(Dirname + "/" + FileName):
            f = open(Dirname + "/" + FileName, "w")
            f.close()
    
    # Create Readme
    title = soup.find("h1")
    objective_card = soup.find("div", {"id": "project-description"})
    readme =  md(str(objective_card))
    f = open(Dirname + "/README.md", "w")
    f.write("# " + title.get_text() + "\n" + readme)
    f.close()

# end main
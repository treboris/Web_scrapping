from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()


soup = BeautifulSoup(contents,"html.parser")
all_list = soup.find_all(name = "a")


for tag in all_list:
    print(tag.getText())
    print("--------------------")
    print(tag.get("href"))
print(all_list)


print("**********************")
heading = soup.find(name = "h3", class_= "heading")
print(heading.get("class"))

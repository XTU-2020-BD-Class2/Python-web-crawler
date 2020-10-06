from bs4 import BeautifulSoup

content_str = """
    
    <div class="box">
        <a href="1984.html">
            <h4>1984</h4>
        </a>
    </div>


"""

soup1 = BeautifulSoup(content_str, features="lxml")
# soup2 = BeautifulSoup(content_str, features="html.parser")
# soup3 = BeautifulSoup(content_str, features="xml")
# soup4 = BeautifulSoup(content_str, features="html5lib")
# print(soup1)
# print(soup2)
# print(soup3)
# print(soup4)

# print(soup1)
# print(soup1.prettify())
soup1.reset()
print(soup1)

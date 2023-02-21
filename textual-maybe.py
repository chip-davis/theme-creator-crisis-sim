from textual.app import App, ComposeResult
from textual.widgets import Input
from textual.widgets import Header, Button
import git
import os
import shutil

class ThemeChangerCode(object):
    def __init__(self, brand_name, brand_logo_nav, brand_logo_profile, brand_email_logo):
        self.brand_name = brand_name
        self.brand_logo_nav = brand_logo_nav
        self.brand_logo_profile = brand_logo_profile
        self.brand_email_logo = brand_email_logo
        self.brand_template = "https://github.com/chip-davis/crisis-frontend.git"
        self.logo_dir = "/public"
    
    def clone_repo(self):
        try:
          repo = git.Repo.clone_from(self.brand_template, self.brand_name)
          repo.git.checkout('brand_template')
        except git.exc.GitCommandError:
          print("Template already cloned")
          pass
    
    def save_navbar_file(self):
        
        ## save the navbar file
        with open (self.brand_name + "/src/Components/Navbar.js", "r") as navbar:
            self.navbar = navbar.readlines()

    def save_news_files(self):
        ## save the news file
        with open (self.brand_name + "/src/Components/News/Blog.js", "r") as news:
            self.news = news.readlines()

        ## save the individual news file
        with open (self.brand_name + "/src/Components/News/DisplayIndividualNews.js", "r") as individual_news:
            self.individual_news = individual_news.readlines()

    def save_email_header(self):
        ## save the email header file
        with open (self.brand_name + "/src/Helpers/Email/Components/EmailHeader/EmailHeaderLeft.js", "r") as email_header:
            self.email_header = email_header.readlines()
    
    def save_palplace_files(self):
        ## save the palplace header file
        with open (self.brand_name + "/src/Helpers/PalPlace/Components/PalPlaceHeader.js", "r") as pal_place_header:
            self.pal_place_header = pal_place_header.readlines()

        ## save the palplace sidebar file
        with open (self.brand_name + "/src/Helpers/PalPlace/Components/Sidebar.js", "r") as pal_place_sidebar:
            self.pal_place_sidebar = pal_place_sidebar.readlines()

    def save_pixter(self):
        ## save the pixter footer file
        with open (self.brand_name + "/src/Helpers/Pixter/Components/Footer/PixterFooter.js", "r") as pixter_footer:
            self.pixter_footer = pixter_footer.readlines()
    
    def save_files(self):
        self.save_navbar_file()
        self.save_news_files()
        self.save_email_header()
        self.save_palplace_files()
        self.save_pixter()


    def change_brand_name(self):
        self.news = [line.replace("BRAND", self.brand_name) for line in self.news]
        self.individual_news = [line.replace("BRAND", self.brand_name) for line in self.individual_news]
        self.pal_place_header = [line.replace("BRAND", self.brand_name) for line in self.pal_place_header]
        self.pal_place_sidebar = [line.replace("BRAND", self.brand_name) for line in self.pal_place_sidebar]
        self.pixter_footer = [line.replace("BRAND", self.brand_name) for line in self.pixter_footer]
    def change_logos(self):
        if os.path.exists(f"{self.brand_name}{self.logo_dir}/brand_email_logo.png"):
            os.remove(f"{self.brand_name}{self.logo_dir}/brand_email_logo.png")
        if os.path.exists(f"{self.brand_name}{self.logo_dir}/brand_logo_nav.png"):
            os.remove(f"{self.brand_name}{self.logo_dir}/brand_logo_nav.png")
        if os.path.exists(f"{self.brand_name}{self.logo_dir}/brand_logo_profile.png"):
            os.remove(f"{self.brand_name}{self.logo_dir}/brand_logo_profile.png")

        shutil.copy(self.brand_email_logo, f"{self.brand_name}{self.logo_dir}/brand_email_logo.png")
        shutil.copy(self.brand_logo_nav, f"{self.brand_name}{self.logo_dir}/brand_logo_nav.png")
        shutil.copy(self.brand_logo_profile, f"{self.brand_name}{self.logo_dir}/brand_logo_profile.png")
      
    def write_files(self):
      with open (self.brand_name + "/src/Components/News/Blog.js", "w") as news:
        news.writelines(self.news)
      with open (self.brand_name + "/src/Components/News/DisplayIndividualNews.js", "w") as individual_news:
        individual_news.writelines(self.individual_news)
      with open (self.brand_name + "/src/Helpers/Email/Components/EmailHeader/EmailHeaderLeft.js", "w") as email_header:
        email_header.writelines(self.email_header)
      with open (self.brand_name + "/src/Helpers/PalPlace/Components/PalPlaceHeader.js", "w") as pal_place_header:
        pal_place_header.writelines(self.pal_place_header)
      with open (self.brand_name + "/src/Helpers/PalPlace/Components/Sidebar.js", "w") as pal_place_sidebar:
        pal_place_sidebar.writelines(self.pal_place_sidebar)
      with open (self.brand_name + "/src/Helpers/Pixter/Components/Footer/PixterFooter.js", "w") as pixter_footer:
        pixter_footer.writelines(self.pixter_footer)




  


class ThemeChanger(App):
    CSS_PATH = "styles.css"
    TITLE = "A theme changer app for Crisis Sim"
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Brand Name", id="brand_name")
        yield Input(placeholder="Nav Logo path", id="nav_logo")
        yield Input(placeholder="Email logo path", id="email_logo")
        yield Header()
        yield Button("Change theme", id="change_theme", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
       print(event)
        ## check if file exists
      # if not os.path.exists(brand_logo_nav):
      #   print("Nav logo file does not exist")
      #   exit()
      # if not os.path.exists(brand_logo_profile):
      #   print("Profile logo file does not exist")
      #   exit()
      # if not os.path.exists(brand_email_logo):
      #   print("Email logo file does not exist")
      #   exit()

      # theme = ThemeChangerCode(brand_name, brand_logo_nav, brand_logo_profile, brand_email_logo)

      # theme.clone_repo()

      # theme.save_files()

      # theme.change_brand_name()

      # theme.change_logos()

      # theme.write_files()



if __name__ == "__main__":
    app = ThemeChanger()
    app.run()
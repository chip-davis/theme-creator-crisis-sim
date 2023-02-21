import git
import os
import shutil

class ThemeChanger(object):
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



if __name__ == "__main__":
  # brand_name = input("What is the brand name? ")
  # brand_logo_nav = input("What is the brand nav logo file path? ")
  # brand_logo_profile = input("What is the brand profile logo file path? ")
  # brand_email_logo = input("What is the brand email logo file path? ")
  brand_name = "Nestle"
  brand_logo_nav = r"logos\brand_logo_nav.png"
  brand_logo_profile= r"logos\brand_logo_profile.png"
  brand_email_logo = r"logos\brand_email_logo.png"
  ## check if file exists
  if not os.path.exists(brand_logo_nav):
    print("Nav logo file does not exist")
    exit()
  if not os.path.exists(brand_logo_profile):
    print("Profile logo file does not exist")
    exit()
  if not os.path.exists(brand_email_logo):
    print("Email logo file does not exist")
    exit()

  theme = ThemeChanger(brand_name, brand_logo_nav, brand_logo_profile, brand_email_logo)
  print("Cloning template...")
  theme.clone_repo()
  print("Template cloned")
  print("Saving files...")
  theme.save_files()
  print("Files saved")
  print("Changing brand name...")
  theme.change_brand_name()
  print("Brand name changed")
  print("Changing logos...")
  theme.change_logos()
  print("Logos changed")
  print("Saving files...")
  theme.write_files()
  print("Files saved")
  print("Done")


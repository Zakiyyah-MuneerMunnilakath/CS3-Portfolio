class Publication:
    def __init__(self,title,author):
        self.__title = title
        self.__author = author
    
    @property    
    def title (self):
        return self.__title
    
    @title.setter
    def title (self, value):
        self.__title = value
        
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, value):
        self.__author = value
        
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        
class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages
            
    @property
    def number_of_pages(self):
        return self.__number_of_pages
        
    @number_of_pages.setter
    def number_of_pages(self, value):
        if value <= 0:
            print("The number of pages must be positive.")
            self.__number_of_pages = 0
        else:
            self.__number_of_pages = value
            
    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.number_of_pages}")
        
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number
        
    @property 
    def issue_number (self):
        return self.__issue_number
        
    @issue_number.setter
    def issue_number(self, value):
        if value <= 0:
            print("The issue number must be positive.")
            self.__issue_number = 0
        else:
            self.__issue_number = value
            
    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")
        
pub1 = Publication("Bahaghari", "Kayla Villanueva")
book1 = Book("Percy Jackson & The Olympians", "Rick Riordan", 67)
mag1 = Magazine("Vogue", "Luisa Entac", 505)
pub2 = Publication("The Central Scholar", "Jamila Acosta")
book2 = Book("Harry Potter and the Philosopher's Stone", "JK Rowling", 61)
mag2 = Magazine("The Economist", "Numerous authors", 777)

print("---PUBLICATIONS---")
pub1.display_info()
print()
pub2.display_info()

print("\n---BOOKS---")
book1.display_info()
print()
book2.display_info()

print("\n---MAGAZINES---")
mag1.display_info()
print()
mag2.display_info()

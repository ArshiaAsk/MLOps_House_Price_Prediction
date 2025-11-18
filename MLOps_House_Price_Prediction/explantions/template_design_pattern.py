from abc import ABC, abstractmethod

class DiningExperience(ABC):
    def serve_dinner(self):
        self.serve_appetizer()
        self.serve_main_course()
        self.serve_dessert()
        self.serve_beverage()
        
    @abstractmethod
    def serve_appetizer(slef):
        pass
    
    @abstractmethod
    def serve_main_course(slef):
        pass
    
    @abstractmethod
    def serve_dessert(self):
        pass
    
    @abstractmethod
    def serve_beverage(slef):
        pass
    
    
    
class ItalianDinner(DiningExperience):
    def serve_appetizer(self):
        print("Serving bruschetta as appetizer.")

    def serve_main_course(self):
        print("Serving pasta as the main course.")

    def serve_dessert(self):
        print("Serving tiramisu as dessert.")

    def serve_beverage(self):
        print("Serving wine as the beverage.")


class ChineseDinner(DiningExperience):
    def serve_appetizer(self):
        print("Serving spring rolls as appetizer.")

    def serve_main_course(self):
        print("Serving stir-fried noodles as the main course.")

    def serve_dessert(self):
        print("Serving fortune cookies as dessert.")

    def serve_beverage(self):
        print("Serving tea as the beverage.")
        


if __name__ == "__main__":
    print("Italian Dinner")
    italian_dinner = ItalianDinner()
    italian_dinner.serve_dinner()
    
    print("Chinese Dinner")
    chinese_dinner = ChineseDinner()
    chinese_dinner.serve_dinner()
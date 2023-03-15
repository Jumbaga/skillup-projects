from abc import ABC, abstractmethod
import re

#Film class, name is a dependency and a private property and has abstract rate movie method to force children classes to implement it.
#Also made film class abstract as there is no interest in having this object instantiated 
class Film(ABC):
    def __init__(self, name):
        self._name = name
    #Property decorator to define class getter    
    @property
    def name(self):
        return self._name
    #Setter decorator to define class setter  
    @name.setter
    def name(self, name):
        self._name = name
    #Abstract method to force children classes to implement
    @abstractmethod
    def rate_movie():
        pass

#SciFi class, extends from Film inheriting name property and has to implement rate movie method, has special effects and stunts as 
#dependencies and private properties.
class SciFi(Film):    
    def __init__(self, name, special_effects, stunts):
        super().__init__(name)
        self._special_effects = special_effects
        self._stunts = stunts
    #Property decorator to define class getters   
    @property
    def special_effects(self):
        return self._special_effects
    @property
    def stunts(self):
        return self._stunts

    #Setter decorator to define class setters    
    @special_effects.setter
    def special_effects(self, special_effects):
        #Value validation [1-10]
        valid_range = [*range(1,11)]
        if special_effects in valid_range:
            self._special_effects = special_effects
        else:
            print(f'Sci-Fi special effects invalid value: {special_effects} --> '
                  f'Valid values range from [{min(valid_range)} - {max(valid_range)}]')
                  
    @stunts.setter
    def stunts(self, stunts):
        #Value validation [1-10]
        valid_range = [*range(1,11)]
        if stunts in valid_range:
            self._stunts = stunts
        else:
            print(f'Sci-Fi stunts invalid value: {stunts} --> '
                  f'Valid values range from [{min(valid_range)} - {max(valid_range)}]')
    #Overriding of rate movie method, its a simple print doing some basic math operations with the properties of the object
    def rate_movie(self):
        print(f'The movie {self._name} has a rating of {round((self._special_effects + self._stunts)/2, 2)} in the Sci-Fi genre.')

#SciFi class, extends from Film inheriting name property and has to implement rate movie method, has special authenticity and 
# viewership as dependencies and private properties.
class Documentary(Film):
    def __init__(self, name, authenticity, viewership):
        super().__init__(name)
        self._authenticity = authenticity
        self._viewership = viewership

    #Property decorator to define class getters
    @property
    def authenticity(self):
        return self._authenticity
    @property
    def viewership(self):
        return self._viewership
    
    #Setter decorator to define class setters
    @authenticity.setter
    def authenticity(self, authenticity):
        #Value validation [1-100]
        valid_range = [*range(1,101)]
        if authenticity in valid_range:
            self._authenticity = authenticity
        else:
            print(f'Documentary authenticity invalid value: {authenticity} --> '
                  f'Valid values range from [{min(valid_range)} - {max(valid_range)}]')
            
    @viewership.setter
    def viewership(self, viewership):
        #Value validation [1-10]
        valid_range = [*range(1,11)]
        if viewership in valid_range:
            self._viewership = viewership
        else:
            print(f'Documentary viewership invalid value: {viewership} --> '
                  f'Valid values range from [{min(valid_range)} - {max(valid_range)}]')
    #Overriding of rate movie method, its a simple print doing some basic math operations with the properties of the object
    def rate_movie(self):
        print(f'The movie {self._name} has a rating of {round(self._authenticity/100 * self._viewership, 2)} in the Documentary genre.')

#Creating 2 instances of SciFi
the_goat = SciFi("Star Wars: A New Hope", 10, 10)
the_coat = SciFi("Highlander II: The Quickening", 1, 0)
#Creating 2 instances of Documentary
knowledge = Documentary("Mankind: The Story of All of Us", 95, 10)
garbage = Documentary("How woke do the woke get to woke the world", 6, 1)

#Putting them on a list
movies = [the_goat,the_coat,knowledge,garbage]
#Iterating through it and calling the rate_movie method
for movie in movies:
    movie.rate_movie()

#Trying to set properties to values outside of the accepted range
the_goat.special_effects = 20
the_coat.stunts = -15
knowledge.viewership = 1000
garbage.authenticity = -9001


#Method to return a list of movies with the word "the" but not the word "and", has a list of strings as a dependency.
def craft_movie_lst(lst):
    #Creating and empty list to populate with valid movies
    movie_lst = []

    #Iterating through the provided list
    for movie in lst:
        
        #Using regex and re module to store match object on variables, we are searching for any match as long has it has at least
        #1 word "the" we store it on the_search, and we do the same for the word "and" but store in and_search variable. Also made
        #regex case-insensitive.
        the_search = re.search(r'\bthe\b', movie, re.IGNORECASE)
        and_search = re.search(r'\band\b', movie, re.IGNORECASE)

        #Because we want movie names with the word "the" but not the word "and" we are using this conditional to do just that:
        #Since re.search returns a match object if it has any matches and None if it has no matches we are interested in the cases
        #where the_search has a match object stored in it but and_search has None, then we append the movie to the list
        if the_search is not None and and_search is None:
            movie_lst.append(movie)
    #Returning a list of valid names
    return movie_lst

#Creating a list with random names valid and invalid to test our function
movies_lst = ["Beauty and the Beast", "The Lion King", "The Godfather", 
          "Fellowship of the Ring", "And You", "The and", "And The"]

#Printing the function call and passing the movie list
print(craft_movie_lst(movies_lst))
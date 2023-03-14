from abc import ABC, abstractmethod
import re

class Film:
    def __init__(self, name):
        self._name = name
        
    @abstractmethod
    def rate_movie():
        pass

class SciFi(Film):    
    def __init__(self, name, special_effects, stunts):
        super().__init__(name)
        self._special_effects = special_effects
        self._stunts = stunts
    
    @property
    def special_effects(self):
        return self._special_effects
    @property
    def stunts(self):
        return self._stunts
    
    @special_effects.setter
    def special_effects(self, special_effects):
        valid_range = [*range(1,11)]
        if special_effects in valid_range:
            self._special_effects = special_effects
        else:
            print(f'Sci-Fi special effects invalid value: {special_effects} --> '
                  f'Valid values range from [{min(valid_range)} - {max(valid_range)}]')
                  
    @stunts.setter
    def stunts(self, stunts):
        valid_range = [*range(1,11)]
        if stunts in valid_range:
            self._stunts = stunts
        else:
            print(f'Sci-Fi stunts invalid value: {stunts} --> '
                  f'Valid values range from [{min(valid_range)} - {max(valid_range)}]')

    def rate_movie(self):
        print(f'The movie {self._name} has a rating of {round((self._special_effects + self._stunts)/2, 2)} in the Sci-Fi genre.')

class Documentary(Film):
    def __init__(self, name, authenticity, viewership):
        super().__init__(name)
        self._authenticity = authenticity
        self._viewership = viewership
    
    @property
    def authenticity(self):
        return self._authenticity
    @property
    def viewership(self):
        return self._viewership
    
    @authenticity.setter
    def authenticity(self, authenticity):
        valid_range = [*range(1,101)]
        if authenticity in valid_range:
            self._authenticity = authenticity
        else:
            print(f'Documentary authenticity invalid value: {authenticity} --> '
                  f'Valid values range from [{min(valid_range)} - {max(valid_range)}]')
            
    @viewership.setter
    def viewership(self, viewership):
        valid_range = [*range(1,11)]
        if viewership in valid_range:
            self._viewership = viewership
        else:
            print(f'Documentary viewership invalid value: {viewership} --> '
                  f'Valid values range from [{min(valid_range)} - {max(valid_range)}]')

    def rate_movie(self):
        print(f'The movie {self._name} has a rating of {round(self._authenticity/100 * self._viewership, 2)} in the Documentary genre.')

the_goat = SciFi("Star Wars: A New Hope", 10, 10)
the_coat = SciFi("Highlander II: The Quickening", 1, 0)
knowledge = Documentary("Mankind: The Story of All of Us", 95, 10)
garbage = Documentary("How woke do the woke get to woke the world", 6, 1)

the_goat.rate_movie()
the_coat.rate_movie()
knowledge.rate_movie()
garbage.rate_movie()

the_goat.special_effects = 20
the_coat.stunts = -15
knowledge.authenticity = 1000
garbage.authenticity = -9001

def craft_movie_lst(lst):

    movie_lst = []
    for movie in lst:

        the_search = re.search(r'\bthe\b', movie, re.IGNORECASE)
        and_search = re.search(r'\band\b', movie, re.IGNORECASE)

        if the_search is not None and and_search is None:
            movie_lst.append(movie)
    return movie_lst

movies = ["Beauty and the Beast", "The Lion King", "The Godfather", "Fellowship of the Ring", "And You"]
print(craft_movie_lst(movies))

    




PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
all_pets = []

class Pet:
    def __init__(self, name, pet_type, owner):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all_pets.append(self)
    
    @property    
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in PET_TYPES:
            raise Exception("Invalid pet type.")
        self._pet_type = pet_type
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Invalid owner type.")
        self._owner = owner
        

class Owner:
    def __init__(self, name,):
        self.pets = []
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all_pets if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet is not a pet type.")
        pet.owner = self
        
    def get_sorted_pets(cls):
        return sorted(cls.all_pets, key=lambda pet:pet.name)
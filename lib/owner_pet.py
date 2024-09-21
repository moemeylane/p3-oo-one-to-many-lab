class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {Pet.PET_TYPES}")
        self.pet_type = pet_type

        # Check if owner is an instance of Owner, if provided
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner.")
            # Add the pet to the owner's pets list
            owner.add_pet(self)

        self.owner = owner

        # Add this pet instance to the class variable 'all'
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        # Return all pets belonging to the owner
        return self._pets

    def add_pet(self, pet):
        # Ensure the pet is an instance of the Pet class
        if not isinstance(pet, Pet):
            raise Exception("Argument must be an instance of Pet.")
        if pet not in self._pets:
            self._pets.append(pet)  # Add the pet to the owner's list of pets
        pet.owner = self  # Set the owner of the pet

    def get_sorted_pets(self):
        # Return the owner's pets sorted by their names
        return sorted(self._pets, key=lambda pet: pet.name)

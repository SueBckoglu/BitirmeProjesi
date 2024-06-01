<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-center col-span-4 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg p-4 flex flex-col justify-center items-center text-center space-y-4">
        <h1 class="text-3xl font-bold text-pink-600">Add Furbaby</h1>
        <p class="text-lg italic text-gray-600">"Loving and caring for a pet opens the door to a deeper connection with the world around us." - Unknown</p>
      </div>
      <div class="bg-white border border-gray-200 rounded-lg p-4 flex flex-col justify-center space-y-4">
        <form @submit.prevent="submitForm" class="space-y-6">
          <div class="flex flex-col">
            <label for="petName" class="mb-2">Name</label>
            <input type="text" id="petName" v-model="pet.name" placeholder="Name" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
          </div>
          <div class="flex flex-col">
            <label for="petType" class="mb-2">Type</label>
            <input type="text" id="petType" v-model="pet.type" placeholder="Type" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
          </div>
          <div class="flex flex-col">
            <label for="petAge" class="mb-2">Age</label>
            <input type="number" id="petAge" v-model="pet.age" placeholder="Age" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
          </div>
          <div class="flex flex-col">
            <label for="petGender" class="mb-2">Gender</label>
            <input type="text" id="petGender" v-model="pet.gender" placeholder="Gender" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
          </div>
          <div class="flex flex-col">
            <label for="petBreed" class="mb-2">Breed</label>
            <input type="text" id="petBreed" v-model="pet.breed" placeholder="Breed" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
          </div>
          <div class="flex flex-col">
            <label for="petColor" class="mb-2">Color</label>
            <input type="text" id="petColor" v-model="pet.color" placeholder="Color" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
          </div>
          <div class="flex flex-col">
            <label for="petBirthplace" class="mb-2">Birthplace</label>
            <input type="text" id="petBirthplace" v-model="pet.birthplace" placeholder="Birthplace" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
          </div>
          <div class="flex flex-col">
            <label for="petSpayed" class="mb-2">Spayed</label>
            <input type="text" id="petSpayed" v-model="pet.spayed" placeholder="Spayed" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
          </div>
          <div class="flex flex-col">
            <label for="petPersonality" class="mb-2">Personality</label>
            <input type="text" id="petPersonality" v-model="pet.personality" placeholder="Personality" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
          </div>
          <div class="flex flex-col">
            <label for="petImage" class="mb-2">Image URL</label>
            <input type="text" id="petImage" v-model="pet.image" placeholder="Image URL" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
          </div>
          <button type="submit" class="py-3 px-6 bg-pink-600 text-white rounded-lg">Add Pet</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      pet: {
        name: '',
        age: null,
        breed: '',
        type: '',
        gender: '',
        color: '',
        birthplace: '',
        spayed: '',
        personality: '',
        image: ''
      },
      errors: []
    };
  },
  methods: {
    submitForm() {
      this.errors = [];

      if (!this.isValid()) {
        this.errors.push("Form is not valid!");
        return;
      }

      axios
        .post('/api/pets/create/', { pet: this.pet })
        .then(response => {
          console.log('Pet created successfully:', response.data);
          this.pet = {
            name: '',
            age: null,
            breed: '',
            type: '',
            gender: '',
            color: '',
            birthplace: '',
            spayed: '',
            personality: '',
            image: ''
          };
          this.$router.push('/animalprofile');
        })
        .catch(error => {
          console.error('Error:', error.response.data);
          this.errors.push(error.response.data);
        });
    },
    isValid() {
      const { name, age, breed, type, gender, color, birthplace, spayed, personality, image } = this.pet;
      return name && age && breed && type && gender && color && birthplace && spayed && personality && image;
    }
  }
}
</script>

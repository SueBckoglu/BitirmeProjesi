<template>
    <div class="p-4 bg-white border border-gray-200 rounded-lg">
        <h3 class="mb-6 text-xl">Furry Family Finders<!--Adorable Friends Waiting for a Home--></h3>

        <div class="space-y-4">
            <div 
                class="flex items-center justify-between"
                v-for="pet in pets"
                :key="pet.id"
            >  
                <div class="flex items-center space-x-2">
                    <img :src="pet.image" class="w-[40px] rounded-full" alt="pet friend">
                    <p class="text-xs"><strong>{{ pet.name }}</strong></p>
                </div>

                <RouterLink to="/animalprofile" class="py-2 px-3 bg-pink-600 text-white text-xs rounded-lg">Get to know</RouterLink>
            </div>
        </div>

        <div class="space-y-4">
            <div 
                class="flex items-center justify-between"
            >  
                    <div class="flex items-center space-x-2">
                        <img src="https://i.pinimg.com/originals/67/7c/6f/677c6fb31ffa3f09248a600ea85105cf.jpg" class="w-[40px] rounded-full" alt="pet friend">
                        <p class="text-xs"><strong>Willow</strong></p>
                    </div>

                <RouterLink to="/animalprofile" class="py-2 px-3 bg-pink-600 text-white text-xs rounded-lg">Get to know</RouterLink>
            </div>
        </div>

    </div>
</template>


<script>
import { RouterLink } from 'vue-router';
import axios from 'axios';

export default {
    name: 'FurryFamilyFinders',
    data() {
        return {
            pets: []
        };
    },
    components: {
        RouterLink
    },
    mounted() {
        this.getPets();
    },
    methods: {
        getPets() {
            axios
                .get('/api/pets/')
                .then(response => {
                    console.log(response.data);
                    this.pets = response.data;
                })
                .catch(error => {
                    console.log('Error: ', error);
                });
        }
    }
}
</script>

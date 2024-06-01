<template>
    <div>
        <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
            <div class="main-center col-span-4 space-y-4">
                <div
                    class="bg-white border border-gray-200 rounded-lg p-4 flex flex-col justify-center items-center text-center space-y-4">
                    <h1 class="text-3xl font-bold text-pink-600">Purrfect Match</h1>
                    <p class="text-lg italic text-gray-600">"The greatness of a nation and its moral progress can be judged
                        by the way its animals are treated." - Mahatma Gandhi</p>
                </div>
                <div class="bg-white border border-gray-200 rounded-lg">
                    <div class="p-4 flex space-x-4">
                        <input type="search" class="p-4 w-full bg-gray-100 rounded-lg"
                            placeholder="Find your purr-fect match!">

                        <a href="#" class="inline-block py-4 px-6 bg-pink-600 text-white rounded-lg">Discover</a>

                        <RouterLink to="/signupanimal" class="flex items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="size-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                            </svg>
                        </RouterLink>
                    </div>
                </div>

                <div class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4">
                    <div class="p-4 text-center bg-gray-100 rounded-lg">
                        <img src="https://i.pinimg.com/originals/67/7c/6f/677c6fb31ffa3f09248a600ea85105cf.jpg"
                            class="mb-6 rounded-full" alt="picture">

                        <p class="text-lg font-semibold">Meredith</p>
                        <p class="text-s text-gray-600 font-semibold italic">The Cat</p>

                        <div class="mt-6 grid grid-cols-2 gap-4">
                            <p class="text-xs text-gray-500"><strong>Age:</strong> 2 years old</p>
                            <p class="text-xs text-gray-500"><strong>Gender:</strong> Female</p>
                            <p class="text-xs text-gray-500"><strong>Breed:</strong> Scottish Fold</p>
                            <p class="text-xs text-gray-500"><strong>Birthplace:</strong> Home-born</p>
                            <p class="text-xs text-gray-500"><strong>Status:</strong> Not spayed</p>
                            <p class="text-xs text-gray-500"><strong>Personality:</strong> Playful and adorable</p>
                        </div>

                        <p class="mt-4 mb-4 text-pink-600 font-semibold"><em>Open your heart to a new furry friend!</em></p>
                        <RouterLink :to="{ name: 'animalprofile', params: { id: pet.id }}" class="inline-block py-4 px-6 bg-pink-600 text-white rounded-lg">Meet Them Now!</RouterLink>
                    </div>

                    <!--<div class="p-4 text-center bg-gray-100 rounded-lg">
                        <img :src="pet.image" class="mb-6 rounded-full" alt="pet picture">

                        <p class="text-lg font-semibold">{{ pet.name }}</p>
                        <p class="text-s text-gray-600 font-semibold italic">{{ pet.type }}</p>

                        <div class="mt-6 grid grid-cols-2 gap-4">
                            <p class="text-xs text-gray-500"><strong>Age:</strong>{{ pet.age }} years old</p>
                            <p class="text-xs text-gray-500"><strong>Gender:</strong> {{ pet.gender}}</p>
                            <p class="text-xs text-gray-500"><strong>Breed:</strong>{{ pet.breed }}</p>
                            <p class="text-xs text-gray-500"><strong>Birthplace:</strong>{{ pet.birthplace }}</p>
                            <p class="text-xs text-gray-500"><strong>Status:</strong>{{ pet.spayed }}</p>
                            <p class="text-xs text-gray-500"><strong>Personality:</strong>{{ pet.personality }}</p>
                        </div>

                        <p class="mt-4 mb-4 text-pink-600 font-semibold"><em>Open your heart to a new furry friend!</em>
                        </p>
                        <a href="#" class="inline-block py-4 px-6 bg-pink-600 text-white rounded-lg">Meet Them Now!</a>
                    </div>-->
                    
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router';
import AnimalProfileView from './AnimalProfileView.vue';


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
            }
        };
    },
    components: { RouterLink }
}

</script>

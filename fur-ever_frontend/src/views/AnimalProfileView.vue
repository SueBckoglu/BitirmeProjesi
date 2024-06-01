<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1 space-y-4">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img :src="pet.image" class="mb-6 rounded-full" :alt="pet.name">
                <p class="text-lg font-semibold">{{ pet.name }}</p>
                <p class="text-s text-gray-600 font-semibold italic">{{ pet.type }}</p> 

                <div class="mt-6 grid grid-cols-2 gap-4">
                <p class="text-xs text-gray-500"><strong>Age:</strong> {{ pet.age }} years old</p>
                <p class="text-xs text-gray-500"><strong>Gender:</strong> {{ pet.gender }}</p>
                <p class="text-xs text-gray-500"><strong>Breed:</strong> {{ pet.breed }}</p>
                <p class="text-xs text-gray-500"><strong>Birthplace:</strong> {{ pet.birthplace }}</p>
                <p class="text-xs text-gray-500"><strong>Status:</strong> {{ pet.spayed }}</p>
                <p class="text-xs text-gray-500"><strong>Personality:</strong> {{ pet.personality }}</p>
                </div>
            </div>

            <button>Contact</button>

            <button>Adopt</button>
            
            </div>

            <div class="main-center col-span-2 space-y-4">
                <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">

                </div>
            </div>

            <div class="main-right col-span-1 space-y-4">
                <AdorableFriendsWaitingForAHome />

                <HelpOutAtTheseLovingShelters />

                <Trends />

                <PeopleYouMayKnow />
            </div>
    </div>
</template>

<script>
import axios from "axios";
import HelpOutAtTheseLovingShelters from "../components/HelpOutAtTheseLovingShelters.vue";
import AdorableFriendsWaitingForAHome from "../components/AdorableFriendsWaitingForAHome.vue";
import Trends from "@/components/Trends.vue";
import PeopleYouMayKnow from "@/components/PeopleYouMayKnow.vue";

export default {
    name: "AnimalProfileView",

    setup() {

    },

    components: {
        AdorableFriendsWaitingForAHome,
        HelpOutAtTheseLovingShelters,
        Trends,
        PeopleYouMayKnow,
    },

    data() {
        return {
            user: {
                id: "",
            },
            pet: {}
        };
    },

    mounted() {
        this.getPetData();
    },


    methods: {
        async getPetData() {
            try {
                const response = await axios.post("https://your-api.com/create_pet", {
                    pet: {
                        // Gerekirse isteğe eklenecek veriler buraya gelecek
                    }
                });
                this.pet = response.data.pet; // API'den gelen pet verisini atar
            } catch (error) {
                console.error("Error fetching pet data:", error);
            }
        },
    }
};
</script>

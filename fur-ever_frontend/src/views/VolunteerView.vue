<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg p-4 flex flex-col justify-center items-center text-center space-y-4">
                <h1 class="text-3xl font-bold text-pink-600">Pawsitive Impact</h1>
                <p class="text-lg italic text-gray-600">"The best way to find yourself is to lose yourself in the service of others." - Mahatma Gandhi</p>
            </div>
            <div class="bg-white border border-gray-200 rounded-lg">
                <div class="p-4 flex space-x-4">
                    <input type="search" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Discover Ways to Help">

                    <a href="#" class="inline-block py-4 px-6 bg-pink-600 text-white rounded-lg">Explore</a>

                    <RouterLink to="/event" class="flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 16.875h3.375m0 0h3.375m-3.375 0V13.5m0 3.375v3.375M6 10.5h2.25a2.25 2.25 0 0 0 2.25-2.25V6a2.25 2.25 0 0 0-2.25-2.25H6A2.25 2.25 0 0 0 3.75 6v2.25A2.25 2.25 0 0 0 6 10.5Zm0 9.75h2.25A2.25 2.25 0 0 0 10.5 18v-2.25a2.25 2.25 0 0 0-2.25-2.25H6a2.25 2.25 0 0 0-2.25 2.25V18A2.25 2.25 0 0 0 6 20.25Zm9.75-9.75H18a2.25 2.25 0 0 0 2.25-2.25V6A2.25 2.25 0 0 0 18 3.75h-2.25A2.25 2.25 0 0 0 13.5 6v2.25a2.25 2.25 0 0 0 2.25 2.25Z" />
                        </svg>
                    </RouterLink> 

                </div>
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-2 gap-4">
                <div class="p-4 flex items-center justify-center bg-gray-100 rounded-lg">
                    <img src="https://i.pinimg.com/originals/b0/f8/67/b0f867df0f02b5c86051d793af1be309.jpg" class="w-[100px] rounded-full" alt="picture">
                    <div class="ml-4">
                        <p class="mb-2"><strong>PawGuard Shelter</strong></p>
                        <p class="text-sm text-gray-500">Next Event:</p>
                        <p class="text-sm font-semibold">Paws in the Park Fundraiser</p>
                        <p class="text-xs text-gray-500">Date: October 15, 2024</p>
                        <p class="text-xs text-gray-500">Time: 10:00 AM - 4:00 PM</p>
                        <p class="text-xs text-gray-500">Location: Central Park</p>
                        <a href="#" class="inline-block py-2 px-4 mt-2 bg-pink-600 text-white rounded-lg">Volunteer</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            
            <AdorableFriendsWaitingForAHome/>
            
            <HelpOutAtTheseLovingShelters/>

            <Trends />

            <PeopleYouMayKnow />
            
        </div>
    </div>
</template>

<script>
import HelpOutAtTheseLovingShelters from '../components/HelpOutAtTheseLovingShelters.vue';
import AdorableFriendsWaitingForAHome from '../components/AdorableFriendsWaitingForAHome.vue'
import Trends from '@/components/Trends.vue';
import PeopleYouMayKnow from '@/components/PeopleYouMayKnow.vue';

export default {
    name: 'VolunteerView',
    components: {
    AdorableFriendsWaitingForAHome,
    HelpOutAtTheseLovingShelters,
    Trends,
    PeopleYouMayKnow
}
}
</script>
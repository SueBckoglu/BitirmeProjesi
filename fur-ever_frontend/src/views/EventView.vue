<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg p-4 flex flex-col justify-center items-center text-center space-y-4">
                <h1 class="text-3xl font-bold text-pink-600">Pawsitive Impact</h1>
                <p class="text-lg italic text-gray-600">"The best way to find yourself is to lose yourself in the service of others." - Mahatma Gandhi</p>
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg grid gap-4">
                <form>
                    <div class="p-4 flex items-center justify-center bg-gray-100 rounded-lg">
                        <img src="https://i.pinimg.com/originals/b0/f8/67/b0f867df0f02b5c86051d793af1be309.jpg" class="mr-4 rounded-full" alt="picture">
                        <div class="ml-4">
                            <div class="flex flex-col">
                                <label for="shelterName" class="mb-2"><strong>Shelter Name</strong></label>
                                <input type="text" id="shelterName" placeholder="Enter Shelter Name" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
                            </div>
                            <div class="flex flex-col">
                                <label for="eventName" class="text-sm text-gray-500 mb-1">Next Event</label>
                                <input type="text" id="eventName" placeholder="Enter Event Name" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
                            </div>
                            <div class="flex flex-col">
                                <label for="eventDate" class="text-xs text-gray-500 mb-1">Date</label>
                                <input type="date" id="eventDate" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
                            </div>
                            <div class="flex flex-col">
                                <label for="eventTime" class="text-xs text-gray-500 mb-1">Time</label>
                                <input type="time" id="eventTime" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
                            </div>
                            <div class="flex flex-col">
                                <label for="eventLocation" class="text-xs text-gray-500 mb-1">Location</label>
                                <input type="text" id="eventLocation" placeholder="Enter Event Location" class="w-full mt-2 py-2 px-4 border border-gray-300 rounded-lg">
                            </div>
                            <button type="submit" class="inline-block py-2 px-4 mt-2 bg-pink-600 text-white rounded-lg">Add Event</button>
                        </div>
                    </div>
                </form>
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
import axios from 'axios';
import { useUserStore } from '@/stores/user'

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
    },

    setup(){
        const userStore = useUserStore()

        return {
            userStore,
        }
    },
    
    data(){
        return {
            form: {
                shelterName: '',
                eventName: '',
                eventDate: '',
                eventTime: '',
                eventLocation: '',
            },
            errors: []
        }
    },

    methods: {
        async submitForm(){
            this.errors = []

            if (this.form.shelterName === ''){
                this.errors.push('Your shelterName is missing')
            }

            if (this.form.eventName === ''){
                this.errors.push('Your eventName is missing')
            }

            if (this.form.eventDate === ''){
                this.errors.push('Your eventDate is missing')
            }

            if (this.form.eventTime === ''){
                this.errors.push('Your eventTime is missing')
            }

            if (this.form.eventLocation === ''){
                this.errors.push('Your eventLocation is missing')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/api/events/create/', this.form)
                    .then(response => {
                        this.userStore.setToken(response.data)

                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;

                        this.$router.push('/volunteer')
                    })
                    .catch(error => {
                        console.log('error', error)

                        this.errors.push('Hey! You need to check your informations seems off to me! Or did you activate your account ?')
                    })
            }
            
            if (this.errors.length === 0) {
                await axios
                    .get('/api/me/')
                    .then(response => {
                        this.userStore.setUserInfo(response.data)

                        this.$router.push('/foryou')
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>
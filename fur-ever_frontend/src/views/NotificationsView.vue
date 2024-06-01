<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg p-4 flex flex-col justify-center items-center text-center space-y-4">
                <h1 class="text-3xl font-bold text-pink-600">🔔 Paw-sitive Pings</h1>
            </div>
            <div 
                class="p-4 bg-white border rounded-lg"
                v-for="notification in notifications"
                v-bind:key="notification.id"
                v-if="notifications.length"
                :style="{ border: '2px solid ' + notification.color }"
            >
                🔔   {{ notification.body }} 

                <button class="underline" @click="readNotification(notification)">Explore Further</button>
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg text-center" v-else>
                🐾 Hooray! <br> Your Inbox is as clean as a cat's whiskers! <br> Keep spreading the love and those paws will soon be filled with joy!
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
import axios from 'axios'

import Trends from '@/components/Trends.vue';
import AdorableFriendsWaitingForAHome from '../components/AdorableFriendsWaitingForAHome.vue'
import HelpOutAtTheseLovingShelters from '../components/HelpOutAtTheseLovingShelters.vue';
import PeopleYouMayKnow from '@/components/PeopleYouMayKnow.vue';

export default {
    name: 'notifications',

    components: {
    AdorableFriendsWaitingForAHome,
    HelpOutAtTheseLovingShelters,
    Trends,
    PeopleYouMayKnow
},

    data() {
        return {
            notifications: [
            { id: 1, body: "f'{request.user.name} could not resist giving your post a little star!'", color: 'pink' },
            { id: 2, body: "f'{request.user.name} left a paw-some comment on one of your posts! 🐾'", color: 'blue' },
            { id: 3, body: "f'Hey there! {request.user.name} wants to paws and be fur-iends with you!'", color: 'yellow' },
            { id: 4, body: "f'Great news! {request.user.name} is now your fur-iend! 🐾'", color: 'teal' },
            { id: 5, body: "f'{request.user.name} gently declined the chance to become fur-iends... 🐾'", color: 'red' },
            { id: 6, body: "f'Oops! {request.user.name} wasn't a fan of your pawment on a post... Don't worry, keep spreading pawsitivity! 🐾'", color: 'purple' },
            { id: 7, body: "f'Yay! {request.user.name} loved your pawment on a post! 🐾'", color: 'green' },
            ]
        }
    },

    mounted() {
        this.getNotifications()
    },

    methods: {
        getNotifications() {
            axios
                .get('/api/notifications/')
                .then(response => {
                    console.log(response.data)

                    this.notifications = response.data
                })
                .catch(error => {
                    console.log('Error: ', error)
                })
        },

        async readNotification(notification) {
            console.log('readNotification', notification.id)

            await axios
                .post(`/api/notifications/read/${notification.id}/`)
                .then(response => {
                    console.log(response.data)

                    if (notification.type_of_notification == 'post_like' || notification.type_of_notification == 'post_comment') {
                        this.$router.push({name: 'postview', params: {id: notification.post_id}})
                    } else {
                        this.$router.push({name: 'friends', params: {id: notification.created_for_id}})
                    }
                })
                .catch(error => {
                    console.log('Error: ', error)
                })
        }
    }
}
</script>
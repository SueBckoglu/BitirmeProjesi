<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg p-4 flex flex-col justify-center items-center text-center space-y-4">
                <h1 class="text-3xl font-bold text-pink-600">Critter Community Corner about #{{ $route.params.id }}</h1>
                <p class="text-lg italic text-gray-600">"The love for all living creatures is the most noble attribute of man." - Charles Darwin</p>
            </div>
            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="post in posts"
                v-bind:key="post.id"
                >
                
                    <FeedItem v-bind:post="post"/>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            
            <Trends/>

            <AdorableFriendsWaitingForAHome/>

            <HelpOutAtTheseLovingShelters/>

            <PeopleYouMayKnow />

        </div>
    </div>
</template>

<script>
import axios from 'axios'
import HelpOutAtTheseLovingShelters from '../components/HelpOutAtTheseLovingShelters.vue'
import AdorableFriendsWaitingForAHome from '../components/AdorableFriendsWaitingForAHome.vue'
import Trends from '@/components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'
import PeopleYouMayKnow from '@/components/PeopleYouMayKnow.vue'

export default {
    name: 'trendview',

    components: {
    AdorableFriendsWaitingForAHome,
    HelpOutAtTheseLovingShelters,
    FeedItem,
    Trends,
    PeopleYouMayKnow
},

    data(){
        return {
            posts: [],
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: {
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true
        }
    },

    methods: {
    getFeed() {

        axios
            .get(`/api/posts/?trend=${this.$route.params.id}`)
            .then(response => {
                console.log('data', response.data)
                this.posts = response.data
            })
            .catch(error => {
                console.log('error', error)
            });
        }
    }
}
</script>
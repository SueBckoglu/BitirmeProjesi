<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg p-4 flex flex-col justify-center items-center text-center space-y-4">
                <h1 class="text-3xl font-bold text-pink-600">Tail Tales Terrace</h1>
                <p class="text-lg italic text-gray-600">"Until one has loved an animal, a part of one's soul remains unawakened." - Anatole France</p>
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <FeedForm 
                    v-bind:user="null" 
                    v-bind:posts="posts"
                />
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="post in posts"
                v-bind:key="post.id"
                >
                
                    <FeedItem v-bind:post="post" v-on:deletePost="deletePost"/>
            </div>

        </div>

        <div class="main-right col-span-1 space-y-4">
            
            <Trends />
            
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
import FeedForm from '@/components/FeedForm.vue'
import FeedItem from '../components/FeedItem.vue'
import Trends from '@/components/Trends.vue'
import PeopleYouMayKnow from '@/components/PeopleYouMayKnow.vue'

export default {
    name: 'FeedView',

    components: {
    AdorableFriendsWaitingForAHome,
    HelpOutAtTheseLovingShelters,
    FeedForm,
    FeedItem,
    Trends,
    PeopleYouMayKnow
},

    data(){
        return {
            posts: [],
            body: '',
        }
    },

    mounted() {
        this.getFeed()
    },

    methods: {
        getFeed() {
            axios
                .get('/api/posts/feed/')
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data

                })
                .catch(error => {
                    console.log('error', error)
                });
        },

        deletePost(id) {
            this.posts = this.posts.filter(post => post.id !== id)
        },
    }
}
</script>
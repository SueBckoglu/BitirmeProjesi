<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <!--<div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img src="https://i.pinimg.com/originals/88/17/25/881725dd36c94939ef455c26f9708b9d.jpg" class="mb-6 rounded-full" alt="profile picture">

                <p><strong>Sueda Bicaklioglu</strong></p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <p class="text-xs text-gray-500">2 pets</p>
                    <p class="text-xs text-gray-500">182 friends</p>
                    <p class="text-xs text-gray-500">120 posts</p>
                </div>
            </div>
        </div>-->

        <div class="main-center col-span-3 space-y-4">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4">
                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Got something to share ?"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach Image</a>

                        <button class="inline-block py-4 px-6 bg-pink-600 text-white rounded-lg">Post</button>
                    </div>
                </form>
            </div>

            <!--<div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="mb-6 flex items-center justify-between">
                    <div class="flex items-center space-x-6">
                        <img src="https://i.pinimg.com/originals/88/17/25/881725dd36c94939ef455c26f9708b9d.jpg" class="w-[40px] rounded-full" alt="profile pic">

                        <p><strong>Sueda Bicaklioglu</strong></p>
                    </div>

                    <p class="text-gray-600">18 minutes ago</p>
                </div>

                <img src="https://i.pinimg.com/originals/2b/80/4c/2b804cb8816ab1e4b765e2c45e2a4f08.jpg" class="w-full rounded-lg" alt="shared pic">


                <div class="my-6 flex justify-between">
                    <div class="flex space-x-6">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 0 1 1.04 0l2.125 5.111a.563.563 0 0 0 .475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 0 0-.182.557l1.285 5.385a.562.562 0 0 1-.84.61l-4.725-2.885a.562.562 0 0 0-.586 0L6.982 20.54a.562.562 0 0 1-.84-.61l1.285-5.386a.562.562 0 0 0-.182-.557l-4.204-3.602a.562.562 0 0 1 .321-.988l5.518-.442a.563.563 0 0 0 .475-.345L11.48 3.5Z" />
                            </svg>


                            <span class="text-gray-500 text-xs">82 likes</span>
                        </div>

                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 0 1-.825-.242m9.345-8.334a2.126 2.126 0 0 0-.476-.095 48.64 48.64 0 0 0-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0 0 11.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155" />
                            </svg>

                            <span class="text-gray-500 text-xs">0 comments</span>
                        </div>
                    </div>

                    <div>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" />
                        </svg>
                    </div>
                </div>
            </div>-->

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="post in posts"
                v-bind:key="post.id"
                >
                
                    <FeedItem v-bind:post="post"/>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            
            <AdorableFriendsWaitingForAHome/>

            <HelpOutAtTheseLovingShelters/>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
import HelpOutAtTheseLovingShelters from '../components/HelpOutAtTheseLovingShelters.vue'
import AdorableFriendsWaitingForAHome from '../components/AdorableFriendsWaitingForAHome.vue'
import FeedItem from '../components/FeedItem.vue'

export default {
    name: 'FeedView',

    components: {
    AdorableFriendsWaitingForAHome,
    HelpOutAtTheseLovingShelters,
    FeedItem
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
                .get('/api/posts/')
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data

                })
                .catch(error => {
                    console.log('error', error)
                });
        },

        submitForm() {
            console.log('submitForm', this.body)

            axios
                .post('/api/posts/create/', {
                    'body': this.body
                })
                .then(response => {
                    console.log('data', response.data)

                    this.posts.unshift(response.data)
                    this.body = ''

                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>
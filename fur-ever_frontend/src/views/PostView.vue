<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">

            <div class="bg-white border border-gray-200 rounded-lg p-4 flex flex-col justify-center items-center text-center space-y-4">
                <h1 class="text-3xl font-bold text-pink-600">PawTalk Plaza</h1> <!--"Paw Prints Discussion"-->
                <p class="text-lg italic text-gray-600">"To converse is to learn together." - Helen Keller</p>
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-if="post.id">
                
                    <FeedItem v-bind:post="post"/>
            </div>

            <div class="p-2 bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-2">
                        <textarea v-model="body" class="p-2 w-full bg-gray-100 rounded-lg" placeholder="Share your thoughts!"></textarea>
                    </div>

                    <div class="p-2 border-t border-gray-100 flex justify-between">
                        <a href="#" class="inline-block py-2 px-4 bg-gray-600 text-white rounded-lg">Fur-tograph</a>

                        <button class="inline-block py-2 px-4 bg-pink-600 text-white rounded-lg">Pawment</button>
                    </div>
                </form>
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="comment in post.comments"
                v-bind:key="comment.id"
            >
                <CommentItem v-bind:comment="comment" />
            </div>

        </div>

        <div class="main-right col-span-1 space-y-4">
            
            <Trends />
            
            <AdorableFriendsWaitingForAHome/>

            <HelpOutAtTheseLovingShelters/>,

            <PeopleYouMayKnow />

        </div>
        
    </div>
</template>

<script>
import axios from 'axios'
import HelpOutAtTheseLovingShelters from '../components/HelpOutAtTheseLovingShelters.vue'
import AdorableFriendsWaitingForAHome from '../components/AdorableFriendsWaitingForAHome.vue'
import FeedItem from '../components/FeedItem.vue'
import CommentItem from '@/components/CommentItem.vue'
import Trends from '@/components/Trends.vue'
import PeopleYouMayKnow from '@/components/PeopleYouMayKnow.vue'

export default {
    name: 'PostView',

    components: {
    AdorableFriendsWaitingForAHome,
    HelpOutAtTheseLovingShelters,
    FeedItem,
    CommentItem,
    Trends,
    PeopleYouMayKnow
},

    data(){
        return {
            post: {
                id: null,
                comments: []
            },
            body: '',
        }
    },

    mounted() {
        this.getPost()
    },

    methods: {
        getPost() {
            axios
                .get(`/api/posts/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.post = response.data.post

                })
                .catch(error => {
                    console.log('error', error)
                });
        },

        submitForm() {
            console.log('submitForm', this.body)

            axios
                .post(`/api/posts/${this.$route.params.id}/comment/`, {
                    'body': this.body
                })
                .then(response => {
                    console.log('data', response.data)

                    this.post.comments.push(response.data)
                    this.post.comments_count += 1
                    this.body = ''

                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>
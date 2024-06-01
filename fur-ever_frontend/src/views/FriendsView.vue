<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img src="https://i.pinimg.com/originals/88/17/25/881725dd36c94939ef455c26f9708b9d.jpg"
                    class="mb-6 rounded-full" alt="profile picture" />

                <p>
                    <strong>{{ user.name }}</strong>
                </p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <p class="text-xs text-gray-500">2 pets</p>
                    <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
                    <p class="text-xs text-gray-500">120 posts</p>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div class="p-4 bg-white border border-gray-200 rounded-lg" 
                v-if="friendshipRequests.length"
            >

                <h2 class="mb-6 text-xl">Friendship Requests</h2>

                <div class="p-4 flex items-center justify-center bg-gray-100 rounded-lg"
                    v-for="friendshipRequest in friendshipRequests" 
                    v-bind:key="friendshipRequest.id"
                >

                    <img src="https://i.pinimg.com/originals/b5/9f/f4/b59ff454de5ce126360313251634ae56.jpg"
                        style="width: 200px; height: auto" class="mr-4 rounded-full" alt="picture" />

                    <div>
                        <p class="mb-2">
                            <strong>
                                <RouterLink :to="{name: 'profile', params: { id: friendshipRequest.created_by.id },}">{{ friendshipRequest.created_by.name }}</RouterLink>
                            </strong>
                        </p>

                        <div class="mt-1 flex flex-col space-y-1">
                            <p class="text-xs text-gray-500">1 pets</p>
                            <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
                            <p class="text-xs text-gray-500">120 posts</p>
                        </div>

                        <div class="mt-6 space-x-2">
                            <button class="inline-block py-4 px-6 bg-pink-600 text-sm text-white rounded-lg" @click="handleRequest('accepted', friendshipRequest.created_by.id)">Accept</button>
                            <button class="inline-block py-4 px-6 bg-red-600 text-sm text-white rounded-lg" @click="handleRequest('rejected', friendshipRequest.created_by.id)">Reject</button>
                        </div>
                    </div>
                </div>
                <hr />
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-2 gap-4" 
                v-if="friends.length">

                <div 
                    class="p-4 text-center bg-gray-100 rounded-lg" 
                    v-for="user in friends" 
                    v-bind:key="user.id"
                >

                    <img src="https://i.pinimg.com/originals/b5/9f/f4/b59ff454de5ce126360313251634ae56.jpg" class="mb-6 rounded-full" alt="picture" />

                    <p>
                        <strong>
                            <RouterLink :to="{ name: 'profile', params: { id: user.id } }">{{ user.name }}</RouterLink>
                        </strong>
                    </p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">1 pets</p>
                        <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
                        <p class="text-xs text-gray-500">120 posts</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <AdorableFriendsWaitingForAHome />

            <HelpOutAtTheseLovingShelters />
        </div>
    </div>
</template>

<script>
import axios from "axios";
import HelpOutAtTheseLovingShelters from "../components/HelpOutAtTheseLovingShelters.vue";
import AdorableFriendsWaitingForAHome from "../components/AdorableFriendsWaitingForAHome.vue";
import FeedItem from "../components/FeedItem.vue";
import { useUserStore } from "@/stores/user";


export default (await import("vue")).defineComponent({
    name: "FriendsView",

    setup() {
        const userStore = useUserStore()

        return {
            userStore,
        };
    },

    components: {
        AdorableFriendsWaitingForAHome,
        HelpOutAtTheseLovingShelters,
    },

    data() {
        return {
            user: {},
            friendshipRequests: [],
            friends: [],
        };
    },

    mounted() {
        this.getFriends();
    },

    methods: {
        getFriends() {
            axios
                .get(`/api/friends/${this.$route.params.id}/`)
                .then((response) => {
                    console.log("data", response.data);

                    this.friendshipRequests = response.data.requests;
                    this.friends = response.data.friends;
                    this.user = response.data.user;
                })
                .catch((error) => {
                    console.log("error", error);
                })
        },

        handleRequest(status, pk)  {
            console.log('handleRequest', status)

            axios
                .post(`/api/friends/${pk}/${status}/`)
                .then(response => {
                    console.log('data', response.data)
                })
                .catch((error) => {
                    console.log("error", error);
                })
        }
    },
});
</script>

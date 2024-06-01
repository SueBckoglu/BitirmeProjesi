<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1 space-y-4">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img :src="user.get_avatar" class="mb-6 rounded-full" alt="profile picture" />

                <p>
                    <strong>{{ user.name }}</strong>
                </p>

                <!--<p class="text-sm italic text-gray-600 border border-gray-200 rounded-lg">User</p>-->

                <div class="mt-6 flex space-x-8 justify-around">
                    <RouterLink :to="{ name: 'profile', params: { id: user.id } }" class="text-xs text-gray-500">{{
                        user.friends_count }} friends</RouterLink>
                    <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p>
                </div>

                <div>
                    <!--Share your story, if you add-->
                </div>

                <div class="mt-6 space-x-6 flex flex-wrap justify-center">
                    <button class="grid justify-center inline-block py-4 px-6 bg-pink-600 text-sm text-white rounded-lg"
                        @click="sendFriendshipRequest" v-if="userStore.user.id !== user.id && can_send_friendship_request">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="size-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z" />
                            </svg>
                            <span>Paw-tner Up</span>
                        </div>
                    </button>

                    <button
                        class="grid justify-center mt-4 inline-block py-4 px-6 bg-pink-600 text-sm text-white rounded-lg"
                        @click="sendDirectMessage" v-if="userStore.user.id !== user.id">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="size-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 0 1-.825-.242m9.345-8.334a2.126 2.126 0 0 0-.476-.095 48.64 48.64 0 0 0-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0 0 11.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155" />
                            </svg>

                            <span>Whisker Whisper</span>
                        </div>
                    </button>

                    <RouterLink class="inline-block py-4 px-6 bg-pink-600 text-sm text-white rounded-lg" to="/profile/edit"
                        v-if="userStore.user.id === user.id">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="size-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Zm6-10.125a1.875 1.875 0 1 1-3.75 0 1.875 1.875 0 0 1 3.75 0Zm1.294 6.336a6.721 6.721 0 0 1-3.17.789 6.721 6.721 0 0 1-3.168-.789 3.376 3.376 0 0 1 6.338 0Z" />
                        </svg>
                    </RouterLink>

                    <button class="inline-block py-4 px-6 bg-red-600 text-sm text-white rounded-lg" @click="logout"
                        v-if="userStore.user.id === user.id">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="size-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M5.636 5.636a9 9 0 1 0 12.728 0M12 3v9" />
                        </svg>
                    </button>
                </div>
            </div>

            <div class="col-span-1 space-y-4">
                <div class="p-4 bg-white border border-gray-200 rounded-lg">
                    <div class="grid grid-cols-2 text-center">
                        <h3 class="mb-6 text-xl">My Pets</h3>
                    </div>

                    <div class="space-y-4">
                        <div class="flex items-center justify-between">
                            <div class="flex items-center space-x-2">
                                <img src="https://i.pinimg.com/originals/67/7c/6f/677c6fb31ffa3f09248a600ea85105cf.jpg" class="w-[40px] rounded-full" alt="pet.name" />
                                <RouterLink to="/animalprofile" class="text-xs"><strong>Meredith</strong></RouterLink>
                            </div>
                        </div>
                    </div>
                    <div class="space-y-4">
                        <div v-for="pet in pets" :key="pet.id" class="flex items-center justify-between">
                            <div class="flex items-center space-x-2">
                                <img :src="pet.image" class="w-[40px] rounded-full" :alt="pet.name" />
                                <RouterLink :to="{ name: 'animalprofile', params: { id: pet.id }}" class="text-xs text-gray-500">{{ pet.name }}</RouterLink>
                            </div>
                        </div>
                    </div>
            </div>

                <div>
                    <!--Gönüllülüklerim-->
                    <div class="p-4 bg-white border border-gray-200 rounded-lg">
                        <h3 class="mb-6 text-xl">My Volunteerings</h3>
                        <!--Sadece bilgilendirme, veri alıyor ilgili Volunteer sayfasından-->
                        <div class="space-y-4">
                            <div class="flex items-center justify-between">
                                <p class="text-xs">
                                    <strong>Walking</strong><br />
                                    <!--Etkinliğin ismi-->
                                    <span class="text-gray-500">PawGuard Shelter</span>
                                    <!--Düzenleyenin adı; barınak adı, kullanıcı adı-->
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <!--Bağışlarım-->
                    <div class="p-4 bg-white border border-gray-200 rounded-lg">
                        <h3 class="mb-6 text-xl">My Donations</h3>
                        <!--Sadece bilgilendirme, veri alıyor ilgili Donation sayfasından-->
                        <div class="space-y-4">
                            <div class="flex items-center justify-between">
                                <p class="text-xs">
                                    <strong>PetAngels Shelter</strong><br />
                                    <!--Bağış yapılan yer-->
                                    <span class="text-gray-500">180 posts</span>
                                    <!--Bağış tutarı-->
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
            <div class="main-center col-span-2 space-y-4">
                <div class="p-4 bg-white border border-gray-200 rounded-lg" v-if="userStore.user.id === user.id">
                    <FeedForm v-bind:user="user" v-bind:posts="posts" />
                </div>

                <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" v-bind:key="post.id">
                    <FeedItem v-bind:post="post" v-on:deletePost="deletePost" />
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

<style>
input[type="file"] {
    display: none;
}

.custom-file-upload {
    border: 1px solid #ccc;
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
}
</style>

<script>
import axios from "axios";
import HelpOutAtTheseLovingShelters from "../components/HelpOutAtTheseLovingShelters.vue";
import AdorableFriendsWaitingForAHome from "../components/AdorableFriendsWaitingForAHome.vue";
import FeedForm from "../components/FeedForm.vue";
import FeedItem from "../components/FeedItem.vue";
import { useUserStore } from "@/stores/user";
import { RouterLink } from "vue-router";
import { useToastStore } from "@/stores/toast";
import Trends from "@/components/Trends.vue";
import PeopleYouMayKnow from "@/components/PeopleYouMayKnow.vue";

export default {
    name: "ProfileView",

    setup() {
        const userStore = useUserStore();
        const toastStore = useToastStore();

        return {
            userStore,
            toastStore,
            pets: [],
        };
    },

    components: {
        AdorableFriendsWaitingForAHome,
        HelpOutAtTheseLovingShelters,
        FeedForm,
        FeedItem,
        RouterLink,
        Trends,
        PeopleYouMayKnow,
    },

    data() {
        return {
            posts: [],
            user: {
                id: "",
            },
            can_send_friendship_request: null,
        };
    },

    mounted() {
        this.getFeed();
        this.getPets();
    },

    watch: {
        "$route.params.id": {
            handler: function () {
                this.getFeed();
            },
            deep: true,
            immediate: true,
        },
    },

    methods: {
        deletePost(id) {
            this.posts = this.posts.filter((post) => post.id !== id);
        },

        sendDirectMessage() {
            console.log("sendDirectMessage");

            axios
                .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
                .then((response) => {
                    console.log(response.data);

                    this.$router.push("/chat");
                })
                .catch((error) => {
                    console.log("error", error);
                });
        },

        sendFriendshipRequest() {
            axios
                .post(`/api/friends/${this.$route.params.id}/request/`)
                .then((response) => {
                    console.log("data", response.data);

                    this.can_send_friendship_request = false;

                    if (response.data.message == "request already sent") {
                        this.toastStore.showToast(
                            5000,
                            "The request has already been sent!",
                            "bg-red-300"
                        );
                    } else {
                        this.toastStore.showToast(
                            5000,
                            "The request was sent!",
                            "bg-emerald-300"
                        );
                    }
                })
                .catch((error) => {
                    console.log("error", error);
                });
        },

        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then((response) => {
                    console.log("data", response.data);

                    this.posts = response.data.posts;
                    this.user = response.data.user;
                    this.can_send_friendship_request =
                        response.data.can_send_friendship_request;
                })
                .catch((error) => {
                    console.log("error", error);
                });
        },

        getPets() {
            axios
                .get(`/api/list-pet/`) // Fetch all pets from the API
                .then((response) => {
                    console.log("Pets data", response.data);
                    this.pets = response.data; // Assign the fetched pets to the component data
                })
                .catch((error) => {
                    console.log("Error fetching pets", error);
                });
        },

        logout() {
            console.log("Log out");

            this.userStore.removeToken();

            this.$router.push("/foryou");
        },
    },
};
</script>

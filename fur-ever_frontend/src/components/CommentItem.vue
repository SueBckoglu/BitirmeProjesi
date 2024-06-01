<template>
    <div class="mb-6 flex items-center justify-between">
        <div class="flex items-center space-x-6">
            <img :src="comment.created_by.get_avatar" class="w-[40px] rounded-full" alt="profile pic" />

            <p>
                <strong>
                    <RouterLink v-if="comment && comment.created_by" :to="{ name: 'profile', params: { id: comment.created_by.id } }">{{ comment.created_by.name }}</RouterLink>
                </strong>
            </p>
        </div>

        <p class="text-gray-600">{{ comment.created_at_formatted }} ago</p>
    </div>

    <p>{{ comment.body }}</p>

    <div class="my-6 flex justify-between">
        <div class="flex space-x-6">
            <div class="flex items-center space-x-2 text-green-600" @click="likeComment(comment.id)">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.182 15.182a4.5 4.5 0 0 1-6.364 0M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0ZM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Z" />
                </svg>

                <span v-if="comment" class="text-gray-500 text-xs">{{ comment.likes_count }} Paws Up</span>
            </div>
            <div class="flex items-center space-x-2 text-red-600" @click="dislikeComment(comment.id)">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.182 16.318A4.486 4.486 0 0 0 12.016 15a4.486 4.486 0 0 0-3.198 1.318M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0ZM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Z" />
                </svg>

                <span v-if="comment" class="text-gray-500 text-xs">{{ comment.dislikes_count }} Paws Down</span>
            </div>
        </div>

        <div>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" />
            </svg>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';

export default {
    props: {
        comment: Object
    },
    
    methods: {
        likeComment(id) {
            axios
                .post(`/api/comment/${id}/like/`)
                .then(response => {
                if (response.data.message == 'Comment liked successfully') {
                    this.comment.likes_count += 1;
                }
            })
                .catch(error => {
                console.log('error', error);
            });
        },
        dislikeComment(id) {
            axios
                .post(`/api/comment/${id}/dislike/`)
                .then(response => {
                if (response.data.message == 'Comment disliked successfully') {
                    this.comment.dislikes_count += 1;
                }
            })
                .catch(error => {
                console.log('error', error);
            });
        }
    },
    
    components: { RouterLink }
}
</script>

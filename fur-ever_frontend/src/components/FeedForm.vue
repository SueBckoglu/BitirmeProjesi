<template>
    <form v-on:submit.prevent="submitForm" method="post">
        <div class="p-4 flex">
            <textarea v-model="body" class="flex-1 p-4 mr-4 bg-gray-100 rounded-lg" placeholder="Got something to share ?"></textarea>

            <div id="preview" v-if="url">
                <img :src="url" alt="preview" class="w-[100px] rounded-xl">
            </div>
        </div>

        <div class="p-2 border-t border-gray-100 flex justify-between">
            <label class="inline-block py-2 px-4 rounded-lg">
                <input type="checkbox" v-model="is_private"> Just Between Us<input/>
            </label>
        </div>

        <div class="p-4 border-t border-gray-100 flex justify-between">
            <label class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">
                <input type="file" ref="file" @change="onFileChange">
                    Fur-tograph
            </label>

            <button class="inline-block py-4 px-6 bg-pink-600 text-white rounded-lg">Paw-st</button>
        </div>
    </form>
</template>

<script>
import axios from 'axios'

export default {
    props: {
        user: Object,
        posts: Array
    },

    data() {
        return {
            body: '',
            is_private: false,
            url: null,
        }
    },

    methods: {
        submitForm() {
            console.log('submitForm', this.body)

            let formData = new FormData()
            formData.append('image', this.$refs.file.files[0])
            formData.append('body', this.body)
            formData.append('is_private', this.is_private)

            axios
                .post('/api/posts/create/', formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        }
                    }) 
                .then(response => {
                    console.log('data', response.data)

                    this.posts.unshift(response.data)
                    this.body = ''
                    this.is_private = false,
                    this.$refs.file.value = null
                    this.url = null
                    
                    if (this.user) {
                        this.user.posts_count += 1
                    }

                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>
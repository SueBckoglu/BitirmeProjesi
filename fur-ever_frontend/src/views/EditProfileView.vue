<template>
    <div class="mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Edit your Paw-rofile</h1>
                <p class="mb-6 text-gray-500">
                    🐾 Welcome to Your Paw-fect Space!
                    <br>Hey there, pet lover! 🐶🐱 Are you ready to add a sprinkle of paw-some personality to your profile? Here’s your chance to make your space as unique and charming as your furry companions!
                    <br>
                    <br>🌟 What Can You Do Here?
                    <br>
                    <br>Change Your Name: Want to go by a different nickname? Feel free to update it here!
                    <br>Switch Up Your Email: Whether it’s a new inbox or just a fresh start, you can change your email anytime.
                    <br>Update Your Profile Pic: Time for a new look? Upload a cute and cuddly profile picture!
                    <br>Password Pawsword: Keep your account secure by changing your password whenever you need.
                    <br>Add Your Fur Babies: Show off your adorable pets by adding their photos and details to your profile.
                    <!--<br>Share Your Story: Let the world know more about you and your furry friends by adding a short bio.-->
                    <!--<br>Connect on Social: Share your pet adventures by linking your Instagram or other social media accounts.-->
                    <br>
                    <br>🌈 Why Wait? Dive In!
                    <br>
                    <br>Your profile is like a canvas waiting to be painted with paw-prints of love and joy. So, go ahead, unleash your creativity, and let’s make your Paw-rofile shine! 🎨💫
                    <br>
                    <br>Ready to get started? Let’s make your Paw-rofile paw-sitively purr-fect! 🐾
                </p>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label for="">Name</label><br>
                        <input type="text" v-model="form.name" placeholder="Your Full Name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"> 
                    </div>

                    <div>
                        <label for="">E-mail</label><br>
                        <input type="email" v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"> 
                    </div>

                    <div>
                        <div>
                            <label>Upload Photo</label><br>
                            <input type="file" ref="file">
                        </div>
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <RouterLink to="/profile/edit/password" class="justify-center mt-4 inline-block py-4 px-6 bg-pink-600 text-sm text-white rounded-lg">
                            <div class="flex items-center space-x-2">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 5.25a3 3 0 0 1 3 3m3 0a6 6 0 0 1-7.029 5.912c-.563-.097-1.159.026-1.563.43L10.5 17.25H8.25v2.25H6v2.25H2.25v-2.818c0-.597.237-1.17.659-1.591l6.499-6.499c.404-.404.527-1 .43-1.563A6 6 0 1 1 21.75 8.25Z" />
                                </svg>
                                Edit password
                            </div>
                        </RouterLink>
                    </div>

                    <div>
                        <button class="py-4 px-6 bg-pink-600 text-white rounded-lg">Save changes</button>
                    </div>
                </form>
            </div>

            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h2 class="mb-6 text-2xl">Add Furbaby</h2>
                <p>Don't forget your furry friend's passport! We need some info from them too.</p>
                <div>
                        <RouterLink to="/signupanimal" class="justify-center mt-4 inline-block py-4 px-6 bg-pink-600 text-sm text-white rounded-lg">
                            <div class="flex items-center space-x-2">
                                Let's begin
                            </div>
                        </RouterLink>
                    </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const toastStore = useToastStore()
        const userStore = useUserStore()

        return {
            toastStore,
            userStore,
        }
    },

    components: {

    },

    data() {
        return {
            form: {
                email: this.userStore.user.email,
                name: this.userStore.user.name,
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing...')
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing...')
            }

            if (this.errors.length === 0) {
                let formData = new FormData()
                formData.append('avatar', this.$refs.file.files[0])
                formData.append('name', this.form.name)
                formData.append('email', this.form.email)

                axios
                    .post('/api/editprofile/', formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        }
                    })
                    .then(response => {
                        if (response.data.message === 'information updated') {
                            this.toastStore.showToast(5000, 'The Information was saved', 'bg-emerald-500')

                            this.userStore.setUserInfo({
                                id: this.userStore.user.id,
                                name: this.form.name,
                                email: this.form.email,
                                avatar: response.data.user.get_avatar
                            })

                            this.$router.back()
                        } else {
                            this.toastStore.showToast(5000, `${response.data.message}. Please try again`, 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>
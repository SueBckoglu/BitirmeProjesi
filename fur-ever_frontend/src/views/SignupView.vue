<template>
    <div class="mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Sign up</h1>
                <p class="mb-6 text-gray-500">
                    Welcome to our pet-loving family! 🐾 
                    Ready to embark on a journey of furry fun and paw-some adventures? 🌟 
                    Sign up now to unlock a world of tail-wagging delights! 🐶 
                    Create a personalized profile for your beloved pet, schedule appointments with ease, and discover a treasure trove of pet care tips and tricks tailored just for you. 🐾 
                    Plus, gain access to exclusive events and special offers that will make your pet's tail wag with excitement! 🎉 
                    Join our community of animal enthusiasts and let's make every moment with our pets unforgettable! 🐾💖
                </p>
                <p class="font-bold">
                    Already have an account ? <RouterLink to="/login" class="underline">Click here</RouterLink> to log in!
                </p>
            </div>
        </div>

        <div class="main-right">
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
                        <label for="">Password</label><br> 
                        <input type="password" v-model="form.password1" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label for="">Confirm Password</label><br>
                        <input type="password" v-model="form.password2" placeholder="Confirm your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="error.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-pink-600 text-white rounded-lg">Sign up</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { useToastStore } from '@/stores/toast'
import axios from 'axios';

export default {
    setup(){
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm(){
            this.errors = []

            if (this.form.email === ''){
                this.errors.push('Your email is missing')
            }

            if (this.form.name === ''){
                this.errors.push('Your name is missing')
            }

            if (this.form.password1 === ''){
                this.errors.push('Your password is missing')
            }

            if (this.form.password1 !== this.form.password2){
                this.errors.push('The password does not match')
            }
            
            if (this.errors.length === 0){
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success'){
                             this.toastStore.showToast(5000, 'Welcome to the Fur-Ever Friends adventure! Please log in to keep spreading love and care to our furry pals.', 'bg-emerald-500')

                             this.form.email = ''
                             this.form.name = ''
                             this.form.password1 = ''
                             this.form.password2 = ''
                        } else {
                            this.errors = response.data.errors;
                            this.toastStore.showToast(5000, 'Oops! Something went paws-up. Could you please give it another try?', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                        this.toastStore.showToast(5000, 'An error occurred during signup. Please try again later.', 'bg-red-300')
                    })
            }
        }
    }

}
</script>
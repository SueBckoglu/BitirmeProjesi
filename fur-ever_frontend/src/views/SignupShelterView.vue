<template>
    <div class="mx-auto max-w-7xl grid grid-cols-2 gap-8 py-12">
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
                    Already have an account? <RouterLink to="/login" class="underline">Click here</RouterLink> to log in!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <div class="mb-6">
                    <p class="font-bold">
                        Are you a shelter manager looking to create a shelter profile? <RouterLink to="/signupshelter" class="underline">Click here</RouterLink> to get started!
                    </p>
                </div>

                <form class="space-y-6" @submit.prevent="submitForm">
                    <div>
                        <label for="name" class="block font-medium">Name</label>
                        <input type="text" v-model="form.name" placeholder="Your Full Name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"> 
                    </div>

                    <div>
                        <label for="email" class="block font-medium">E-mail</label>
                        <input type="email" v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"> 
                    </div>

                    <div>
                        <label for="workers" class="block font-medium">How many workers do you have?</label>
                        <input type="number" v-model="form.worker" placeholder="Workers" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"> 
                    </div>

                    <div>
                        <label for="shelteranimal" class="block font-medium">How many animals do you have?</label>
                        <input type="number" v-model="form.shelteranimal" placeholder="Animals" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"> 
                    </div>

                    <div>
                        <label for="password1" class="block font-medium">Password</label>
                        <input type="password" v-model="form.password1" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label for="password2" class="block font-medium">Confirm Password</label>
                        <input type="password" v-model="form.password2" placeholder="Confirm your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" :key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button type="submit" class="w-full py-4 px-6 bg-pink-600 text-white rounded-lg">Sign up</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { useToastStore } from '@/stores/toast';

export default {
    setup() {
        const toastStore = useToastStore();

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
                password2: '',
                worker: '',
                shelteranimal: '',
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
                this.errors.push('Your name is missing...')
            }

            if (this.form.worker === ''){
                this.errors.push('Your workers field is missing...')
            }

            if (this.form.shelteranimal === ''){
                this.errors.push('Your animal field is missing...')
            }

            if (this.form.password1 === ''){
                this.errors.push('Your password is missing...')
            }

            if (this.form.password1 !== this.form.password2){
                this.errors.push('The passwords does not match!')
            }

            if (this.errors.length === 0) {
                axios
                .post('/api/shelter_profile/create/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'Welcome to the Fur-Ever Friends adventure! Do not forget to activate your account to keep spreading love and care to our furry pals.', 'bg-emerald-500')
                            this.form.email = '';
                            this.form.name = '';
                            this.form.worker = '';
                            this.form.shelteranimal = '';
                            this.form.password1 = '';
                            this.form.password2 = '';

                            this.$router.push('/login')
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }
                            
                            this.toastStore.showToast(5000, 'Oops! Something went paws-up. Could you please give it another try?', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                        this.toastStore.showToast(5000, 'An error occurred during signup. Please try again later.', 'bg-red-300')
                    })
        
                }
            },
    },
}
</script>


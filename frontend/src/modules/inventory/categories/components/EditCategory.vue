<template>
    <div class="page-edit-category">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/categories">Categories</router-link></li>
                <li><router-link :to="{ name: 'Category', params: { id: category.id }}">{{ category.name }}</router-link></li>
                <li class="is-active"><router-link :to="{ name: 'CategoryEdit', params: { id: category.id }}" aria-current="true">Edit</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit - {{ category.name }}</h1>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label>Name</label>
                    
                    <div class="control">
                        <input type="text" name="name" class="input" v-model="category.name">
                    </div>
                </div>


            <div class="column is-12">
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="submitForm">Save changes</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'EditCategory',
    data() {
        return {
            category: {}
        }
    },
    mounted() {
        this.getCategory()
    },
    methods: {
        getCategory() {
            const categoryID = this.$route.params.id

            axios
                .get(`/api/v1/categories/${categoryID}`)
                .then(response => {
                    this.category = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        submitForm() {
            const categoryID = this.$route.params.id

            axios
                .patch(`/api/v1/categories/${categoryID}/`, this.category)
                .then(response => {
                    toast({
                        message: 'The changes was saved',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                    
                    this.$router.push('/categories')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
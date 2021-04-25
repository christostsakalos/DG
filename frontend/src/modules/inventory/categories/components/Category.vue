<template>
    <div class="page-category">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/categories">Categories</router-link></li>
                <li><router-link :to="{ name: 'Category', params: { id: category.id }}">{{ category.name }}</router-link></li>
            </ul>
        </nav>
        <div class="columns is-centered">
            <div class="column is-4">
                <h1 class="title">{{ category.name }}</h1>

                 <router-link :to="{ name: 'CategoryEdit', params: { id: category.id }}" class="button is-light mt-4">Edit Category</router-link>
                 <br>
                 <router-link :to="{ name: 'CategoryDelete', params: { id: category.id }}" class="button is-danger mt-4">Delete Category</router-link>
            </div>

            <div class="column is-4">
                <h2 class="subtitle">Category details</h2>

                                           <div class="table-container"> <h2 class="subtitle">Sub Categories: </h2>
                <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                    <thead>
                    <tr class="th">
                        <th>Name</th>
                    </tr></thead>

                    <tbody>
                    <tr  v-for="categories in sub_categories" v-bind:key="categories.id">
                        <td class="table is-narrow">{{ categories.name }}</td>
                    </tr>
               </tbody>
                </table>
 
            </div>
            </div>

        </div>
      


    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Category',
    data () {
        return {
            category: {},
            sub_categories: []
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
                    for (let i = 0; i < response.data.sub_categories.length; i++) {
                        this.sub_categories.push(response.data.sub_categories[i])}
                    console.log(this.sub_categories)
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
<template>
    <div class="page-subcategory">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/categories">Categories</router-link></li>
                <li><router-link :to="{ name: 'Subcategory', params: { id: subcategory.id }}">{{ subcategory.name }}</router-link></li>
            </ul>
        </nav>
        <div class="columns is-centered">
            <div class="column is-4">
                <h1 class="title">{{ subcategory.name }}</h1>

                 <router-link :to="{ name: 'SubcategoryEdit', params: { id: subcategory.id }}" class="button is-light mt-4">Edit Subcategory</router-link>
                 <br>
                 <router-link :to="{ name: 'SubcategoryDelete', params: { id: subcategory.id }}" class="button is-danger mt-4">Delete Subcategory</router-link>
            </div>

            <div class="column is-4">
                <h2 class="subtitle">Parent category name</h2>

                <div class="table-container"> <h2 class="subtitle"><strong>{{subcategory.parent_name}}</strong></h2>
            </div>
            </div>

        </div>
      


    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Subcategory',
    data () {
        return {
            subcategory: {},
        }
    },
    mounted() {
        this.getSubcategory()
    },
    methods: {
        getSubcategory() {
            const subcategoryID = this.$route.params.id

            axios
                .get(`/api/v1/subcategories/${subcategoryID}`)
                .then(response => {

                    this.subcategory = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
<template>
    <div class="page-part">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/categories">Categories</router-link></li>
                <li><router-link :to="{ name: 'Part', params: { id: part.id }}">{{ part.name }}</router-link></li>
            </ul>
        </nav>
        <div class="columns is-centered">
            <div class="column is-4">
                <h1 class="title">{{ part.name }}</h1>

                 <router-link :to="{ name: 'PartEdit', params: { id: part.id }}" class="button is-light mt-4">Edit Part</router-link>
                 <br>
                 <router-link :to="{ name: 'PartDelete', params: { id: part.id }}" class="button is-danger mt-4">Delete Part</router-link>
            </div>

            <div class="column is-4">
                <h2 class="subtitle">Category</h2>

                <div class="table-container"> <h2 class="subtitle"><strong>{{part.category_name}}</strong></h2>
                <p>Name: <strong>{{part.name}}</strong></p>
                <p>Description: {{part.description}}</p>
                <p>Quantity: {{part.quantity}}</p>
            </div>
            </div>

        </div>
      


    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Part',
    data () {
        return {
            part: {},
        }
    },
    mounted() {
        this.getPart()
    },
    methods: {
        getPart() {
            const partID = this.$route.params.id

            axios
                .get(`/api/v1/parts/${partID}`)
                .then(response => {

                    this.part = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
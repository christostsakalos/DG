<template>
    <div class="page-customer">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/customers">Customers</router-link></li>
                <li><router-link :to="{ name: 'Customer', params: { id: customer.id }}">{{ customer.first_name }} {{  customer.last_name}}</router-link></li>
            </ul>
        </nav>
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ customer.first_name }} {{ customer.last_name }}</h1>

                 <router-link :to="{ name: 'CustomerEdit', params: { id: customer.id }}" class="button is-light mt-4">Edit</router-link>
                 <br>
                 <router-link :to="{ name: 'CustomerDelete', params: { id: customer.id }}" class="button is-danger mt-4">Delete</router-link>
            </div>

            <div class="column is-12">
                <h2 class="subtitle">Customer details</h2>

                <p><strong>{{ customer.email }}</strong></p>
                
                <p v-if="customer.address">{{ customer.address }}</p>
                <p v-if="customer.city">{{ customer.city }}</p>
                <p v-if="customer.postcode || customer.country">{{ customer.postcode }} {{ customer.country }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Customer',
    data () {
        return {
            customer: {}
        }
    },
    mounted() {
        this.getCustomer()
    },
    methods: {
        getCustomer() {
            const customerID = this.$route.params.id

            axios
                .get(`/api/v1/customers/${customerID}`)
                .then(response => {
                    this.customer = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
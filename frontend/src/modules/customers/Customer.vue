<template>
    <div class="page-customer">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/customers">Customers</router-link></li>
                <li><router-link :to="{ name: 'Customer', params: { id: customer.id }}">{{ customer.first_name }} {{  customer.last_name}}</router-link></li>
            </ul>
        </nav>
        <div class="columns is-centered">
            <div class="column is-4">
                <h1 class="title">{{ customer.first_name }} {{ customer.last_name }}</h1>

                 <router-link :to="{ name: 'CustomerEdit', params: { id: customer.id }}" class="button is-light mt-4">Edit Customer</router-link>
                 <br>
                 <router-link :to="{ name: 'CustomerDelete', params: { id: customer.id }}" class="button is-danger mt-4">Delete Customer</router-link>
            </div>

            <div class="column is-4">
                <h2 class="subtitle">Customer details</h2>

                <p><strong>{{ customer.email }}</strong></p>
                
                <p v-if="customer.address">{{ customer.address }}</p>
                <p v-if="customer.city">{{ customer.city }}</p>
                <p v-if="customer.postcode || customer.country">{{ customer.postcode }} {{ customer.country }}</p>
            </div>

        </div>
        <div class="columns is-centered">
   
           
                            <div class="table-container"> <h2 class="subtitle">Owned vehicles: </h2>
                <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                    <thead>
                    <tr class="th">
                        <th>Make</th>
                        <th>Model</th>
                        <th>Vehicle Registration number</th>
                        <th>Fuel Type</th>
                        <th>Colour</th>
                    </tr></thead>

                    <tbody>
                    <tr  v-for="vehicle in owned_vehicles" v-bind:key="vehicle.id">
                        <td class="table is-narrow">{{ vehicle.make }}</td>
                        <td class="table is-narrow">{{ vehicle.model }}</td>
                        <td class="table is-narrow">{{ vehicle.vehicleregistrationnumber }}</td>
                        <td class="table is-narrow">{{ vehicle.fueltype }}</td>
                        <td class="table is-narrow">{{ vehicle.colour }}</td>
<!--                         <td class="table is-narrow"><router-link :to="{ name: 'Customer', params: { id: customer.id }}" class="button is-info">View</router-link>
                        <router-link :to="{ name: 'CustomerEdit', params: { id: customer.id }}" class="button is-link">Edit</router-link>
                        <button class="button is-danger" @click="Deletecustomer(customer.id)">Delete</button></td> -->
                    </tr>
               </tbody>
                </table>
 
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
            customer: {},
            owned_vehicles: []
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
                    for (let i = 0; i < response.data.owned_vehicles.length; i++) {
                        this.owned_vehicles.push(response.data.owned_vehicles[i])}
                    console.log(this.owned_vehicles)
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
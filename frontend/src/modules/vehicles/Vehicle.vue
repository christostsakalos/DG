<template>
    <div class="page-vehicle">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/vehicles">Vehicles</router-link></li>
                <li><router-link :to="{ name: 'Vehicle', params: { id: vehicle.id }}">{{ vehicle.make }} {{  vehicle.model}}</router-link></li>
            </ul>
        </nav>
        <div class="columns is-centered">
            <div class="column is-4">
                <h1 class="title">{{ vehicle.make }} {{  vehicle.model}}</h1>

                 <router-link :to="{ name: 'VehicleEdit', params: { id: vehicle.id }}" class="button is-light mt-4">Edit Vehicle</router-link>
                 <br>
                 <router-link :to="{ name: 'VehicleDelete', params: { id: vehicle.id }}" class="button is-danger mt-4">Delete Vehicle</router-link>
            </div>

            <div class="column is-4">
                <h2 class="subtitle">Vehicle details</h2>

                <p><strong>{{ vehicle.vehicleregistrationnumber }}</strong></p><br>
                <p><strong>{{ vehicle.fueltype }}</strong></p><br>
                <p><strong>{{ vehicle.colour }}</strong></p>
            </div>
                        <div class="column is-4">
                <h2 class="subtitle">Vehicle owner:</h2>

                <p><strong>{{ vehicle.first_name }}</strong></p><br>
                <p><strong>{{ vehicle.last_name }}</strong></p>
            </div>
        </div>
        <div class="columns is-centered">
   
           
<!--                             <div class="table-container"> <h2 class="subtitle">Vehicle Owner: </h2>
                <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                    <thead>
                    <tr class="th">
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                    </tr></thead>

                    <tbody>
                    <tr  v-for="vehicle in owned_vehicles" v-bind:key="vehicle.id">
                        <td class="table is-narrow">{{ vehicle.make }}</td>
                        <td class="table is-narrow">{{ vehicle.model }}</td>
                        <td class="table is-narrow">{{ vehicle.vehicleregistrationnumber }}</td>
                        <td class="table is-narrow">{{ vehicle.fueltype }}</td>
                        <td class="table is-narrow">{{ vehicle.colour }}</td>
                    </tr>
               </tbody>
                </table>
 
            </div>-->
            </div> 
      


    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Vehicle',
    data () {
        return {
            vehicle: {},
            owner: []
        }
    },
    mounted() {
        this.getVehicle()
    },
    methods: {
        getVehicle() {
            const vehicleID = this.$route.params.id

            axios
                .get(`/api/v1/vehicles/${vehicleID}`)
                .then(response => {

                    this.vehicle = response.data
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
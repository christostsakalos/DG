<template>
    <div class="page-jobsheet">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li><router-link to="/jobsheets">Jobsheets</router-link></li>
                <li><router-link :to="{ name: 'Jobsheet', params: { id: jobsheet.id }}">Job {{ jobsheet.reference_number }}</router-link></li>
            </ul>
        </nav>
        <div class="columns is-centered">
            <div class="column is-4">
                <h1 class="title">{{ jobsheet.first_name }} {{ jobsheet.last_name }}</h1>
                <button @click="setAsPaid()" class="button is-success mt-4" v-if="!jobsheet.paid">Set as paid</button><br>
                 <router-link :to="{ name: 'JobsheetEdit', params: { id: jobsheet.id }}" class="button is-light mt-4">Edit Jobsheet</router-link>
                 <br>
                 <router-link :to="{ name: 'JobsheetDelete', params: { id: jobsheet.id }}" class="button is-danger mt-4">Delete Jobsheet</router-link>
            </div>

            <div class="column is-4">
                <h2 class="subtitle">Jobsheet Details</h2>

                <p><strong>{{ jobsheet.make }}</strong></p><br>
                <p><strong>{{ jobsheet.model }}</strong></p><br>
                <p><strong>{{ jobsheet.vehicleregistrationnumber }}</strong></p>
                <p><strong>{{ jobsheet.notes }}</strong></p>
            </div>
                        <div class="column is-4">
                <h2 class="subtitle">Status</h2>

                <p>Paid: <strong> {{ getStatusLabel() }}</strong></p><br>
                <p>Remaining:<strong>{{ jobsheet.remaining }}£</strong></p>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast';
export default {
    name: 'Jobsheet',
    data () {
        return {
            jobsheet: {}
        }
    },
    mounted() {
        this.getJobsheet()
    },
    methods: {
        getJobsheet() {
            const jobsheetID = this.$route.params.id

            axios
                .get(`/api/v1/jobsheets/${jobsheetID}`)
                .then(response => {
                    this.jobsheet = response.data})
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
                    getStatusLabel() {
                if (this.jobsheet.paid) {
                    return 'Is paid'
                } else {
                    return 'Is not paid'
                }
        },
     setAsPaid() {
                this.jobsheet.paid = true


                 axios
                    .patch(`/api/v1/jobsheets/${this.jobsheet.id}/`, this.jobsheet)
                    .then(response => {
                        toast({
                            message: 'The changes was saved',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
                
            }
    }
}
</script>